from fastapi import FastAPI, Depends,UploadFile,File
import uvicorn
from schemas import User
from sqlalchemy.orm import Session
from utils import get_db,save_data
import models
from database import engine
import pandas as pd
from fastapi_csv import FastAPI_CSV
import csv
from typing import List


app = FastAPI()

models.Base.metadata.create_all(bind = engine)

@app.post('/insert',status_code=201 )
def insert_data(std : User, db : Session = Depends(get_db)):
    new_user=models.user_model(name=std.name,password=std.password,email=std.email)
    return  save_data(new_user,db)
