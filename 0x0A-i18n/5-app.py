#!/usr/bin/env python3
""" 5. Mock logging in """
from flask import Flask, render_template, request, g
from flask_babel import Babel, _

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
def before_request():
    """ Determines if a user is logged in """
    user_id = request.args.get('login_as')
    dict_user = get_user(user_id)
    if dict_user:
        g.user = dict_user


def get_user(user_id):
    """ Gets a user dictionary or None """
    if user_id and int(user_id) in users:
        return users[int(user_id)]
    return None


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world():
    """ Render a html file """
    login = False
    if g.get('user') is not None:
        login = True
    return render_template('5-index.html', login=login)


@babel.localeselector
def get_locale() -> str:
    """ Determines the best match with the supported languages """
    lang = request.args.get('locale')
    if lang in app.config['LANGUAGES']:
        return lang
    if (g.get('user') and g.user.get("locale", None)
            and g.user["locale"] in app.config['LANGUAGES']):
        return g.user["locale"]
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
