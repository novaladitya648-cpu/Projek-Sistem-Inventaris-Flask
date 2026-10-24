from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = "inventaris-secret-key"

# Data barang
data_barang = [
    {
        "kode": "BRG-001",
        "nama": "Laptop ASUS ROG",
        "kategori": "Elektronik",
        "stok": 45,
        "satuan": "Unit",
        "lokasi": "Gudang A (Lantai 1)"
    },
    {
        "kode": "BRG-002",
        "nama": "Kemeja Flanel Pria",
        "kategori": "Pakaian",
        "stok": 120,
        "satuan": "Pcs",
        "lokasi": "Gudang B (Lantai 2)"
    },
    {
        "kode": "BRG-003",
        "nama": "Serum Wajah Glowing",
        "kategori": "Kosmetik",
        "stok": 85,
        "satuan": "Botol",
        "lokasi": "Gudang C (Khusus)"
    },
    {
        "kode": "BRG-004",
        "nama": 'Smart TV Samsung 43"',
        "kategori": "Elektronik",
        "stok": 15,
        "satuan": "Unit",
        "lokasi": "Gudang A (Lantai 1)"
    },
    {
        "kode": "BRG-005",
        "nama": "Celana Jeans Denim",
        "kategori": "Pakaian",
        "stok": 95,
        "satuan": "Pcs",
        "lokasi": "Gudang B (Lantai 2)"
    }
]

# Penyimpanan sementara transaksi barang masuk
transaksi_masuk = []
transaksi_keluar = []

# DASHBOARD
@app.route("/")
def home():
    # Menghitung jumlah jenis barang
    total_jenis_barang = len(data_barang)

    # Menghitung total seluruh stok barang
    total_stok = sum(
        barang["stok"] for barang in data_barang
    )

    # Kapasitas maksimum gudang
    kapasitas_maksimum = 1000

    # Menghitung persentase kapasitas gudang
    kapasitas_gudang = min(
        round((total_stok / kapasitas_maksimum) * 100),
        100
    )

    # Menghitung jumlah barang yang stoknya menipis
    batas_stok_minimum = 20

    # Daftar barang menipis dipakai bersama oleh kartu Stok Menipis
    # dan notifikasi lonceng agar angkanya selalu sama.
    daftar_stok_menipis = [
        barang for barang in data_barang
        if barang["stok"] < batas_stok_minimum
    ]
    stok_menipis = len(daftar_stok_menipis)

    # Menghitung total barang masuk bulan berjalan
    sekarang = datetime.now()

    total_barang_masuk = sum(
        transaksi["jumlah"]
        for transaksi in transaksi_masuk
        if transaksi["tanggal"].month == sekarang.month
        and transaksi["tanggal"].year == sekarang.year
    )

    # Grafik Barang Masuk dan Barang Keluar: periode tetap Agustus - Oktober 2026
    # Setiap tuple berisi (tahun, bulan, label). Bulan tanpa transaksi bernilai 0.
    periode_grafik = [
        (2026, 8, "Agustus"),
        (2026, 9, "September"),
        (2026, 10, "Oktober")
    ]

    label_bulan = [label for _, _, label in periode_grafik]
    data_masuk_bulanan = []
    data_keluar_bulanan = []

    for tahun, bulan, _ in periode_grafik:
        total_masuk = sum(
            transaksi["jumlah"]
            for transaksi in transaksi_masuk
            if transaksi["tanggal"].month == bulan
            and transaksi["tanggal"].year == tahun
        )

        total_keluar = sum(
            transaksi["jumlah"]
            for transaksi in transaksi_keluar
            if transaksi["tanggal"].month == bulan
            and transaksi["tanggal"].year == tahun
        )

        data_masuk_bulanan.append(total_masuk)
        data_keluar_bulanan.append(total_keluar)

    # Grafik Kategori Inventaris: jumlah JENIS barang per kategori
    # (bukan jumlah stok). Kategori dikelompokkan tanpa membedakan
    # huruf besar/kecil agar "Elektronik" dan "elektronik" tidak terpisah.
    kategori_hitung = {}
    for barang in data_barang:
        nama_kategori = barang["kategori"].strip()
        kunci = nama_kategori.casefold()

        if kunci not in kategori_hitung:
            kategori_hitung[kunci] = {"nama": nama_kategori, "jumlah": 0}

        kategori_hitung[kunci]["jumlah"] += 1

    label_kategori = [item["nama"] for item in kategori_hitung.values()]
    data_kategori = [item["jumlah"] for item in kategori_hitung.values()]

    # Pesan sistem: aktivitas transaksi terbaru yang benar-benar tercatat
    aktivitas = [
        {
            "jenis": "masuk",
            "nama": transaksi["nama"],
            "jumlah": transaksi["jumlah"],
            "tanggal": transaksi["tanggal"]
        }
        for transaksi in transaksi_masuk
    ] + [
        {
            "jenis": "keluar",
            "nama": transaksi["nama"],
            "jumlah": transaksi["jumlah"],
            "tanggal": transaksi["tanggal"]
        }
        for transaksi in transaksi_keluar
    ]
    aktivitas_terbaru = sorted(
        aktivitas,
        key=lambda item: item["tanggal"],
        reverse=True
    )[:5]

    return render_template(
        "index.html",
        total_jenis_barang=total_jenis_barang,
        total_barang_masuk=total_barang_masuk,
        kapasitas_gudang=kapasitas_gudang,
        total_stok=total_stok,
        kapasitas_maksimum=kapasitas_maksimum,
        stok_menipis=stok_menipis,
        batas_stok_minimum=batas_stok_minimum,
        label_bulan=label_bulan,
        data_masuk_bulanan=data_masuk_bulanan,
        data_keluar_bulanan=data_keluar_bulanan,
        label_kategori=label_kategori,
        data_kategori=data_kategori,
        daftar_stok_menipis=daftar_stok_menipis,
        aktivitas_terbaru=aktivitas_terbaru
    )

