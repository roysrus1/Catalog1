from flask import Flask, render_template, request, redirect, jsonify, url_for, flash

from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker
from catalog_setup import Base, Student, Prize, User

from flask import session as login_session
import random, string

from functools import wraps

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
from oauth2client.client import AccessTokenCredentials
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)

CLIENT_ID = json.loads(open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Student Catalog Application"

#Connect to Database and create database session
engine = create_engine('sqlite:///studentswithusers.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

#Login  - generate session state token and render html page to login
@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))

    login_session['state'] = state

    return render_template('login.html', STATE=state)

#Authenticate via Google  - generate session state token and render html page to login
@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token

    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data


    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token

    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s' % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        #response = make_response(json.dumps(result.get('error')), 500)
        response = make_response(json.dumps('Failed to dump.'), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.

    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response


    stored_credentials = login_session.get('credentials')
    login_session['credentials'] = credentials.access_token

    stored_gplus_id = login_session.get('gplus_id')
    if stored_credentials is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response


    login_session['gplus_id'] = gplus_id
    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}


    answer = requests.get(userinfo_url, params=params)
    data = answer.json()
    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

   # Generate Welcome screen based on Google authentication success
    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output

#create a decorator function for logins:
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in login_session:
            return redirect('/login')
        return f(*args, **kwargs)
    return decorated_function


