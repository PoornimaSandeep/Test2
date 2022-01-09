from fastapi import FastAPI,Response,Depends
from . import database,models
from sqlalchemy.orm import Session
from .schemas import users
import uvicorn

app=FastAPI()

#models.Base.metadata.createall(database.engine)
models.Base.metadata.create_all(database.engine)
def get_db():
    db=database.SessionLocal()
    try:
        yield db
    finally:
         db.close()

@app.post("/users")
def create_user(request:users,db:Session=Depends(get_db)):
    new_user=models.Users(name=request.name,email=request.email,password=request.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return "created"







if __name__=="__main__":
    uvicorn.run(app)
