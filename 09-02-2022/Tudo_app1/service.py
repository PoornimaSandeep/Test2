from models import add_data
from database import add_user
from utils import retrive_data

def service_data(new_customer,db):
    data=str(new_customer.account_no)
    if len(data)>=3:
       return add_user(new_customer,db)
    else:
        return'you entered account no is too small'

def service_retrieve(db):
    return retrive_data(db)