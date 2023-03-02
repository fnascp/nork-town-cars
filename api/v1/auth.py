from flask import Blueprint
from flask import jsonify
from flask import request

from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

from dtos.auth_dtos import (
    LoginRequestDTO, RegisterRequestDTO, RegisterResponseDTO)
from exceptions.erros import UserAlreadyExistsError
from services.auth_service import autenticate_user, create_user

auth_bp = Blueprint('auth', __name__)


@auth_bp.route("/register", methods=["POST"])
def register():
    request_data = RegisterRequestDTO.from_dict(request.json)
    try:
        user = create_user(request_data)
        response = RegisterResponseDTO(user.id, user.email, user.full_name)
        return jsonify(response)
    except UserAlreadyExistsError: 
        return jsonify({"msg": "User already exists"}), 400


@auth_bp.route("/login", methods=["POST"])
def login():
    request_data = LoginRequestDTO.from_dict(request.json)
    token = autenticate_user(request_data)
    if token is None:
        return jsonify({"msg": "Bad username or password"}), 401
    return jsonify(access_token=token)


@auth_bp.route("/me", methods=["GET"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
