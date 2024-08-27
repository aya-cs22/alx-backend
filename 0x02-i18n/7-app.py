from flask import Flask, render_template, request, g
from flask_babelex import Babel
import pytz
from pytz.exceptions import UnknownTimeZoneError

app = Flask(__name__)

class Config:
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """get user"""
    user_id = request.args.get('login_as')
    if user_id and user_id.isdigit():
        user_id = int(user_id)
        return users.get(user_id)
    return None


@app.before_request
def before_request():
    g.user = get_user()

@babel.localeselector
def get_locale():
    """get_locale"""
    local = request.args.get('locale')
    if local in app.config['LANGUAGES']:
        return local
    
    if g.user and g.user.get('locale'):
        return g.user['locale']

    
    local = babel_get_locale()
    if local:
        return str(local)
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@babel.timezoneselector
def get_timezone():
    """timezone"""
    timezone = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except UnknownTimeZoneError:
            pass

    if g.user and g.user.get('timezone'):
        return g.user['timezone']

    return 'UTC'

@app.route('/')
def index():
    """html"""
    return render_template('6-index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

