from database import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    name :str
    password:str
    email:str