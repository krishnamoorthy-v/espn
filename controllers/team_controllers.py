from flask import Blueprint, request

from dao.team_dao import team
from dto.response_model import ResponseModel

team_api = Blueprint('team_api', __name__)


@team_api.route('/', methods=['POST'])
def post_data():
    body = request.get_json()
    data = team(**body)
    data.save()
    return ResponseModel(1, "Details Added", data.to_json()).to_json_response(200)
    

@team_api.route('/', methods=['GET'])
def get_all():
    data = team.objects()
    return ResponseModel(1,"Details List", data.to_json()).to_json_response(200)
    

@team_api.route('/<id>', methods=['GET'])
def get_one_detail(id: str):
    data = team.objects.get_or_404(id=id)
    return ResponseModel(1, "Details", data.to_json()).to_json_response(200)



@team_api.route('/<id>', methods=['PUT'])
def update_data(id: str):
    body = request.get_json()
    data = team.objects.get_or_404(id=id)
    data.update(**body)
    return get_one_detail(id)


@team_api.route('/<id>', methods=['DELETE'])
def delete_data(id: int):
    data = team.objects.get_or_404(id=id)
    data.delete()
    return ResponseModel(1, "Detail Deleted", data.to_json()).to_json_response(200)