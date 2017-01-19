#!/usr/bin/env python
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(String(20),primary_key=True)
    name = Column(String(20))

engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/test')

DBsession = sessionmaker(bind=engine)
session = DBsession()
user = session.query(User).filter(User.id=='5').one()

print('type:',type(user))
print('name:',user.name)
session.close()
