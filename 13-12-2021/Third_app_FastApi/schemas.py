from pydantic import BaseModel


class Blog(BaseModel):
      name:str
      descr:str
