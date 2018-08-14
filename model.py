from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Place your database schema code here

# Example code:
class Account(Base):
    __tablename__ = "accounts"
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String, primary_key = True)
    acc_type = Column(String)
    password= Column(String)
    gender= Column(String)
    birth = Column(String)

    def __repr__(self):
        return ("first_name: {}, last_name: {},Username: {}, Account Type: {},Password: {},Gender: {}, Birth: {}"
        .format(self.first_name,self.last_name,self.username, self.acc_type,self.password,self.gender,self.birth))