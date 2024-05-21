from db import db

class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String, unique=True, nullable= False)
    items = db.relationship("ItemModel", back_populates="store", lazy="dynamic", cascade = "all, delete")  #lazy=dynamic means that the items here are not going to be fetched from the database until we tell it to.
    tags = db.relationship("TagModel", back_populates= "store", lazy="dynamic")
