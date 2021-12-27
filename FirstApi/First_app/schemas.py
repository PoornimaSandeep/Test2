from typing import Optional, List
from pydantic import BaseModel


class data(BaseModel):
    name: str
    ph_no: int


class ItemBase(BaseModel):
    title : str
    description : Optional[str]=None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class Userbase(BaseModel):
    email: str


class UserCreate(Userbase):
    password: str


class User(Userbase):
    id: int
    is_active: bool
    item: List[Item] = []

    class Config:
        orm_mode = True

