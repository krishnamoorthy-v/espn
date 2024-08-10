from flask import Blueprint, request
from dto.response_model import ResponseModel
from  services.roles_service import create_role, get_all_roles, get_by_id, update_by_id, delete_by_id

roles_api = Blueprint('roles_api',__name__)

#Get All Roles
@roles_api.route('/roles',methods=["GET"])
def get_all():
    data = get_all_roles().to_json()
    return ResponseModel(1,"All Roles",data).to_json_response(200)

#Create New Role
@roles_api.route('/roles',methods=['POST'])
def create_new_role():
    body = request.get_json()
    data = create_role(body) 
    return ResponseModel(1,"Role Created",data.to_json()).to_json_response(200)

#Get Role By ID
@roles_api.route('/roles/<role_id>',methods=["GET"])
def get_role_by_id(role_id):
    data = get_by_id(id=role_id)
    return ResponseModel(1,"Role",data.to_json()).to_json_response(200)

#Update Role By ID
@roles_api.route('/roles/<role_id>',methods=["PUT"])
def update_role_by_id(role_id):
    body = request.get_json()
    data = update_by_id(role_id, body)
    return ResponseModel (1,"Role Updated",data.to_json()).to_json_response(200)

#Delete Role By ID
@roles_api.route('/roles/<role_id>',methods=["DELETE"])
def delete_role_by_id(role_id):
    data = delete_by_id(role_id)
    return ResponseModel(1,"Role Deleted",data.to_json()).to_json_response(200)
    
