from mongo_config import db
from services.validation import Player_Validation

validate = Player_Validation()


class Player(db.Document):
    image = db.StringField()
    name = db.StringField(required=True)
    age = db.IntField(required=True, validation=validate.age_valid)
    address = db.StringField(required=True)
    phone_number = db.IntField(required=True, unique=True, validation=validate.phone_number_valid)
    email_id = db.EmailField(required=True, unique=True, max_length=30)
    type = db.StringField(required=True)
