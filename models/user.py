import uuid

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import String
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash

from app.app import db
from exceptions.erros import UserAlreadyExistsError


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    full_name = db.Column(String(70), index=True, nullable=False)
    email = db.Column(String(120), index=True, unique=True, nullable=False)
    password_hash = db.Column(String(128), unique=True, nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


def save_user(user):
    try:
        db.session.add(user)
        db.session.commit()
    except IntegrityError:
        raise UserAlreadyExistsError


def get_by_email(email):
    return User.query.filter_by(email=email).first()