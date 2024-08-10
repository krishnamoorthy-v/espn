from dao.user import Users,Roles
from dto.myexception import myException
import base64
from werkzeug.security import check_password_hash,generate_password_hash
from mongoengine.queryset.visitor import Q
from flask_jwt_extended import create_access_token,create_refresh_token,get_jwt_identity

# Get All Users
def get_all_users():
    data = Users.objects()
    if not data:
        raise myException('No users available !',400)
    return data

    
# Create New User
def create_user(body):
    body['roleId']=Roles.objects(id=body['roleId']).first()
    if not body['roleId']:
        raise myException('Invalid Role !',400);
    body['password'] = generate_password_hash(body['password'])
    data = Users(**body)
    data.validate()
    data.save()
    return data   


#User_Image_Encode
def user_image_encode(file,id):
    user = Users.objects(id = id).first()
    img_content = file.read()
    encoded_image = base64.b64encode(img_content).decode("utf-8")
    user['profileImg'] = encoded_image
    user.save()
    return user



# Get User By ID
def get_user_id(id):
    user = Users.objects(id=id).first()
    if not user:
        raise myException ("User not found !",400);
    return user


# Update User By ID
def update_one_user(id,body):
    data = Users.objects(id=id).first()    
    if not data:
        raise myException('User not found !',400);
    body['password'] =generate_password_hash(body['password'])
    data.update(**body)
    return get_user_id(id)


#Delete User By ID
def delete_one_user(id):
    data = Users.objects(id=id).first()    
    if not data :
        raise myException ("User not found !",400)
    data.delete()
    return data 


#Create User With Role[USER] // SIGNUP
def  user_with_role(body):
    body['roleId']=Roles.objects(name='USER').first()
    if not body['roleId']:
        raise myException('Authorization error !',403)
    body['password'] = generate_password_hash(body['password'])
    data = Users(**body)
    data.validate()
    data.save()
    return data


# Login For User
def user_login(body):
    username = body['email_or_phone']
    password = body['password']
    user = Users.objects(Q(email = username) | Q(mobileNo = username)).first()    
    if user:
        valid = check_password_hash(user['password'],password)
        if valid:
            access_token = create_access_token(identity=username,fresh=True)
            refresh_token = create_refresh_token(identity=username)
            result = {
                'access_token':access_token,
                'refresh_token':refresh_token,
                'msg':'Login Successful' 
                }    
            return result
        else:
            return {'msg':'Incorrect Password'},404
    else:
        return {'msg':'User does not exist'},400
    
    
# Access Token Refresh
def token_refresh():
    user = get_jwt_identity()
    access_token = create_access_token(identity=user,fresh=False)
    result = {
            'msg':'Token Refreshed',
            'access_token': access_token,
            'user':user
        }    
    return result 

# Login For Admin
def login_for_admin(body):
    username = body['email_or_phone']
    password = body['password']
    user = Users.objects(Q(email = username) | Q(mobileNo = username)).first()
    if user:
        if user.roleId.name != "USER":
            
            valid = check_password_hash(user['password'],password)
            if valid:
                access_token = create_access_token(identity=username,fresh=True)
                refresh_token = create_refresh_token(identity=username)
                result = {
                    'access_token':access_token,
                    'refresh_token':refresh_token,
                    'msg':'Login Successful' 
                    }       
                return result
            else:
                raise myException("Incorrect Password", 400)
        raise myException("User does not have access", 400)
    raise myException("User does not exist", 400)

