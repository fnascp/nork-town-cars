from flask import Flask

from api.v1.auth import auth_bp
from api.v1.home import home_bp
from api.v1.owner import owner_bp

from .app import jwt, db, migrate


DATABASE_URI = 'postgresql+psycopg2://app_user:app_password@localhost:5432/app'

def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    db.init_app(app)
    migrate.init_app(app, db)

    app.config["JWT_SECRET_KEY"] = "super-secret" 
    jwt.init_app(app)
    app.register_blueprint(auth_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(owner_bp)

    return app

from models import user, owner, car