from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from utils.timer import Timer
from config import *

db = SQLAlchemy()
timer = Timer()


def create_app():

    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    db.init_app(app)

    # create tables
    from models import User, Clock, Sleep
    db.create_all(app=app)

    from .main import main_bp
    app.register_blueprint(main_bp)

    from .apiv1 import apiv1_bp
    app.register_blueprint(apiv1_bp, url_prefix='/api')

    timer.start()

    return app
