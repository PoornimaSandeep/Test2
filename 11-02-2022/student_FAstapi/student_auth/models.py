from database import Base
from sqlalchemy import Column, Integer, String


class user_model(Base):
    __tablename__ = 'authurization_table'
    stu_id = Column(Integer,primary_key=True)
    name = Column(String)
    password=Column(String)
    email=Column(String)