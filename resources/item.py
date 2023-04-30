import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import items,stores

from schemas import ItemSchema, ItemUpdateSchema

blp = Blueprint("items",__name__,description="Operations on items")

@blp.route("/item/<string:item_id>")
class Item(MethodView):
    @blp.response(200,ItemSchema)
    def get(self,item_id):
        try:
            print(items)
            return items[item_id]
        except KeyError:
            abort(404, message="Item not found")
    def delete(self,item_id):
        try:
            del items[item_id]
            return {"message": "Item deleted"}
        except KeyError:
            abort(404, message="Item not found.")
    @blp.arguments(ItemUpdateSchema)
    @blp.response(200,ItemSchema)
    def put(self, item_data, item_id):
        item_data = request.get_json()      
        try:
            item = items[item_id]
            # item |= item_data # this does an inplace modification (in higher version pf python)
            item ={**item,**item_data} #This is unpacking both dictionaries into a new one, resulting in a union.
            return item
        except KeyError:
            abort(404, message="Item not found.")

@blp.route("/item")
class ItemList(MethodView):
    @blp.response(200,ItemSchema(many=True))
    def get(self):
        print(items)
        return items.values()  # this will return the list of items not the onject o fthe items because we put in the marshmellow ItemSchema(many =True)

    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self,item_data):  # the 2nd paramter conatins the json/dict which is the validated fields that the Schema requested. 
        for item in items.values():
            if (item_data["name"] == item["name"] and item_data["store_id"] == item["store_id"]):
                abort(400, message="Item already exist.")

        if item_data["store_id"] not in stores:
            abort(404, message="Store not found")

        item_id = uuid.uuid4().hex
        item = {**item_data, "id": item_id }
        items[item_id] = item
        return item