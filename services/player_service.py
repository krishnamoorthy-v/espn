import base64
from mongoengine import NotUniqueError, ValidationError
from dao.player import Player
from dto.myexception import myException

import json


def save_player_service(input):
    try:
        data = Player(**input)
        data.save()
    except NotUniqueError as e:
        raise myException("Details Already Exits")
    except ValidationError as e:
        raise myException(e.message)
    return data


def upload_file_service(id, file):
    bin_file = file.read()
    enc = base64.b64encode(bin_file)
    bin_message = enc.decode("utf-8")
    try:
        data = Player.objects.get_or_404(id=id)
    except ValidationError as e:
        raise myException(e.message)

    data.update(image=bin_message)
    data = Player.objects.get_or_404(id=id)

    return data


def update_player_service(id, input):
    try:
        data = Player.objects.get_or_404(id=id)
        data.update(**input)
        data = Player.objects.get_or_404(id=id)
    except NotUniqueError as e:
        raise myException("Details Already Exits")

    except ValidationError as e:
        raise myException(e.message)
    return data


def delete_one_details_service(id):
    try:
        data = Player.objects.get_or_404(id=id)
    except ValidationError as e:
        raise myException(e.message)
    data.delete()
    return data


def get_one_player_service(id):
    try:
        data = Player.objects.get_or_404(id=id)
    except ValidationError as e:
        raise myException(e.message)
    return data


def get_all_player_service():
    data = Player.objects()
    if not data:
        raise myException("No data found")
    return data


def paginate_order_service(page, count, field):
    data = Player.objects.order_by(field).paginate(page=page, per_page=count)
    x = []
    for row in data.items:
        x.append(json.loads(row.to_json()))
    return x


def like_query_servic(match):
    regex = r'^{}'.format(match)
    data = Player.objects.filter(name__regex=regex)
    return data
