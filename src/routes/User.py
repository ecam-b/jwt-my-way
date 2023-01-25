from flask import Blueprint, jsonify
# Models
from models.UserModel import UserModel


user_bp = Blueprint("user", __name__)

@user_bp.route("/users", methods=["GET"])
def get_all_users():
  users = UserModel.query.all()
  list = []

  for user in users:
    list.append({
      "public_id": user.public_id,
      "name": user.name,
      "email": user.email,
      "password": user.password
    })

  return jsonify({"users": list})