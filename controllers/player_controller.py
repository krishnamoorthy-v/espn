import json
from flask import Blueprint, request
from services.validation import Player_Validation
from dto.response_model import ResponseModel
from services.player_service import save_player_service, upload_file_service, update_player_service, \
    delete_one_details_service, get_one_player_service, get_all_player_service, paginate_order_service, like_query_servic
from dao.player import Player

validate = Player_Validation()
player_api = Blueprint("player_api", __name__)


@player_api.route("/", methods=["POST"])
def save_player():
    """
    get the player information from the request call and store it in the db
    :return: json format information
    """
    input = request.get_json()
    data = save_player_service(input).to_json()
    return ResponseModel(1, "Details Added", data).to_json_response(200)


@player_api.route("/upload/<id>", methods=["PUT"])
def upload_file(id: str):
    """
    get the profile picture from the request call and store it in the particular player information in db
    :param id: represent particular player id
    :return: particular player information after update
    """
    file = request.files["file"]
    data = upload_file_service(id, file)
    return ResponseModel(1, "Profile updated", data.to_json()).to_json_response(200)


@player_api.route("/<id>", methods=["put"])
def update_player(id: str):
    input = request.get_json()
    data = update_player_service(id, input)
    return ResponseModel(1, "Details Updated", data.to_json()).to_json_response(200)


@player_api.route("/<id>", methods=["delete"])
def delete_one_detail(id: str):
    data = delete_one_details_service(id)
    return ResponseModel(1, "Details Deleted", data.to_json()).to_json_response(200)


@player_api.route("/<id>", methods=["get"])
def get_one_detail(id: str):
    data = get_one_player_service(id)
    return ResponseModel(1, "Details retrieved", data.to_json()).to_json_response(200)


@player_api.route("/", methods=["GET"])
def get_all_details():
    data = get_all_player_service()
    return ResponseModel(1, "Details retrieved", data.to_json()).to_json_response(200)


@player_api.route("/order/<field>", methods=["get"])
def paginate_order(field: str):
    page = request.args.get("page", type=int)
    count = request.args.get("count", type=int)
    x = paginate_order_service(page, count, field)
    return ResponseModel(1, "Details retrieved", json.dumps(x)).to_json_response(200)


@player_api.route("/filter", methods=["get"])
def filter_name():
    name = request.args.get("name")
    data = Player.objects.filter(name=name)
    return ResponseModel(1, "Details retrived", data.to_json()).to_json_response(200)


@player_api.route("/likequery", methods=["GET"])
def like_query():
    match = request.args.get("match")
    data = like_query_servic(match)
    return ResponseModel(1, "Details retrived", data.to_json()).to_json_response(200)