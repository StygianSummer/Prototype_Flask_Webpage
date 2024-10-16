from flask import Blueprint
#Login in auth, rest in views.
auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<p>Login page</p>"

@auth.route('/logout')
def logout():
    return "<p>Logout page</p>"

@auth.route('/register')
def register():
    return "<p>Register page</p>"