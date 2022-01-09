from fastapi import FastAPI,Depends,status,Response
import uvicorn
from . import schemas,database,models
from .schemas import Blog
from sqlalchemy.orm import Session


app=FastAPI()

models.Base.metadata.create_all(database.engine)
@app.get("/")
def hello():
    return "hello world"

def get_db():
    db=database.SessionLocal()
    try:
         yield db
    finally:
           db.close()




@app.post("/blog")
def creating_blogs(request:Blog,response:Response,db:Session=Depends(get_db)):
    new_blog=models.Blogs(title=request.name,Descr=request.descr)
    db.add(new_blog)
    response.status_code=status.HTTP_201_CREATED
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get("/blogs")
def dispaly_blogs(db:Session=Depends(get_db)):
    blogs=db.query(models.Blogs).all()
    return blogs
@app.get("/blogs/{id}")
def show(id,response:Response,db:Session=Depends(get_db)):
    blogs=db.query(models.Blogs).filter(models.Blogs.id==id).first()
    if not blogs:
        response.status_code=status.HTTP_404_NOT_FOUND
        return {"details":f"id {id} not found"}
    response.status_code = status.HTTP_302_FOUND
    return blogs

@app.delete("/blogs/{id}")
def delete_blog(id,db:Session=Depends(get_db)):
    db.query((models.Blogs)).filter(models.Blogs.id==id).delete()
    db.commit()

@app.put("/blogs/{id}")
def put(id,db:Session=Depends(get_db)):









if __name__ =="__main.py__":
    uvicorn.run(app,port="4000")