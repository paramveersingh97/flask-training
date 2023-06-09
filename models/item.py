from enum import unique
from db import db

class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(80), unique= True, nullable=False)
    price = db.Column(db.Float(precision=2),unique= False, nullable=False)
    store_id = db.column(db.String, unique=False, nullable = False)