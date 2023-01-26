from flask import request, jsonify
from functools import wraps
import jwt
# Config
from config import SECRET_KEY
# Models
from models.UserModel import UserModel

def token_required(func):
  @wraps(func)
  def decorated(*args, **kwargs):
    token = None

    if "token" in request.headers:
      token = request.headers["token"]

    if not token:
      return jsonify({"message": "Token faltante"}), 401

    try:
      print(jwt.decode(token, SECRET_KEY, algorithms=["HS256"]))
      data = jwt.decode(token, SECRET_KEY)
      current_user = UserModel.query.filter_by(public_id = data["public_id"]).first()
    except:
      return jsonify({"message": "Token invalido"}), 401
    return func(current_user, *args, **kwargs)
  return decorated