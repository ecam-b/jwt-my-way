from database.db import db

class UserModel(db.Model):
  __tablename__ = "user"

  id = db.Column(db.Integer, primary_key=True)
  public_id = db.Column(db.String(50), unique=True)
  name = db.Column(db.String(100))
  email = db.Column(db.String(70), unique=True)
  password = db.Column(db.String(500))


  def __init__(self, public_id, name, email, password):
    self.public_id = public_id
    self.name = name
    self.email = email
    self.password = password