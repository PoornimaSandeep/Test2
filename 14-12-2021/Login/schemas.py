from pydantic import BaseModel

class users(BaseModel):
      name:str
      email:str
      password:str
