from mongo_config import db


class team(db.Document):
    # _id  = db.StringField(default=None)
    teamName = db.StringField(default=None)
    logo = db.StringField(default=None)
    # playersid= db.StringField(default=None)
