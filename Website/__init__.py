#__init__.py makes any directory a python package
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'demo'

    from .views import views #importing Blueprints
    from .auth import auth

    app.register_blueprint(views, urlprefix= '/')  # register Blueprints
    app.register_blueprint(auth, urlprefix= '/') #the prefix is before we can access stuff inside. No prefix yet

    return app