# DAFTAR BARANG
@app.route("/tables")
def tables():
    return render_template(
        "tables.html",
        data_barang=data_barang
    )

# TAMBAH BARANG
@app.route("/tambah-barang", methods=["GET", "POST"])
def tambah_barang():
    if request.method == "POST":
        kode = request.form.get("kode", "").strip()
        nama = request.form.get("nama", "").strip()
        kategori = request.form.get("kategori", "").strip()
        stok = request.form.get("stok", "").strip()
        satuan = request.form.get("satuan", "").strip()
        lokasi = request.form.get("lokasi", "").strip()

        if not all([kode, nama, kategori, stok, satuan, lokasi]):
            flash("Semua kolom wajib diisi.", "danger")
            return render_template("tambah_barang.html")

        if any(barang["kode"] == kode for barang in data_barang):
            flash("Kode barang sudah digunakan.", "danger")
            return render_template("tambah_barang.html")

        try:
            stok = int(stok)

            if stok < 0:
                raise ValueError

        except ValueError:
            flash("Stok harus berupa angka nol atau lebih.", "danger")
            return render_template("tambah_barang.html")

        barang_baru = {
            "kode": kode,
            "nama": nama,
            "kategori": kategori,
            "stok": stok,
            "satuan": satuan,
            "lokasi": lokasi
        }

        data_barang.append(barang_baru)

        flash("Barang berhasil ditambahkan.", "success")

        return redirect(url_for("tables"))

    return render_template("tambah_barang.html")


# EDIT BARANG
@app.route("/edit-barang/<kode>", methods=["GET", "POST"])
def edit_barang(kode):
    barang = next(
        (item for item in data_barang if item["kode"] == kode),
        None
    )

    if barang is None:
        flash("Barang tidak ditemukan!", "danger")
        return redirect(url_for("tables"))

    if request.method == "POST":
        nama = request.form.get("nama", "").strip()
        kategori = request.form.get("kategori", "").strip()
        stok = request.form.get("stok", "").strip()
        satuan = request.form.get("satuan", "").strip()
        lokasi = request.form.get("lokasi", "").strip()

        if not all([nama, kategori, stok, satuan, lokasi]):
            flash("Semua kolom wajib diisi!", "danger")
            return render_template(
                "edit_barang.html",
                barang=barang
            )

        try:
            stok = int(stok)

            if stok < 0:
                raise ValueError

        except ValueError:
            flash("Stok harus berupa angka nol atau lebih!", "danger")
            return render_template(
                "edit_barang.html",
                barang=barang
            )

        barang["nama"] = nama
        barang["kategori"] = kategori
        barang["stok"] = stok
        barang["satuan"] = satuan
        barang["lokasi"] = lokasi

        flash("Data barang berhasil diperbarui!", "success")

        return redirect(url_for("tables"))

    return render_template(
        "edit_barang.html",
        barang=barang
    )

# HAPUS BARANG
@app.route("/hapus-barang/<kode>", methods=["POST"])
def hapus_barang(kode):
    barang = next(
        (item for item in data_barang if item["kode"] == kode),
        None
    )

    if barang is None:
        flash("Barang tidak ditemukan!", "danger")
        return redirect(url_for("tables"))

    data_barang.remove(barang)

    flash("Data barang berhasil dihapus!", "success")

    return redirect(url_for("tables"))


