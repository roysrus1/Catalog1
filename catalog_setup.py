#code to setup initial scehma for student/prize catalog

from sqlalchemy import Column, ForeignKey, Integer, String, BINARY, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

import datetime

Base = declarative_base()

#define User table - Users are typically teachers or administrators that add students and the prizes they have won to the database
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'name': self.name,
           'id': self.id,
           'email': self.email
       }

#define Student table
class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer,ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'name': self.name,
           'id': self.id,
           'user_id': self.user_id
       }

#define Prize table
class Prize(Base):
    __tablename__ = 'prize'


    name =Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(250))
    student_id = Column(Integer,ForeignKey('student.id'))
    student = relationship(Student)
    user_id = Column(Integer,ForeignKey('user.id'))
    user = relationship(User)
    time = Column(DateTime, default=datetime.datetime.utcnow)

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'name': self.name,
           'description': self.description,
           'student_id': self.student_id,
           'id': self.id,
           'user_id': self.user_id
       }


engine = create_engine('sqlite:///studentswithusers.db')


Base.metadata.create_all(engine)
