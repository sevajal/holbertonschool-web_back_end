#!/usr/bin/env python3
""" 4. Force locale with URL parameter  """
from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Config class for Babel object """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def hello_world():
    """ Render a html file """
    return render_template('4-index.html')


@babel.localeselector
def get_locale():
    """ Determines the best match with the supported languages """
    if request.full_path.split('/')[1][:8] == "?locale=":
        lang = request.full_path.split('/')[1][8:]
        if lang in app.config['LANGUAGES']:
            return lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run()
