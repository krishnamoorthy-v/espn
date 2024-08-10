from mongo_config import db

class Feeds(db.Document):
    title = db.StringField(required=True)
    subDescription = db.StringField()
    description = db.StringField(required=True)
    posterImg = db.StringField(required=True)
    status = db.StringField()