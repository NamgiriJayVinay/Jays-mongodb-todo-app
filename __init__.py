from flask import Flask 

from .main.app import main
from .extensions import mongo

def create_app():
    app=Flask(__name__)
    app.config['MONGO_URI']='mongodb+srv://jayvinay:jaymongo@cluster0.fzoac.mongodb.net/mydb?retryWrites=true&w=majority'
    mongo.init_app(app)

    app.register_blueprint(main)

    return app
