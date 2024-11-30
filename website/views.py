from flask import Blueprint, render_template
import api

views = Blueprint("views", __name__)


@views.route("/pemancingan")
def list_pemancingan():

    api.list_pemancingan()

    
    # Query ke pemancingan
    return render_template( 
        "list_pemancingan.html",  
        active_page="pemancingan",
        informasi_pemancingan = api.list_pemancingan()
    )

@views.route("/pemancingan/<int:id>")
def detail_pemancingan(id):

    detail_pemancingan = {}
    if id == 1:
        detail_pemancingan = {
            "id": 1,
            "nama": "Pemancingan Tulun Tiga Sumedang",
            "alamat": "Lorem ipsum dolor sit amet, sollicitudin est, ut vehicula",
            "image_url": "pemancingan_1.jpg",
            "harga": "Rp. 30.000",
            "biaya_olah": "Rp. 5.000",
            "deskripsi": "Cras dapibus, lorem ac feugiat facilisis, sem eros sollicitudin est, ut vehicula tortor orci volutpat orci. Sed vitae odio ac odio consectetur lacinia eu ut nunc.",
            "kolam": [
                "Kolam Kecil",
                "Kolam Besar"
            ],
            "Jenis Ikan": [
                "Ikan Mas",
                "Ikan Nila"
            ],
            "link_map": "https://maps.app.goo.gl/JU3KL4Zkq22rx4Ea9"
        }
    elif id == 2:
        detail_pemancingan = {
            "id": 2,
            "nama": "Pemancingan Ikan Mujaer",
            "alamat": "Jl. Raya Sumedang, No. 1, Sumedang",
            "harga": "Rp. 30.000",
            "biaya_olah": "Rp. 5.000",
            "deskripsi": "Pemancingan ikan mujaer yang terletak di Sumedang, menyediakan fasilitas pancing dan makanan ikan mujaer.",
            "kolam": [
                "Kolam Kecil",
                "Kolam Besar"
            ],
            "Jenis Ikan": [
                "Ikan Mujaer",
                "Ikan Nila"
            ]
        }
    elif id == 3:
        detail_pemancingan = {
            "id": 3,
            "nama": "Pemancingan Ikan Tias",
            "alamat": "Jl. Raya Sumedang, No. 1, Sumedang",
            "harga": "Rp. 30.000",
            "biaya_olah": "Rp. 5.000",
            "deskripsi": "Pemancingan ikan tias yang terletak di Sumedang, menyediakan fasilitas pancing dan makanan ikan tias.",
            "kolam": [
                "Kolam Kecil",
                "Kolam Besar"
            ],
            "Jenis Ikan": [
                "Ikan Tias",
                "Ikan Nila"
            ]
        }
    elif id == 4:
        detail_pemancingan = {
            "id": 4,
            "nama": "Pemancingan Ikan Tawes",
            "alamat": "Jl. Raya Situraja, No. 1, Situraja",
            "harga": "Rp. 30.000",
            "biaya_olah": "Rp. 5.000",
            "deskripsi": "Pemancingan ikan tawes yang terletak di Situraja, menyediakan fasilitas pancing dan makanan ikan tawes.",
            "kolam": [
                "Kolam Besar"
                "Kolam Kecil"
            ],
            "Jenis Ikan": [
                "Ikan Tawes",
                "Ikan Nila"
            ]
        }
    
    return render_template( 
        "detail_pemancingan.html",  
        active_page="pemancingan",
        informasi_pemancingan = detail_pemancingan
    )

@views.route("/pemancingan/<int:id>/reservasi")
def reservasi_pemancingan(id):
    return render_template( 
        "reservasi.html",  
        active_page="pemancingan",
        informasi_pemancingan = {
            "id": 1,
            "harga_masuk": 10000,
            "ikan_perkilo": 10000,
            "biaya_olah_perkilo": 3000,
            # "kolam": {
            #     1 : "Kolam Kecil",
            #     2 : "Kolam Besar"
            # }
        }
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

