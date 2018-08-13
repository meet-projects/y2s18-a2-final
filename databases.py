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
   # return True if account is not None else False
    if account==None:

        return False
    else:
        return True


def check_user_and_pass():
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])

    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(Users).filter(Users.email.in_([POST_USERNAME]), Users.password.in_([POST_PASSWORD]) )
    result = query.first()
    if result:
        session['logged_in'] = True
    else:
        flash('wrong password!')
return home
    
    
    # check = session.query(Account).filter(username)