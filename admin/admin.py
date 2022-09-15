import asyncpg
from flask_jwt_extended import jwt_required
from flask import Blueprint, request, redirect, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, set_access_cookies, set_refresh_cookies, unset_jwt_cookies, verify_jwt_in_request

admin_bp = Blueprint('admin', __name__)


@admin_bp.route("/logout", methods=["GET"])
@jwt_required()
def logout_endpoint():
    response = jsonify()
    unset_jwt_cookies(response)
    return response, 200