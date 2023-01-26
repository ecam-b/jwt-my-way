from flask import Blueprint, jsonify, request, make_response
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import jwt
from datetime import datetime, timedelta
# Models
from models.UserModel import UserModel
# Database
from database.db import db
# Config
from config import SECRET_KEY
# Decoradores
from utils.token_required import token_required


user_bp = Blueprint("user", __name__)

@user_bp.route("/users", methods=["GET"])
@token_required
def get_all_users(current_user):
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


@user_bp.route("/login", methods=["POST"])
def login():
  auth = request.json

  if not auth or not auth["email"] or not auth["password"]:
    return make_response("No es posible realizar la verificación.", 401)
  
  user = UserModel.query.filter_by(email = auth["email"]).first()

  if not user:
    return make_response("Usuario no registrador.")

  if check_password_hash(user.password, auth["password"]):
    token = jwt.encode(
      {
        "public_id": user.public_id,
        "exp": datetime.utcnow() + timedelta(minutes=30)
      },
      SECRET_KEY,
      algorithm="HS256"
    )
    return make_response(jsonify({"token": token}), 201)

  return make_response("No es posible validar la información. Contraseña incorrecta.", 403)


@user_bp.route("/signup", methods=["POST"])
def signup():
  data = request.json
  public_id = str(uuid.uuid4())
  name = data["name"]
  email = data["email"]
  password = generate_password_hash(data["password"])

  user = UserModel.query.filter_by(email = email).first()

  if not user:
    user = UserModel(public_id, name, email, password)
    db.session.add(user)
    db.session.commit()

    return make_response("Usuario añadido", 201)
  else:
    return make_response("Usuario ya existente. Por favor ingrese.", 202)

  