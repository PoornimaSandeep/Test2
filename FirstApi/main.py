import uvicorn
from fastapi import FastAPI
app = FastAPI()


@app.get("/")
def hi():
    return f"hello world"


@app.get("/hello/{name}")
def hello_(name):
    return f"hello world {name}"

food_items={
    "breakfast":["dosa","idli"],
    "lunch":["full_meals","chapathi"],
     "snaks":["gobi","panipuri"] }

@app.get("/menu/{food_name}")
def menu(food_name):
    return food_items.get(food_name)

@app.post("/data/")
def  post_data(name,phone_number):
    return f"title{name} name {phone_number}"


if __name__ ==" __main__ ":
    uvicorn.run(app)

