from flask import Flask

from api.v1.auth import auth_bp
from api.v1.home import home_bp
from flask_jwt_extended import JWTManager
import sqlalchemy


jwt = JWTManager()
db = sqlalchemy.create_engine('postgresql+psycopg2://app_user:app_password@localhost:5432/app')

def create_app() -> Flask:
    app = Flask(__name__)

    app.config["JWT_SECRET_KEY"] = "super-secret" 
    jwt.init_app(app)
    app.register_blueprint(auth_bp)
    app.register_blueprint(home_bp)

    return app






