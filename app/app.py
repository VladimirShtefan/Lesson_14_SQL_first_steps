import os

import dotenv
from flask import Flask

from app.blueprints.genre_blueprint.views import genre_blueprint
from app.blueprints.movie_blueprint.views import title_blueprint
from app.blueprints.rating_blueprint.views import rating_blueprint
from app.paths import DEV_CONFIG_FILE_PATH, PROD_CONFIG_FILE_PATH


app = Flask(__name__)
app.register_blueprint(title_blueprint)
app.register_blueprint(rating_blueprint)
app.register_blueprint(genre_blueprint)

dotenv.load_dotenv(override=True)

if os.environ.get('FLASK_ENV') == 'development':
    app.config.from_pyfile(DEV_CONFIG_FILE_PATH)
    app.config['SECRET_KEY'] = 'super-secret-key'
else:
    app.config.from_pyfile(PROD_CONFIG_FILE_PATH)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
