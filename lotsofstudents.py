from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from catalog_setup import Base, User, Student, Prize

engine = create_engine('sqlite:///studentswithusers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create a sample user
User1 = User(name="Tim Williams", email="tinnyTim@udacity.com")
session.add(User1)
session.commit()


#Create students
Student1 = Student(name="Dan Thomas", user=User1)
session.add(Student1)
session.commit()

Student2 = Student(name="Lisa Ladio", user=User1)
session.add(Student2)
session.commit()


# Create Prizes for Students
Prize1 = Prize(name="Best Debator 2017", description="Best Debator of the graduating senior class", student= Student2, user=User1)
session.add(Prize1)
session.commit()

Prize2 = Prize(name="Best Science Award 2017", description="Best Science student of the graduating senior class", student=Student1, user=User1)
session.add(Prize2)
session.commit()


print "completed initial database populate!"