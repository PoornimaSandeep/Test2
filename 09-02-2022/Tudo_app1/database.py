from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# import  models

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgress123@127.0.0.1:5432/postgres"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def add_user(new_customer,db):
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return f' your account created successfully with this {new_customer.account_no} account no'