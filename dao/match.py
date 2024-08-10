from mongo_config import db
import json

class Match(db.Document):
    matchName = db.StringField(unique=True)
    date = db.StringField()
    status = db.StringField()
    location = db.StringField()
    team_id_1 = db.ReferenceField('team')
    team_id_2 = db.ReferenceField('team')

    def to_json_get(self,team_id_1,team_id_2):
        jsons={
            'matchName':self.matchName,
            "date":self.date,
            "status":self.status,
            "location":self.location,
            "team_id_1":json.loads(team_id_1),
            "team_id_2":json.loads(team_id_2)
        }
        return jsons



