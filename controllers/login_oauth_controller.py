from flask import Blueprint, request, session
import google_auth_oauthlib

from dto.response_model import ResponseModel
import requests
import json

login_oauth_api = Blueprint("login_oauth", __name__)

client_config = {"web":
                     {"client_id": "59874236544-534c262hc8ui3nnum7bv3grampij1t8r.apps.googleusercontent.com",
                      "project_id": "my-first-step-361006",
                      "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                      "token_uri": "https://oauth2.googleapis.com/token",
                      "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                      "client_secret": "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",
                      "redirect_uris": ["http://127.0.0.1:5000/oauth/redirect_url"]
                      }
                 }


@login_oauth_api.route("/login", methods=["GET"])
def login():
    flow = google_auth_oauthlib.flow.Flow.from_client_config(client_config, scopes=["openid email profile"],
                                                             redirect_uri="http://127.0.0.1:5000/oauth/redirect_url")
    auth_url, state = flow.authorization_url(access_type='offline')
    session["state"] = state
    return auth_url


@login_oauth_api.route("/redirect_url", methods=["GET"])
def redirect_url():
    if request.args.get('state') != session.get('state'):
        return ResponseModel(1, 'Invalid state parameter', '').to_json_response(400)
    code = request.args.get("code")
    access_token_info = get_access_token(code)
    data = get_data_from_google_api(access_token_info)
    return data


def get_data_from_google_api(info):
    response_data = requests.get(
        url="https://www.googleapis.com/oauth2/v3/userinfo?access_token=" + info["access_token"])
    return json.loads(response_data.content)


def get_access_token(code):
    form_data = {
        "grant_type": "authorization_code",
        "redirect_uri": "http://127.0.0.1:5000/oauth/redirect_url",
        "client_secret": "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",
        "client_id": "59874236544-534c262hc8ui3nnum7bv3grampij1t8r.apps.googleusercontent.com",
        "code": code
    }
    response_access_token = requests.post(url="https://oauth2.googleapis.com/token", data=form_data)
    access_token_info = json.loads(response_access_token.content)
    return access_token_info



