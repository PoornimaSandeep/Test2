from database import Base
from sqlalchemy import Column, Integer, String


class Student_model(Base):
    __tablename__ = 'student_data'
    stu_id = Column(Integer,primary_key=True)
    name = Column(String)
    Kannada = Column(String)
    English = Column(String)
    Hindhi = Column(String)
    Maths = Column(String)
    Science = Column(String)
    Social = Column(String)
    status=Column(String)
    chance=Column(String)

