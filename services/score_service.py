import csv
import json

from dao.score_card import ScoreCard
from dao.player import Player
from dao.team_dao import team


def save_to_db(file):
    string_of_data = file.read().decode("utf-8")
    array_of_dict = csv.DictReader(string_of_data.splitlines())
    for row in array_of_dict:
        # getting object id for team
        batting_team_id = team.objects.get_or_404(teamName=row["batting_team"])
        bowling_team_id = team.objects.get_or_404(teamName=row["bowling_team"])

        # getting object id for player
        batsman_id = Player.objects.get_or_404(name=row["batsman"])
        bowler_id = Player.objects.get_or_404(name=row["bowler"])
        non_striker_id = Player.objects.get_or_404(name=row["non_striker"])

        # store data to the score_card collection
        ScoreCard(
            match_id=row["match_id"],
            inning=row["inning"],
            batting_team_id=batting_team_id.id,
            bowling_team_id=bowling_team_id.id,
            over=row["over"],
            ball=row["ball"],
            batsman=batsman_id.id,
            non_striker=non_striker_id.id,
            bowler=bowler_id,
            super_over=row["is_super_over"],
            wide_run=row["wide_runs"],
            by_run=row["bye_runs"],
            legby_run=row["legbye_runs"],
            noball_run=row["noball_runs"],
            penality_run=row["penalty_runs"],
            batsman_run=row["batsman_runs"],
            extra_run=row["extra_runs"],
            total_run=row["total_runs"]
        ).save()

    return "csv data stored"


def get_paginate_service(page, count):
    x = []
    data = ScoreCard.objects.paginate(page, count)
    for row in data.items:
        x.append(json.loads(row.to_json()))
    return x
