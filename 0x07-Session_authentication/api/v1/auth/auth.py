#!/usr/bin/env python3
""" Module for basic authenticator """
from flask import request
from typing import List, TypeVar
import os


class Auth():
    """ Class for basic authenticator """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Public method that requires auth"""
        if path is None or excluded_paths is None or excluded_paths is []:
            return True
        if path[-1] != "/":
            path = path + "/"
        if path not in excluded_paths:
            return True
        if path in excluded_paths:
            return False

    def authorization_header(self, request=None) -> str:
        """ Public method for authorization header """
        if request is None or request.headers.get("Authorization") is None:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """ Public method for current user """
        return None

    def session_cookie(self, request=None):
        """ Returns a cookie value from a request """
        if request is None:
            return None
        session_id = os.getenv("SESSION_NAME")
        return request.cookies.get(session_id)
