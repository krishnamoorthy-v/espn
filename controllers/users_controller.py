from flask import request,Blueprint
from dto.response_model import ResponseModel
from flask_jwt_extended import jwt_required
from services.users_service import get_all_users, create_user, get_user_id, update_one_user,\
                                   delete_one_user, user_with_role, user_login, token_refresh,\
                                   login_for_admin,user_image_encode

users_api = Blueprint('users_api',__name__)


# Get All Users
@users_api.route('/users',methods=['GET'])
@jwt_required()
def get_users():
    data = get_all_users().to_json()
    return ResponseModel(1,"Users",data).to_json_response(200)


# Create New User
@users_api.route('/users',methods=['POST'])
def post_user():
    body = request.get_json()
    data = create_user(body)
    return ResponseModel(1,"User Created",data.to_json()).to_json_response(200)


#Upload User Image
@users_api.route('/users/<user_id>/images',methods=['POST'])
def image_encode(user_id):
    file = request.files['profileImg']
    data = user_image_encode(file,user_id)
    return ResponseModel(1,"Image Updated",data.to_json()).to_json_response(200) 

    
# Get User By ID
@users_api.route('/users/<user_id>',methods=['GET'])
@jwt_required()
def get_one_users(user_id):
    data = get_user_id(id=user_id)
    if not data:
        return ResponseModel(1,"Invalid ID / No user found",).to_jsonify_response(404)
    return ResponseModel(1,"User",data.to_json()).to_json_response(200)


# Update User By ID
@users_api.route('/users/<user_id>',methods=['PUT'])
@jwt_required()
def update_users(user_id):
    body = request.get_json()
    data = update_one_user(user_id,body)
    return ResponseModel(1,"User Updated",data.to_json()).to_json_response(200)


#Delete User By ID
@users_api.route('/users/<user_id>',methods=['DELETE'])
@jwt_required()
def delete_users(user_id):
    data = delete_one_user(user_id)
    return ResponseModel(1,"User Deleted",data.to_json()).to_json_response(200)


#Create User With Role
@users_api.route('/signup',methods=['POST'])
def signup():
    body = request.get_json()
    data = user_with_role(body)
    return ResponseModel (1,"Signup Successfull",data.to_json()).to_json_response(200)


# Login For User
@users_api.route('/login',methods=['POST'])
def login():
    body = request.get_json()
    data = user_login(body)
    return ResponseModel (1,"Login Successfull",data).to_jsonify_response(200)


# Access Token Refresh
@users_api.route('/refresh',methods=['PUT'])
@jwt_required(refresh=True)
def valid_token():
    data = token_refresh()
    return ResponseModel (1,"Token Refreshed",data).to_jsonify_response(200)


# Login For Admin
@users_api.route('/admin/login',methods=['POST'])
def admin_login():
    body = request.get_json()
    data = login_for_admin(body)
    return ResponseModel (1,"Login Successfull",data).to_jsonify_response(200)
    
    
