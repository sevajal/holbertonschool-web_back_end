#!/usr/bin/env python3
""" Module of Session_auth views
"""
from api.v1.views import app_views
from flask import jsonify, request, abort
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ login a user """
    data = request.form
    if not data.get('email'):
        return jsonify({"error": "email missing"}), 400
    if not data.get('password'):
        return jsonify({"error": "password missing"}), 400
    user = User.search({'email': data.get('email')})
    if not user:
        return jsonify({"error": "no user found for this email"}), 404
    if not user[0].is_valid_password(data.get('password')):
        return jsonify({"error": "wrong password"}), 401
    from api.v1.app import auth
    session_id = auth.create_session(user[0].id)
    response = jsonify(user[0].to_json())
    response.set_cookie(os.getenv('SESSION_NAME'), session_id)
    return response


@app_views.route('auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def delete():
    """ Deletes session - Logout """
    from api.v1.app import auth
    if auth.destroy_session(request) is False:
        abort(404)
    return jsonify({}), 200
