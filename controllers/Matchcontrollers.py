from flask import request, Blueprint
from services.match_service import post_match, update_match, get_match, delete_by_match
from dto.response_model import ResponseModel
from dao.match import Match
import json
match_api = Blueprint('match_api', __name__)


# POST MATCH
@match_api.route('/', methods=['POST'])
def post_data():
    body = request.get_json()
    data = post_match(body)
    return ResponseModel(1, "Match Created", data.to_json()).to_json_response(200)


#GET ALL MATCH
@match_api.route('/', methods=['GET'])
def get_all():
    data = Match.objects()
    temp =[]
    for i in data:
        value = get_match(i)
        team_1 = value.team_id_1
        team_2 = value.team_id_2
        temp.append(value.to_json_get(team_1,team_2))
    return ResponseModel(1, "details ",temp).to_jsonify_response(200)


# GET ONE MATCH
@match_api.route('/<id>', methods=['GET'])
def get_one_detail(id: str):
    body = Match.objects.get_or_404(id=id)
    # print(body)
    data = get_match(body)
    # print(data)
    team_1 = data.team_id_1
    team_2 = data.team_id_2
    return ResponseModel(1, "GETTING MATCH", data.to_json_get(team_1, team_2)).to_jsonify_response(200)


# DELETE ONE MATCH
@match_api.route('/<match_id>', methods=['DELETE'])
def delete_data(match_id):
    data = delete_by_match(match_id)
    return ResponseModel(1, "Detail Deleted", data.to_json()).to_json_response(200)


# UPDATE MATCH
@match_api.route('/<id>', methods=['PUT'])
def update_data(id: str):
    body = request.get_json()
    data = update_match(body)
    return ResponseModel(1, "MATCH UPDATED", data.to_json()).to_json_response(200)


# DELETE ALL MATCH
@match_api.route('/', methods=['DELETE'])
def delete_all_data():
    data = Match.objects()
    data.delete()
    return ResponseModel(1, "All  Data deleted", data.to_json()).to_json_response(200)
