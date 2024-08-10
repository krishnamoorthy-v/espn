import json

from flask import Flask, jsonify, url_for
import datetime
from flask_jwt_extended import JWTManager
from mongoengine.errors import ValidationError, NotUniqueError
from dto.myexception import myException
from controllers.roles_controller import roles_api
from controllers.users_controller import users_api
from controllers.team_controllers import team_api
from controllers.feeds_controller import feeds_api
from controllers.player_controller import player_api
from controllers.score_controller import score_api
from controllers.login_oauth_controller import login_oauth_api
from flask import Flask
from controllers.Matchcontrollers import match_api
from authlib.integrations.flask_client import OAuth
import requests

app = Flask(__name__)
app.register_blueprint(roles_api, url_prefix='/api/v1')
app.register_blueprint(users_api, url_prefix='/api/v1')
app.register_blueprint(team_api, url_prefix='/team')
app.register_blueprint(feeds_api, url_prefix='/api/v1')
app.register_blueprint(match_api, url_prefix='/match')
app.register_blueprint(player_api, url_prefix='/players')
app.register_blueprint(score_api, url_prefix="/scores")
app.register_blueprint(login_oauth_api, url_prefix="/oauth")

jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = 'Icanio'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = datetime.timedelta(days=30)
jwt.init_app(app)

app.secret_key = "Icanio.com"
oauth = OAuth(app)

GOOGLE_CLIENT_ID = "59874236544-534c262hc8ui3nnum7bv3grampij1t8r.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET = "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"
CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'


@app.route('/login')
def login():
    oauth.register(
        name='google',
        client_id=GOOGLE_CLIENT_ID,
        client_secret=GOOGLE_CLIENT_SECRET,
        server_metadata_url=CONF_URL,
        client_kwargs={
            'scope': 'openid email profile'
        }
    )
    
    # Redirect to google_auth function
    redirect_uri = url_for('google_auth', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)


@app.route('/oauth/redirect')
def google_auth():
    token = oauth.google.authorize_access_token()
    data1 = token['access_token']

    url = 'https://www.googleapis.com/oauth2/v3/userinfo?access_token=' + data1
    response = requests.get(url)
    user_info = json.loads(response.text)
    print(user_info)

    return user_info


@app.route('/')
def hello_world():  # put application's code here   
    return 'Hello World!'


@app.errorhandler(myException)
def handle_my_custom(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.errorhandler(ValidationError)
def handle_validation_error(error):
    if error.to_dict():
        response = jsonify(error.to_dict())
        response.status_code = 400
        return response
    else:
        response = jsonify({
            "message": error.message
        })
        return response


@app.errorhandler(NotUniqueError)
def handle_unique_error(error):
    response = jsonify({
        'message': 'The given Value already exist !',
        'error': str(error)
    })
    response.status_code = 400
    return response


if __name__ == '__main__':
    app.run()
