from flask import Blueprint, render_template, redirect, url_for
from website import api
auth = Blueprint("auth", __name__)

@auth.route("/login")
def login():
    return render_template( 
        "login.html",
    )
