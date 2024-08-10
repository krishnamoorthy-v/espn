from mongo_config import db
from dao.player import Player
from dao.team_dao import team


class ScoreCard(db.Document):
    match_id = db.StringField()
    inning = db.IntField()
    batting_team_id = db.ReferenceField(team)
    bowling_team_id = db.ReferenceField(team)
    over = db.IntField()
    ball = db.IntField()
    batsman = db.ReferenceField(Player)
    non_striker = db.ReferenceField(Player)
    bowler = db.ReferenceField(Player)
    super_over = db.BooleanField()
    wide_run = db.IntField()
    by_run = db.IntField()
    legby_run = db.IntField()
    noball_run = db.IntField()
    penality_run = db.IntField()
    batsman_run = db.IntField()
    extra_run = db.IntField()
    total_run = db.IntField()
