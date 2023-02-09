#!/usr/bin/env python3
""" Module for basic authenticator """
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
import base64
from models.user import User


class BasicAuth(Auth):
    """ Basic Auth """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Extract base64 authorization heade"""
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if authorization_header.split(" ")[0] != "Basic":
            return None
        return authorization_header.split(" ")[1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """ decode base64 authorization header """
        header = base64_authorization_header
        if header is None:
            return None
        if type(header) is not str:
            return None
        try:
            return base64.b64decode(header).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header:
                                 str) -> (str, str):
        """ Extract user credentials """
        header = decoded_base64_authorization_header
        if header is None:
            return None, None
        if type(header) is not str:
            return None, None
        if ":" not in header:
            return None, None
        return header.split(":", 1)

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """ User object from credentials """
        if user_email is None or type(user_email) is not str:
            return None
        if user_pwd is None or type(user_pwd) is not str:
            return None
        users = User.search({"email": user_email})
        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user """
        auth_header = self.authorization_header(request)
        base64 = self.extract_base64_authorization_header(auth_header)
        decode = self.decode_base64_authorization_header(base64)
        user_email, user_pwd = self.extract_user_credentials(decode)
        return self.user_object_from_credentials(user_email, user_pwd)
