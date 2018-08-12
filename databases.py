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


def account(acc_type,username,password,birth,gender):
    add_account = Account(
        acc_type = acc_type,
        username = username,
        password = password,
        birth = birth,
        gender = gender)
    session.add(add_account)
    session.commit()
account("citizen","sir","meet18","1808","male")
account("admin","huh","meet18","1808","male")
