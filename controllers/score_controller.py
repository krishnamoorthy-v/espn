import json

from flask import Flask, Blueprint, request

from dto.response_model import ResponseModel
from services.score_service import get_paginate_service
from services.score_service import save_to_db

score_api = Blueprint("score_api", __name__)


@score_api.route("/", methods=["POST"])
def save_score():
    """
    get csv file to store it in the database ScoreCard
    :return: "csv data stored"
    """
    file = request.files["csvfile"]
    status = save_to_db(file)
    return status


@score_api.route("/paginate", methods=["POST"])
def disp_page():
    """
    To display the no of document per page
    :return: array of json(document)
    """
    page = request.args.get("page", type=int)
    count = request.args.get("count", type=int)
    x = get_paginate_service(page, count)
    return ResponseModel(1, "Details retrieved", json.dumps(x)).to_json_response(200)