# Create a new user and add to the database
def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session['email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id

# For a given user_id, return the user record
def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user

# For a given user email, return the user record
def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None


# DISCONNECT - Revoke a current user's token and reset their login_session
@app.route('/gdisconnect')
def gdisconnect():

    credentials = AccessTokenCredentials(login_session['credentials'], 'user-agent-value')
    #credentials = login_session.get('credentials')

    if credentials is None:
        response = make_response(json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    access_token = credentials.access_token

    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    result1 = h.request(url, 'GET')[1]
    err1 = 'Token expired or revoked'

    #Delete Login session parameters as part of logging out user
    if (err1 in result1) or result['status'] == '200':
        del login_session['credentials']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        credentials = None
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return redirect('/student/')
    else:
        err_msg = 'Failed to revoke token for given user.' + result['status'] + str(result1)
        response = make_response(json.dumps(err_msg, 400))
        response.headers['Content-Type'] = 'application/json'
        return response



#JSON API to view prizes won by a particular Student
@app.route('/student/<int:student_id>/prizes/JSON')
def studentPrizeJSON(student_id):
    prizes = session.query(Prize).filter_by(student_id=student_id).all()
    return jsonify(Prizes=[i.serialize for i in prizes])

#JSON API to view a specific prize won by a specific student
@app.route('/student/<int:student_id>/prizes/<int:prize_id>/JSON')
def prizesItemJSON(student_id, prize_id):
    prize = session.query(Prize).filter_by(id=prize_id).one()
    return jsonify(Prize_Item=prize.serialize)

#JSON API to view all students
@app.route('/student/JSON')
def studentsJSON():
    students = session.query(Student).all()
    return jsonify(students=[r.serialize for r in students])

#JSON API to view all students and the prizes they have won
@app.route('/catalog.json')
def catalogJSON():
    catalog = []
    students = session.query(Student).all()
    for student in students:
        studentDict = {'Student Name': student.name, 'Student ID': student.id}
        catalog.append(studentDict)
        prizes = session.query(Prize).filter_by(student_id=student.id).all()
        for prize in prizes:
            PrizeDict = {'     Prize Name': prize.name,
                         '     Prize Id': prize.id,
                         '     Prize Description': prize.description}
            catalog.append(PrizeDict)


    jsonStr = json.dumps(catalog, indent=4)
    parsed = json.loads(jsonStr)
    return jsonify(students=parsed)


#Show all students
@app.route('/')
@app.route('/student/')
def showStudents():
    students = session.query(Student).order_by(asc(Student.name))
    prizes = session.query(Prize).order_by(desc(Prize.time)).all()
    table_rows = map(None, students, prizes)

    username = None
    if 'username' in login_session:
        return render_template('students.html', table_rows=table_rows,
                               username=login_session['username'])
    else:
        return render_template('publicstudents.html', table_rows=table_rows,
                               username=None)

#Create a new student
@app.route('/student/new/', methods=['GET', 'POST'])
@login_required
def newStudent():

    if request.method == 'POST':
        owner = session.query(User).filter_by(id=login_session['user_id']).one()
        newStudent = Student(name=request.form['name'], user=owner)
        session.add(newStudent)
        session.commit()
        flash('New Student %s Successfully Created' % newStudent.name)
        return redirect(url_for('showStudents'))
    else:
        return render_template('newStudent.html', username=login_session['username'])

#Edit a student
@app.route('/student/<int:student_id>/edit/', methods=['GET', 'POST'])
@login_required
def editStudent(student_id):

    editedStudent = session.query(Student).filter_by(id=student_id).one()
    creator = getUserInfo(editedStudent.user_id)

    if creator.name != login_session['username']:
        flash('Student %s can only be Edited by owner %s' % (editedStudent.name, creator.name))
        return redirect('/student/')

    if request.method == 'POST':
        if request.form['name']:
            editedStudent.name = request.form['name']
            session.add(editedStudent)
            session.commit()
            flash('Student Successfully Edited %s' % editedStudent.name)
            return redirect(url_for('showStudents'))
    else:
        return render_template('editStudent.html', student=editedStudent)


#Delete a student
@app.route('/student/<int:student_id>/delete/', methods=['GET', 'POST'])
@login_required
def deleteStudent(student_id):

    studentToDelete = session.query(Student).filter_by(id=student_id).one()
    creator = getUserInfo(studentToDelete.user_id)

    if creator.name != login_session['username']:
        flash('Student %s can only be Deleted by owner %s ' % (studentToDelete.name, creator.name))
        return redirect('/student/')

    if request.method == 'POST':

        #delete prizes associated with the student being deleted along with deleting the student
        prizes = session.query(Prize).filter_by(student_id=student_id).all()
        for prize in prizes:
            session.delete(prize)
            session.commit()
        session.delete(studentToDelete)
        session.commit()

        flash('%s Successfully Deleted' % studentToDelete.name)
        return redirect('/student/')
    else:
        return render_template('deleteStudent.html', student=studentToDelete,
                               username=login_session['username'])

#Show prizes won by a specific student
@app.route('/student/<int:student_id>/')
@app.route('/student/<int:student_id>/prizes/')
def showStudent(student_id):
    student = session.query(Student).filter_by(id=student_id).one()
    prizes = session.query(Prize).filter_by(student_id=student_id).all()

    username = None
    if 'username' in login_session:
        username = login_session['username']

    creator = getUserInfo(student.user_id)

    return render_template('prize.html', student=student, prizes=prizes,
                           creator=creator, username=username)



#Create a new prize
@app.route('/student/<int:student_id>/prizes/new/', methods=['GET', 'POST'])
def newPrize(student_id):
    if 'username' not in login_session:
        return redirect('/login')

    student = session.query(Student).filter_by(id=student_id).one()
    creator = getUserInfo(student.user_id)

    if creator.name != login_session['username']:
        flash('Student %s prizes can only be Edited by owner %s' % (student.name, creator.name))
        return redirect('/student/')

    if request.method == 'POST':
        owner = session.query(User).filter_by(id=login_session['user_id']).one()
        newPrize = Prize(name=request.form['name'], description=request.form['description'],
                         student=student, user=owner)
        session.add(newPrize)
        session.commit()
        flash('New Prize %s Item Successfully Created' % (newPrize.name))
        return redirect(url_for('showStudent', student_id=student_id))
    else:
        return render_template('newprize.html', student_id=student_id)

#Edit a prize
@app.route('/student/<int:student_id>/prizes/<int:prize_id>/edit', methods=['GET', 'POST'])
def editPrize(student_id, prize_id):

    if 'username' not in login_session:
        return redirect('/login')

    student = session.query(Student).filter_by(id=student_id).one()
    creator = getUserInfo(student.user_id)

    if creator.name != login_session['username']:
        flash('Student %s prizes can only be Edited by owner %s' % (student.name, creator.name))
        return redirect('/student/')

    editedPrize = session.query(Prize).filter_by(id=prize_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedPrize.name = request.form['name']
        if request.form['description']:
            editedPrize.description = request.form['description']
        session.add(editedPrize)
        session.commit()
        flash('Prize Item Successfully Edited')
        return redirect(url_for('showStudent', student_id=student_id))
    else:
        return render_template('editprize.html', student_id=student_id, prize=editedPrize,
                               username=login_session['username'])


#Delete a prize
@app.route('/student/<int:student_id>/prizes/<int:prize_id>/delete', methods=['GET', 'POST'])
def deletePrize(student_id, prize_id):

    if 'username' not in login_session:
        return redirect('/login')

    student = session.query(Student).filter_by(id=student_id).one()
    creator = getUserInfo(student.user_id)

    if creator.name != login_session['username']:
        flash('Student %s prizes can only be edited by owner %s' % (student.name, creator.name))
        return redirect('/student/')

    prizeToDelete = session.query(Prize).filter_by(id=prize_id).one()

    if request.method == 'POST':
        session.delete(prizeToDelete)
        session.commit()
        flash('Prize Item Successfully Deleted')
        return redirect(url_for('showStudent', student_id=student_id))
    else:
        return render_template('deletePrize.html', prize=prizeToDelete,
                               student_id=student_id, username=login_session['username'])



if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
