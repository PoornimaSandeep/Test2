from database import insert_data
import models
from utils import database_retrive,\
    database_retrive_one,database_update,database_delete,sub_update
def service_insert(new_user,db):
    return insert_data(new_user,db)

def service_csv(l2,db):
    for i in range (len(l2)):
         if i>0:
            data=l2[i]
            total=int(data[1])+int(data[2])+int(data[3])+int(data[4])+int(data[5])+int(data[6])
            average=total/6
            if average>90:
                status='distinction'
            if average>75 and average>90:
                status='average'
            if average<75:
               status='fail'

            if status=='fail':
               chance='yes'
            else:
                chance='no'
            new_user = models.Student_model(name=data[0], Kannada=data[1], English=data[2], Hindhi=data[3],
                                           Maths=data[4], Science=data[5], Social=data[6], status=status,
                                           chance=chance)
            db.add(new_user)
            db.commit()
            db.refresh(new_user)

    return 'done'


def service_retrive(db):
    return database_retrive(db)

def service_retrive_one(id,db):
    return database_retrive_one(id,db)



def service_update(id,kannada,English,Hindhi,Maths,Science,Social,status,chance,db):
    return database_update(id,kannada,English,Hindhi,Maths,Science,Social,status,chance,db)

def service_subject(id,kannada,English,Hindhi,Maths,Science,Social,db):
    return sub_update(id,kannada,English,Hindhi,Maths,Science,Social,db)


def service_delete(id,db):
    return database_delete(id,db)