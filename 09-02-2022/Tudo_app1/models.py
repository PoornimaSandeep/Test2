from database import Base
from sqlalchemy import Column, Integer, String
from uuid import uuid4


class add_data(Base):
    __tablename__ = 'sbi_bank'
    account_no = Column(Integer,primary_key=True)
    name = Column(String)
    amount = Column(Integer)
