#!/usr/bin/env python3
""" 5. Mock logging in """
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from typing import Union

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Config class for Babel object """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.before_request
def before_request(login_as: int = None):
    """ Determines if a user is logged in """
    user: dict = get_user()
    g.user = user


def get_user() -> Union[dict, None]:
    """ Gets a user dictionary or None """
    login_user = request.args.get('login_as', None)
    if login_user is None:
        return None
    user: dict = {}
    user[login_user] = users.get(int(login_user))
    return user[login_user]


@app.route('/')
def hello_world():
    """ Render a html file """
    return render_template('5-index.html')


@babel.localeselector
def get_locale():
    """ Determines the best match with the supported languages """
    lang = request.args.get('locale')
    if lang in app.config['LANGUAGES']:
        return lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run()
