from flask import Flask
from flask_smorest import Api
from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint
from resources.tag import blp as TagBlueprint
import os
from db import db
import models




#Register blueprints in the api (resources)
 
def create_app(db_url=None):
    app = Flask(__name__,instance_path=os.getcwd())
        #configurations options (flask configurations)
    app.config["PROPAGATE_ECXCEPTIONS"] = True  # if there is any exception that occurs hidden inside the extension of flask to propagate into the main app so that we can see it
    # flsk smorest congigs that will show on the docs
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3" # openapi is the standard for the api documentation 
    app.config["OPENAPI_URL_PREFIX"] = "/" # tells flask-smorest where the root of the API is.
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"  # loads the code from here to display the documentation
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    api = Api(app) # this basically connect flask-smorest extension to the flask app
    with app.app_context():
        db.create_all()
    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(StoreBlueprint)
    api.register_blueprint(TagBlueprint)

    return app