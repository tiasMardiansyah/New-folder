from flask import Blueprint

auth = Blueprint("auth", __name__)

@auth.route("/login")
def login():
    return "<p>Login YEAHHH</p>"

@auth.route("/logout")
def logout():
    return "<p>Logout YEAHHH</p>"

@auth.route("/sign-up")
def sign_up():
    return "<p>Sign Up YEAHHH</p>"