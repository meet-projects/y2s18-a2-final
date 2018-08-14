# Database related imports
# Make sure to import your tables!
from model import Base, Account

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# You can change the name of your database, just change project.db to whatever you want (make sure to include .db at the end!)
# Make sure you have the same name for the database in the app.py file!
engine = create_engine('sqlite:///project.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Your database functions are located under here (querying, adding items, etc.)


def add_account(username,password,birth,gender,acc_type):
    if check_user_exists(username)==False:
        add_account = Account(
            acc_type = acc_type,
            username = username,
            password = password,
            birth = birth,
            gender = gender)
        session.add(add_account)
        session.commit()
    else:
        raise Exception("User already exists")

def check_user_exists(username):

    account = session.query(Account).filter_by(username=username).first()
    if account==None:

        return False
    else:
        return True


def check_user_and_pass(username, password):
    print("hello")
    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(Account).filter_by(username=username,password=password)
    print("check")
    result = query.first()
    if result is not None:
        return True
    else:
       print('wrong password!')
       return False
       
    
    
    # check = session.query(Account).filter(username)