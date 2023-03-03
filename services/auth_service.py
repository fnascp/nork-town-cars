from flask_jwt_extended import create_access_token

from dtos.auth_dtos import (
    LoginRequestDTO, RegisterRequestDTO, RegisterResponseDTO)
from models.user import User, save_user, get_by_email


def create_user(user_data: RegisterRequestDTO) -> RegisterResponseDTO:
    u = User(full_name=user_data.full_name, email=user_data.email)
    u.set_password(user_data.password)
    save_user(u)
    return RegisterResponseDTO(u.id, u.email, u.full_name)


def autenticate_user(login_data: LoginRequestDTO) -> str | None:
    user = get_by_email(login_data.email)
    if user is None or user.check_password(login_data.password) == False:
        return None
    return create_access_token(identity=user.email)
