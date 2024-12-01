from flask import Blueprint, render_template, jsonify
from website import api

views = Blueprint("views", __name__)


@views.route("/pemancingan")
def list_pemancingan():

    # Query ke pemancingan
    return render_template( 
        "list_pemancingan.html",  
        active_page="pemancingan",
        informasi_pemancingan = api.list_pemancingan()
    )

@views.route("/pemancingan/<int:id>")
def detail_pemancingan(id):

    # Query ke pemancingan
    return render_template( 
        "detail_pemancingan.html",  
        active_page="pemancingan",
        informasi_pemancingan = api.detail_pemancingan(id)
    ) 

@views.route("/pemancingan/<int:id>/reservasi")
def reservasi_pemancingan(id):
    return render_template( 
        "reservasi.html",  
        active_page="pemancingan",
        informasi_pemancingan = api.detail_pemancingan(id)
    )

@views.route("/histori_reservasi")
def reservasi():
    return render_template( 
        "histori_reservasi.html",  
        active_page="reservasi"
    )                                       

@views.route("/profile")
def profile():
    return render_template( 
        "profile.html",  
        active_page="profile"
    )

