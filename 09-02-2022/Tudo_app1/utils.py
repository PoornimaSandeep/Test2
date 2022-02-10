from database import SessionLocal
from models import add_data

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def retrive_data(db):
    data=db.query(add_data).filter(add_data.account_no>1)
    response={}
    for i in data:
        response['account_no']=data.account_no
        response['name'] = data.name
        response['amount'] = data.amount
    return response