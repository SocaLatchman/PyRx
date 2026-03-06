from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
ma = Marshmallow()

def init_db_ma(app):
    db.init_app(app)
    ma.init_app(app)