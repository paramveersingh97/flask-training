from sqlite3 import IntegrityError
import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import StoreSchema
from models import StoreModel
from db import db
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

blp = Blueprint("stores",__name__,description="Operations on stores")

#now  create a class whose methods routes to a specific endpoint
@blp.route("/store/<string:store_id>")
class Store(MethodView):
    @blp.response(200, StoreSchema)
    def get(self, store_id):
        store = StoreModel.query.get_or_404(store_id) # this query comes in Flask SQLAchemy not in Vanilla SQLAlchemy # retrieves the item by primary key if there is no item present it will automatically abort 
        return store
    
    def delete(self,store_id):
        store = StoreModel.query.get_or_404(store_id)
        db.session.delete(store)
        db.session.commit()
        return {"message": "Srore Deleted."}

@blp.route("/store")
class StoreList(MethodView):
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        return StoreModel.query.all()

    @blp.arguments(StoreSchema) 
    @blp.response(200, StoreSchema)   
    def post(self, store_data):
        store = StoreModel(**store_data)  # **item_data is turning dict to key word args
        try:
            db.session.add(store)
            db.session.commit()
        except IntegrityError:
            abort(400, message=" A store with the same name already exist. ")
        except SQLAlchemyError:
            abort(500, message="An error occured while insering the item.")
        return store
