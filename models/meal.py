from database import db
from flask_login import UserMixin

class Meal(db.Model, UserMixin):
    # id (int), name (text), description (text), date/time(text), in or out diet indicator (text)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    time = db.Column(db.String(80), nullable=False)
    indicator = db.Column(db.String(80), nullable=False)