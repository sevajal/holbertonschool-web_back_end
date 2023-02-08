#!/usr/bin/env python3
""" Module for basic authenticator """
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth


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
