from flask import Blueprint
from flask import jsonify
from flask import request

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

from dtos.auth_dtos import LoginRequestDTO


auth_bp = Blueprint('auth', __name__)

# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@auth_bp.route("/login", methods=["POST"])
def login():
    request_data = LoginRequestDTO.from_dict(request.json)

    if request_data.email != "test" or request_data.password != "test":
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=request_data.email)
    return jsonify(access_token=access_token)


# Protect a route with jwt_required, which will kick out requests
# without a valid JWT present.
@auth_bp.route("/me", methods=["GET"])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
