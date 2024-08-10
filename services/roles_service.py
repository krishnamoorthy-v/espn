from dao.roles import Roles
from dto.myexception import myException

#Get All Roles
def get_all_roles():
    data = Roles.objects()
    if not data:
        raise myException("No roles available",400 );
    return data

#Create New Role
def create_role(body):
    role_name = body['name']
    if not role_name:
        raise myException("Please provide details",400);
    if role_name:
        user = Roles.objects(name = role_name).first()
        if not user:
            data = Roles(**body)
            data.save() 
            return data
        raise myException('Role already exist',400)

#Get Role By ID
def get_by_id(id):
    data = Roles.objects(id=id)
    if not data :
        raise myException ('Requested role not found',400)
    return data

#Update Role By ID
def update_by_id(id,body):
    data = Roles.objects(id=id)
    role_name = body['name']
    if not data:
        raise myException('Requested role not found',400)
    if data:
        user = Roles.objects(name = role_name).first()
        if not user:
            data.update(**body)
            return get_by_id(id)
        raise myException('Role already exist',400)

#Delete Role By ID
def delete_by_id(id):
    data = Roles.objects(id=id).first()
    if not data:
        raise myException('Requested role not found',400) 
    data.delete()
    return data 


