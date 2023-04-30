from flask import Flask
from flask_smorest import Api
from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint

app = Flask(__name__)


#Register blueprints in the api (resources)
 

    #configurations options (flask configurations)
app.config["PROPAGATE_ECXCEPTIONS"] = True  # if there is any exception that occurs hidden inside the extension of flask to propagate into the main app so that we can see it
# flsk smorest congigs that will show on the docs
app.config["API_TITLE"] = "Stores REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3" # openapi is the standard for the api documentation 
app.config["OPENAPI_URL_PREFIX"] = "/" # tells flask-smorest where the root of the API is.
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"  # loads the code from here to display the documentation


api = Api(app) # this basically connect flask-smorest extension to the flask app
api.register_blueprint(ItemBlueprint)
api.register_blueprint(StoreBlueprint)