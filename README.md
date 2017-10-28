# Catalog Application - catalog.py
Code for catalog project assignment

#New section for LightSail documentation

#Server & App info:
IP address: 54.236.38.136
SSH Port: 2200
URL: http://54.236.38.136/

#Summary of Software Installed:

1. apache2
2. libapache2-mod-wsgi
3. postgresql
4. git
5. psycopg2 sqlalchemy
6. python-pip python-dev build-essential
7. pip install --upgrade pip
8. pip install --upgrade virtualenv

#Summary of configuration changes made:

1. For the python database code in all 3 py files, changed class User to class Owner.  This was because User was a reserved class.
2. For the python database code in all 3 py files, changed the engine from sqlite to postgres.  The associated URL info also changed.

3. In the catalog.py code, the app.secret_key had to be defined outside the if _name_ = '_main_' block since this was code was now being called by the wsgi code.

4. The path to client_secrets.json had to be specified else the file was not being found.
5.  The /etc/apache2/sites-enabled/000-default.conf was updated to call /var/www/html/myapp.wsgi for port 80.
6. The /var/www/html/myapp.wsgi file was updated to call catalog.py from /var/www/html/Catalog1.
7. Changes were made to the UFW and SSH settings on the Lightsail portal per the project details at:
https://classroom.udacity.com/nanodegrees/nd004/parts/00413454014/modules/357367901175462/lessons/3573679011239847/concepts/ce268cfe-99ec-49be-9326-876375f89a22

TinyURL for the above is:  https://tinyurl.com/y9z25kn2

8. Two users with different privilege levels were defined in postgres sql.  The first user ('king') had all privileges, allowing this user to create the database and the tables.  The second user ('catalog') had update privileges only, this user was used in the catalog.py code to ensure any malacious side effects from the web application would have limited damage.
Updates were made on the Google Cloud Portal (API/Credentials/Client id for web client) to authorize the code running on this lighsail ubuntu instance.  This included allowing http://54.236.38.136 as an Authorized Javascript origin and http://ec2-54-236-38-136.compute-1.amazonaws.com/oauth2callback as an Authorized redirect URI.  This hostname corresponded to the ip address of the same vm.

List of 3rd Party Resources used:

1) SQLAlchemy
2) Python Flask 
3) Python functools.wraps
4) Python Requests LIbrary
5) Python httplib2
6) Python oauth2client



*********************** OLD INFO BELOW ON RUNNING SAME APP IN VAGARANT *********************************




#Prerequisites
# Installing the Vagrant VM for ud330 - Authentication & Authorization

**Note: If you already have a vagrant machine installed from previous Udacity courses skip to the 'Fetch the Source Code and VM Configuration' section**

In Lessons 2,3 and 4 of this course, you'll use a virtual machine (VM) to run a web server and a web app that uses it. The VM is a Linux system that runs on top of your own machine.  You can share files easily between your computer and the VM.

We're using the Vagrant software to configure and manage the VM. Here are the tools you'll need to install to get it running:

### Git

If you don't already have Git installed, [download Git from git-scm.com.](http://git-scm.com/downloads) Install the version for your operating system.

On Windows, Git will provide you with a Unix-style terminal and shell (Git Bash).
(On Mac or Linux systems you can use the regular terminal program.)

You will need Git to install the configuration for the VM. If you'd like to learn more about Git, [take a look at our course about Git and Github](http://www.udacity.com/course/ud775).

### VirtualBox

VirtualBox is the software that actually runs the VM. [You can download it from virtualbox.org, here.](https://www.virtualbox.org/wiki/Downloads)  Install the *platform package* for your operating system.  You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it.

**Ubuntu 14.04 Note:** If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center, not the virtualbox.org web site. Due to a [reported bug](http://ubuntuforums.org/showthread.php?t=2227131), installing VirtualBox from the site may uninstall other software you need.

### Vagrant

Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem.  [You can download it from vagrantup.com.](https://www.vagrantup.com/downloads) Install the version for your operating system.

**Windows Note:** The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.

## Fetch the Source Code and VM Configuration

**Windows:** Use the Git Bash program (installed with Git) to get a Unix-style terminal.
**Other systems:** Use your favorite terminal program.

From the terminal, run:

    git clone https://github.com/udacity/OAuth2.0 oauth

This will give you a directory named **oauth** complete with the source code for the flask application, a vagrantfile, and a bootstrap.sh file for installing all of the necessary tools.

## Run the virtual machine!

Using the terminal, change directory to oauth (**cd oauth**), then type **vagrant up** to launch your virtual machine.


## Running the Catalog Menu App
Once it is up and running, type **vagrant ssh**. This will log your terminal into the virtual machine, and you'll get a Linux shell prompt. When you want to log out, type **exit** at the shell prompt.  To turn the virtual machine off (without deleting anything), type **vagrant halt**. If you do this, you'll need to run **vagrant up** again before you can log into it.


Now that you have Vagrant up and running type **vagrant ssh** to log into your VM.  change to the /vagrant directory by typing **cd /vagrant**. This will take you to the shared folder between your virtual machine and host machine.

## Running the Catalog Application

Type **ls** to ensure that you are inside the directory that contains catalog.py, catalog_setup.py, lotsosstudents.py and two directories named 'templates' and 'static'

Now type **python catalog_setup.py** to initialize the database.

Type **python lotsofstudents.py** to populate the database with students and prizes.

Type **python catalog.py** to run the Flask web server. In your browser visit **http://localhost:5000** to view the student menu app.

If you are not logged on, you can view the students and prizes populated via the lotsofstudents.py (initially).

If you choose to log on, you will be redirected to a google authentication process.  Once logged on, you should be able to view, add, edit, and delete students and prize items.
