from pydantic import BaseModel
class account_details(BaseModel):
      #account_no : int
      name : str
      amount : int
