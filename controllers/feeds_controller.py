from flask import Blueprint, request
from dto.response_model import ResponseModel
from  services.feeds_service import all_feeds, new_feed, get_feed, update_feed, delete_feed

feeds_api = Blueprint('feeds_api',__name__)

#Get All Feeds
@feeds_api.route('/feeds',methods=["GET"])
def get_all_feeds():
    data = all_feeds()
    return ResponseModel(1,"All Feeds",data.to_json()).to_json_response(200)

#Create New Feed
@feeds_api.route('/feeds',methods=["POST"])
def create_new_feed():
    title = request.form.get('title')
    subdescription = request.form.get('subDescription')
    description = request.form.get('description')
    image = request.files['posterImg']
    status = request.form.get('status')
    data = new_feed(title, subdescription, description, image, status)
    return ResponseModel(1,"Feed Created",data.to_json()).to_json_response(200)

#Get Feeds By Id
@feeds_api.route('/feeds/<feedId>',methods=["GET"])
def get_feed_by_id(feedId):
    data = get_feed(feedId)
    return ResponseModel(1,"Feed Getted",data.to_json()).to_json_response(200)

#Update Feed By Id
@feeds_api.route('/feeds/<feedId>',methods=["PUT"])
def update_feed_by_id(feedId):
    title = request.form.get('title')
    subdescription = request.form.get('subDescription')
    description = request.form.get('description')
    image = request.files['posterImg']
    status = request.form.get('status')
    data = update_feed(feedId, title, subdescription, description, image, status)
    return ResponseModel (1,"Feed Updated",data.to_json()).to_json_response(200)

#Delete Feed By Id
@feeds_api.route('/feeds/<feedId>',methods=["DELETE"])
def delete_feed_by_id(feedId):
    data = delete_feed(feedId)
    return ResponseModel(1,"Feed Deleted",data.to_json()).to_json_response(200)