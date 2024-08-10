from dao.match import Match
from dto.myexception import myException
from datetime import date
from datetime import datetime
from flask import Flask, request
from controllers.team_controllers import team
import json


# POST MATCH
def post_match(body):
    data = Match(**body)
    users = Match.objects(matchName=data.matchName)
    if not users:
        data.save()
        return data
    else:
        raise myException("MATCH NAME IS ALREADY CREATED !", 400)


# UPDATE MATCH
def update_match(body):
    data = Match(**body)
    users = Match.objects(matchName=data.matchName)
    if not users:
        data.save()
        return data
    else:
        raise myException('MATCH NAME WAS ALREADY CREATED !', 400)


def get_by_id(id):
    data = team.objects(id=id)
    return data


def get_match(data):
    dates = data.date
    today = date.today()
    value = str(today)

    d1 = datetime.strptime(dates, "%Y-%m-%d")
    d2 = datetime.strptime(value, "%Y-%m-%d")

    result1 = d1 - d2
    result = result1.days

    team_1 = get_by_id(data.team_id_1.id).to_json()

    # print(data.team_id_1)
    # print(data.team_id_1.id)
    # print(data)

    team_2 = get_by_id(data.team_id_2.id).to_json()

    data.team_id_1 = team_1
    data.team_id_2 = team_2

    if result == 0:
        fun = "Match on live"
        data.status = fun
        return data

    elif result > 0:
        fun = str(result)
        sat = "upcoming " + fun + "days on left"
        data.status = sat
        return data

    else:
        fun = "Finished"
        data.status = fun
        return data


def delete_by_match(id):
    data = Match.objects(id=id)
    if not data:
        raise myException("not found ", 400)
    data.delete()
    return data


