#!/usr/bin/env python3
""" 20. End-to-end integration test """
import requests

URL = 'http://localhost:5000'


def register_user(email: str, password: str) -> None:
    """ Registers a user """
    data = {"email": email, "password": password}
    response = requests.post(f'{URL}/users', data=data)
    assert response.status_code == 200, "register_user fail"


def log_in_wrong_password(email: str, password: str) -> None:
    """ Log with wrong password """
    data = {"email": email, "password": password}
    response = requests.post(f'{URL}/sessions', data=data)
    assert response.status_code == 401, "log_in_wrong_password fail"


def log_in(email: str, password: str) -> str:
    """ Correct login """
    data = {"email": email, "password": password}
    response = requests.post(f'{URL}/sessions', data=data)
    assert response.status_code == 200, "log_in fail"
    session_id = response.cookies.get("session_id")
    return session_id


def profile_unlogged() -> None:
    """ Profile unlogged """
    data = {"session_id": None}
    response = requests.get(f'{URL}/profile', data=data)
    assert response.status_code == 403, "profile_unlogged fail"


def profile_logged(session_id: str) -> None:
    """ Profile logged """
    data = {"session_id": session_id}
    response = requests.get(f'{URL}/profile', cookies=data)
    assert response.status_code == 200, "profile_logged fail"


def log_out(session_id: str) -> None:
    """ Log out """
    data = {"session_id": session_id}
    response = requests.delete(f'{URL}/sessions', cookies=data)
    assert response.status_code == 200, "log_out fail"


def reset_password_token(email: str) -> str:
    """ Reset password token """
    data = {"email": email}
    response = requests.post(f'{URL}/reset_password', data=data)
    assert response.status_code == 200, "reset_password_token fail"
    return response.json().get("reset_token")


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """ update password """
    data = {
        "email": email,
        "reset_token": reset_token,
        "new_password": new_password
    }
    response = requests.put(f'{URL}/reset_password', data=data)
    assert response.status_code == 200, "update_password fail"


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"

if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
