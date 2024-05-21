import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models import ItemModel
from schemas import ItemSchema, ItemUpdateSchema
from sqlalchemy.exc import SQLAlchemyError
from db import db

blp = Blueprint("items",__name__,description="Operations on items")

@blp.route("/item/<string:item_id>")
class Item(MethodView):
    @blp.response(200,ItemSchema)
    def get(self,item_id):
        item = ItemModel.query.get_or_404(item_id) # this query comes in Flask SQLAchemy not in Vanilla SQLAlchemy # retrieves the item by primary key if there is no item present it will automatically abort 
        return item
        
    def delete(self,item_id):
        item = ItemModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Item Deleted."}

    @blp.arguments(ItemUpdateSchema)
    @blp.response(200,ItemSchema)
    def put(self, item_data, item_id):
        item = ItemModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = ItemModel(id = item_id,**item_data)
        db.session.add(item)
        db.session.commit()

@blp.route("/item")
class ItemList(MethodView):
    @blp.response(200,ItemSchema(many=True))
    def get(self):
        return ItemModel.query.all()  # this will return the list of items not the object o fthe items because we put in the marshmellow ItemSchema(many =True)

    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self,item_data):  # the 2nd paramter conatins the json/dict which is the validated fields that the Schema requested. 
        item = ItemModel(**item_data)  # **item_data is turning dict to key word args
        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occured while insering the item.")
        return item