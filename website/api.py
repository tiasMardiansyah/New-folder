from flask import Blueprint, request, current_app
from sqlalchemy.sql import text
from website.database import db, create_session
from datetime import datetime

api = Blueprint("api", __name__)

def execute_query(query, params=None, fetch_all=True):
    with current_app.app_context():
        with db.engine.connect() as connection:
            if params:
                result = connection.execute(query, params)
            else:
                result = connection.execute(query)
            if fetch_all:
                rows = [dict(row) for row in result.mappings()]
                return rows
            return result

@api.route("/api/v1/list_pemancingan", methods=["GET"])
def list_pemancingan():

    keyword = request.args.get("keyword")

    # Query ke pemancingan
    query = "SELECT * FROM pemancingan where is_verified = 1 "

    if keyword:
        query += f" AND (lower(nama_pemancingan) LIKE  lower('%{keyword}%'))"
    
    endQuery = text(query)
    result = execute_query(endQuery)
    pemancingan = []

    # Looping data pemancingan
    for row in result:
        pemancingan.append({
            "id": row["id"],
            "nama": row["nama_pemancingan"],
            "description": row["detail_pemancingan"],
            "alamat": row["alamat_pemancingan"],
            "image_url": row["link_foto_pemancingan"],
            "biaya_tempat": row["biaya_tempat"],
            "biaya_olah": row["biaya_pengolahan"],
            "biaya_ikan": row["biaya_ikan_per_kilo"]
        })

    # Jika tidak ada data pemancingan
    if not pemancingan: 
        return {
            "success": False,
            "message": "pemancingan tidak ditemukan",
        }
    
    result = {
        "success": True,
        "data": pemancingan
    }

    return result

@api.route("/api/v1/detail_pemancingan/<int:id>", methods=["GET"])
def detail_pemancingan(id):
    query_pemancingan = text(f"""
        SELECT * FROM pemancingan WHERE id={id} and is_verified = 1 
    """)

    query_kolam = text(f"""
        SELECT id, nama, kapasitas FROM kolam WHERE id_pemancingan={id}
    """)

    query_jenis_ikan = text(f"""
        SELECT id, nama, jumlah FROM ikan WHERE id_pemancingan={id}
    """)

    result = execute_query(query_pemancingan)
    pemancingan = {}

    result_kolam = execute_query(query_kolam)
    kolam = []

    result_jenis_ikan = execute_query(query_jenis_ikan)
    jenis_ikan = []

    for row in result_kolam:
        kolam.append({
            "id" : row["id"],
            "nama": row["nama"],
            "kapasitas": row["kapasitas"]
        })

    for row in result_jenis_ikan:
        jenis_ikan.append({
            "id": row["id"],
            "nama": row["nama"],
            "jumlah": row["jumlah"]
        })

    for row in result:
        pemancingan = {
            "id": row["id"],
            "nama": row["nama_pemancingan"],
            "description": row["detail_pemancingan"],
            "alamat": row["alamat_pemancingan"],
            "image_url": row["link_foto_pemancingan"],
            "biaya_tempat": row["biaya_tempat"],
            "biaya_ikan": row["biaya_ikan_per_kilo"],
            "biaya_olah": row["biaya_pengolahan"],
            "link_map": row["link_map"],
            "kolam": kolam,
            "jenis_ikan": jenis_ikan,
        }

    if not pemancingan:
        return {
            "success": False,
            "message": "Detail pemancingan tidak ditemukan"
        }

    return pemancingan

@api.route("/api/v1/reservasi", methods=["POST"])
def submit_reservasi ():
    data = request.get_json()
    print(data)

    id_pemancingan = data["idPemancingan"]
    tanggal_mancing = data["tanggalMancing"]
    jam_mancing = data["jamMancing"]
    jumlah_orang_mancing = data["jumlahOrangMancing"]
    berat_dipancing = data["beratDipancing"]
    kolam_dipilih = data["kolamDipilih"]
    biaya_keseluruhan = data["biayaKeseluruhan"]
    biaya_keseluruhan = data["biayaKeseluruhan"]
    is_diolah = data["isDiolah"]

    # Combine tanggal_mancing and jam_mancing to create a datetime object
    tanggal_jam_mancing = datetime.strptime(f"{tanggal_mancing} {jam_mancing}", "%Y-%m-%d %H:%M")

    latest_id_query = text("SELECT id FROM reservasi where Date(created_time) = CURDATE() order by created_time desc")

    query = text(f"""
        INSERT INTO 
            reservasi (
                id,
                id_pemancingan, 
                id_user, 
                id_kolam,
                tanggal_reserv, 
                jumlah_orang, 
                berat_ikan_dipancing, 
                is_diolah, 
                status_terakhir, 
                total_bayar,
                created_by
            ) 
        VALUES (
            :id,
            :id_pemancingan,
            :id_user,
            :id_kolam,
            :tanggal_reserv,
            :jumlah_orang,
            :berat_ikan_dipancing,
            :is_diolah,
            :status_terakhir,
            :total_bayar,
            :created_by
        )
    """)

    histori_query = text(f"""
        INSERT INTO 
            histori_reservasi (
                id_reservasi, 
                status
            )
        VALUES (
            :new_reservasi_id,
            'Dibuat'
        )
    """)

    session = create_session()
    try:
        with session.begin():
            result = execute_query(latest_id_query)

            new_reservasi_id = 'R0000000000000'
            if (result != []):
                new_reservasi_id = result[0]['id']

            new_reservasi_id = int(new_reservasi_id[9:]) +  1

            # Generate id berdasarkan tahun, bulan, dan hari saat ini
            current_date = datetime.now()
            formatted_id = f"R{current_date.year}{current_date.month:02d}{current_date.day:02d}{new_reservasi_id:05d}"

            # Insert the new reservation with the formatted ID
            session.execute(query, {
                'id': formatted_id,
                'id_pemancingan': id_pemancingan,
                'id_user': 1,  # Replace with actual user ID
                'id_kolam': kolam_dipilih,
                'tanggal_reserv': tanggal_jam_mancing,
                'jumlah_orang': jumlah_orang_mancing,
                'status_terakhir': 'Dibuat',
                'berat_ikan_dipancing': berat_dipancing,
                'is_diolah': is_diolah,
                'total_bayar': biaya_keseluruhan,
                'created_by': 1  # Replace with actual user ID
            })

            # Insert into histori_reservasi with the new formatted ID
            session.execute(histori_query, {
                'new_reservasi_id': formatted_id
            })

        return {
            "success": True,
            "data" : {
                "id_reservasi": formatted_id
            },
            "message": "Reservasi berhasil"
        }
    except Exception as e:
        print(str(e))
        return {
            "success": False,
            "message": str(e)
        }
    finally:
        session.close()

    
def get_histori_reservasi():

    
    query = text("SELECT * FROM histori_reservasi where id_user = :id_user")

    result = execute_query(query, {'id_user': 1})
    histori_reservasi = []

    for row in result:

        tanggal = row["tanggal_reserv"]
        tanggal_reserv = tanggal.strftime("%Y-%m-%d")
        jam_reserv = tanggal.strftime("%H:%M")

        
        histori_reservasi.append({
            "id_reservasi": row["id_reservasi"],

            "status": row["status"]
        })
    return result