# PROFIL
@app.route("/profil")
def profil():
    return render_template(
        "profil.html",
        profil={
            "nama": "Eliazar Noval Galih",
            "peran": "Administrator Gudang"
        },
        total_jenis_barang=len(data_barang),
        total_stok=sum(barang["stok"] for barang in data_barang)
    )

# LOGIN
@app.route("/login")
def login():
    return render_template("login.html")

# barang masuk
@app.route("/barang-masuk", methods=["GET", "POST"])
def barang_masuk():
    if request.method == "POST":
        kode = request.form.get("kode", "").strip()
        jumlah_input = request.form.get("jumlah", "").strip()

        barang = next(
            (item for item in data_barang if item["kode"] == kode),
            None
        )

        if barang is None:
            flash("Barang tidak ditemukan!", "danger")
            return redirect(url_for("barang_masuk"))

        try:
            jumlah = int(jumlah_input)

            if jumlah <= 0:
                raise ValueError

        except ValueError:
            flash(
                "Jumlah barang harus berupa angka lebih dari 0!",
                "danger"
            )
            return redirect(url_for("barang_masuk"))

        # Tambahkan stok barang
        barang["stok"] += jumlah

        # Simpan transaksi barang masuk
        transaksi_masuk.append({
            "kode": barang["kode"],
            "nama": barang["nama"],
            "jumlah": jumlah,
            "tanggal": datetime.now()
        })

        flash(
            f"Barang masuk berhasil dicatat! "
            f"Stok {barang['nama']} bertambah {jumlah} unit.",
            "success"
        )

        return redirect(url_for("barang_masuk"))

    # Menghitung total barang masuk bulan berjalan
    sekarang = datetime.now()

    total_barang_masuk = sum(
        transaksi["jumlah"]
        for transaksi in transaksi_masuk
        if transaksi["tanggal"].month == sekarang.month
        and transaksi["tanggal"].year == sekarang.year
    )

    return render_template(
        "barang_masuk.html",
        data_barang=data_barang,
        transaksi_masuk=transaksi_masuk,
        total_barang_masuk=total_barang_masuk,
        now_month=sekarang.month,
        now_year=sekarang.year
    )

# barang keluar
@app.route("/barang-keluar", methods=["GET", "POST"])
def barang_keluar():
    if request.method == "POST":
        kode = request.form.get("kode", "").strip()
        jumlah_input = request.form.get("jumlah", "").strip()
        keterangan = request.form.get("keterangan", "").strip()

        # Mencari barang berdasarkan kode
        barang = next(
            (item for item in data_barang if item["kode"] == kode),
            None
        )

        if barang is None:
            flash("Barang tidak ditemukan!", "danger")
            return redirect(url_for("barang_keluar"))

        # Memvalidasi jumlah barang keluar
        try:
            jumlah = int(jumlah_input)

            if jumlah <= 0:
                raise ValueError

        except ValueError:
            flash(
                "Jumlah barang keluar harus berupa angka lebih dari 0!",
                "danger"
            )
            return redirect(url_for("barang_keluar"))

        # Memastikan stok mencukupi
        if jumlah > barang["stok"]:
            flash(
                f"Stok {barang['nama']} tidak mencukupi! "
                f"Stok tersedia: {barang['stok']}.",
                "danger"
            )
            return redirect(url_for("barang_keluar"))

        # Mengurangi stok barang
        barang["stok"] -= jumlah

        # Menyimpan riwayat transaksi barang keluar
        transaksi_keluar.append({
            "kode": barang["kode"],
            "nama": barang["nama"],
            "jumlah": jumlah,
            "keterangan": keterangan,
            "tanggal": datetime.now()
        })

        flash(
            f"Barang keluar berhasil dicatat! "
            f"Stok {barang['nama']} berkurang {jumlah}.",
            "success"
        )

        return redirect(url_for("barang_keluar"))

    # Menghitung total barang keluar bulan berjalan
    sekarang = datetime.now()

    total_barang_keluar = sum(
        transaksi["jumlah"]
        for transaksi in transaksi_keluar
        if transaksi["tanggal"].month == sekarang.month
        and transaksi["tanggal"].year == sekarang.year
    )

    return render_template(
        "barang_keluar.html",
        data_barang=data_barang,
        transaksi_keluar=transaksi_keluar,
        total_barang_keluar=total_barang_keluar,
        now_month=sekarang.month,
        now_year=sekarang.year
    )

if __name__ == "__main__":
    app.run(debug=True)