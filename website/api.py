from flask import Blueprint, jsonify, request
import database

views = Blueprint("views", __name__)

def execute_query(query):
    result = database.engine.execute(query)
    return result

@views.route("api/v1/list_pemancingan", methods=["GET"])
def list_pemancingan():

    keyword = request.args.get("keyword")

    # Query ke pemancingan
    query = """
    SELECT * FROM pemancingan where 1=1
    """

    if keyword:
        query += f" AND (lower(nama_pemancingan) LIKE '%{keyword}%'"
    
    result = execute_query(query)
    pemancingan = []

    # Looping data pemancingan
    for row in result:
        pemancingan.append({
            "id": row["id"],
            "nama": row["nama_pemancingan"],
            "description": row["description"],
            "alamat": row["alamat"],
            "image_url": row["image_url"],
            "harga": row["harga"],
            "biaya_olah": row["biaya_olah"]
        })

    # Jika tidak ada data pemancingan
    if not pemancingan: 
        return jsonify({"message": "Data pemancingan tidak ditemukan"})

    return jsonify(pemancingan)

@views.route("api/v1/detail_pemancingan/<int:id>", methods=["GET"])
def detail_pemancingan(id):
    
    query_pemancingan = f"""
        SELECT * FROM pemancingan WHERE id={id}
    """

    query_kolam = f"""
        SELECT nama FROM kolam WHERE pemancingan_id={id}
    """

    query_jenis_ikan = f"""
        SELECT nama FROM jenis_ikan WHERE pemancingan_id={id}
    """

    result = execute_query(query_pemancingan)
    pemancingan = {}

    result_kolam = execute_query(query_kolam)
    kolam = [row["nama"] for row in result_kolam]

    result_jenis_ikan = execute_query(query_jenis_ikan)
    jenis_ikan = [row["nama"] for row in result_jenis_ikan]

    for row in result:
        pemancingan = {
            "id": row["id"],
            "nama": row["nama_pemancingan"],
            "deskripsi": row["description"],
            "alamat": row["alamat"],
            "image_url": row["image_url"],
            "harga": row["harga"],
            "biaya_olah": row["biaya_olah"],
            "kolam": kolam,
            "jenis_ikan": jenis_ikan,
            "link_map": row["link_map"]
        }

    if not pemancingan:
        return jsonify({"message": "Detail pemancingan tidak ditemukan"})

    return jsonify(pemancingan)