from mongo_config import db

class Roles(db.Document):
    name =db.StringField(unique=True)

    