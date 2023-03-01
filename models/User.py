import uuid
from sqlalchemy.dialects.postgresql import UUID
from app import db
from sqlalchemy import String


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    full_name = db.Column(String(70), index=True, nullable=False)
    email = db.Column(String(120), index=True, unique=True, nullable=False)
    password_hash = db.Column(String(128), unique=True, nullable=False)