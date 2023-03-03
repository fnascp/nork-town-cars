from flask import Blueprint
from flask import jsonify
from flask import request

from flask_jwt_extended import jwt_required

from dtos.owners_dtos import NewOwnerRequestDTO
from exceptions.erros import UserAlreadyExistsError
from services.owner_service import add_owner


owner_bp = Blueprint('owner', __name__, url_prefix='/owners')


@owner_bp.route("/add", methods=["POST"])
@jwt_required()
def add_new_owner():
    request_data = NewOwnerRequestDTO.from_dict(request.json)
    try:
        added_owner = add_owner(request_data)
        return jsonify(added_owner), 201
    except UserAlreadyExistsError: 
        return jsonify({"msg": "Owner already exists"}), 400