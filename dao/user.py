from mongo_config import db
from dao.roles import Roles

class Users(db.Document):
    fullName = db.StringField(required = True)
    email = db.EmailField(unique = True,max_length = 30,required = True)
    mobileNo = db.StringField(unique = True,max_length = 10,required = True,regex = r'^\+?\d{9,15}$')
    mobileNoCode = db.IntField(max_length = 8,required = True)
    password = db.StringField(required = True)
    roleId = db.ReferenceField(Roles,required = True)
    profileImg = db.StringField() 
    geo_location =db.ListField(db.StringField(required = True))

    



    

