from database import SessionLocal
import models
from models import Student_model
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def save_data(new_user,db):
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return f'successfully created {new_user.stu_id}'
