from .database import Base
from sqlalchemy import  Column,Integer,String


class Blogs(Base):
    __tablename__ ='Blogs'
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String)
    Descr=Column(String)
