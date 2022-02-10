from fastapi import FastAPI,Depends
from models import add_data
from models import add_data
from sqlalchemy.orm import Session
import models
from database import engine
from service import service_data,service_retrieve
from utils import get_db
from Schemas import account_details
import uvicorn

app=FastAPI()

models.Base.metadata.create_all(bind=engine)


@app.post("/add")
def add(account:account_details,db:Session=Depends(get_db)):
    new_customer=models.add_data(name=account.name,amount=account.amount)
    return service_data(new_customer,db)

@app.get("/")
def display(db : Session = Depends(get_db)):
    return service_retrieve(db)

if __name__ == '__main__':
    uvicorn.run(app)