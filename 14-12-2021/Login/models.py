from .database import Base
from sqlalchemy import Column,Integer,String

class Users(Base):
      __tablename__ = 'Login_credential'
      em_id=Column(Integer,primary_key=True,index=True,autoincrement=True)
      name=Column(String)
      email=Column(String)
      password=Column(Integer)