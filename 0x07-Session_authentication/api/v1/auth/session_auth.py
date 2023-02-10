#!/usr/bin/env python3
""" Module for basic authenticator """
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
import base64
from models.user import User


class SessionAuth(Auth):
    """ Session Auth Class"""
    pass
