from flask import Blueprint
from flask import jsonify
from flask import request

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

from dtos.auth_dtos import (
    LoginRequestDTO, RegisterRequestDTO, RegisterResponseDTO)
from models.user import User, save_user

auth_bp = Blueprint('auth', __name__)


@auth_bp.route("/register", methods=["POST"])
def register():
    request_data = RegisterRequestDTO.from_dict(request.json)
    u = User(full_name=request_data.full_name, email=request_data.email)
    u.set_password(request_data.password)
    save_user(u)

    response = RegisterResponseDTO(
        "algum id", request_data.email, request_data.full_name)
    return jsonify(response)


@auth_bp.route("/login", methods=["POST"])
def login():
    request_data = LoginRequestDTO.from_dict(request.json)

    if request_data.email != "test" or request_data.password != "test":
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=request_data.email)
    return jsonify(access_token=access_token)


@auth_bp.route("/me", methods=["GET"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
