from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# Config
from config import SECRET_KEY, DATABASE_URI_CONNECTION
# Database
from database.db import db
# Routes
from routes.User import user_bp

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI_CONNECTION
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
SQLAlchemy(app)

db.init_app(app)
with app.app_context():
  db.create_all()


if __name__ == "__main__":

  # Blueprints
  app.register_blueprint(user_bp)

  app.run(debug=True)