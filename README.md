📦 Sistem Inventaris Gudang Distribusi Barang
Sistem Inventaris Gudang Distribusi Barang adalah aplikasi berbasis web yang dibuat untuk membantu pengelolaan persediaan barang di gudang. 
Aplikasi ini dikembangkan menggunakan Python dan Flask dengan tampilan yang sederhana agar pengguna lebih mudah mengelola data serta memantau pergerakan barang.
Project ini dibuat sebagai bagian dari tugas perkuliahan dengan judul Pengembangan Sistem Informasi Inventaris Barang Berbasis Web Menggunakan Flask.

🎯 Tujuan Project
Project ini bertujuan untuk mempermudah proses pencatatan dan pemantauan persediaan barang di gudang, 
khususnya dalam mengelola data barang serta mencatat transaksi barang masuk dan keluar.

✨ Fitur Utama
Dashboard: Menampilkan ringkasan informasi inventaris dan grafik pergerakan barang.
Manajemen Data Barang: Menampilkan, menambahkan, mengedit, dan menghapus data barang.
Barang Masuk: Mencatat barang yang masuk ke gudang.
Barang Keluar: Mencatat barang yang keluar untuk keperluan distribusi.
Grafik Inventaris: Menampilkan visualisasi pergerakan barang menggunakan Chart.js.

🛠️ Teknologi yang Digunakan
Python sebagai bahasa pemrograman.
Flask sebagai framework pengembangan aplikasi web.
HTML untuk menyusun struktur halaman.
CSS untuk mengatur tampilan aplikasi.
JavaScript untuk mendukung interaksi pada halaman web.
Chart.js untuk menampilkan grafik inventaris.
Git dan GitHub untuk pengelolaan kode dan kolaborasi project.

📁 Struktur Project
Projek-Sistem-Inventaris-Flask/
├── app.py
├── requirements.txt
├── templates/
│   ├── index.html
│   └── ...
├── static/
│   ├── css/
│   ├── js/
│   ├── img/
│   └── vendor/
└── README.md

Keterangan:
app.py: File utama yang mengatur aplikasi Flask, halaman, dan proses pengelolaan inventaris.
requirements.txt: Daftar library Python yang dibutuhkan aplikasi.
templates/: Menyimpan file HTML untuk tampilan halaman web.
static/: Menyimpan file CSS, JavaScript, gambar, dan aset pendukung lainnya.
README.md: Dokumentasi singkat mengenai project.

🚀 Cara Menjalankan Project
1. Clone Repository
git clone https://github.com/novaladitya648-cpu/Projek-Sistem-Inventaris-Flask.git
2. Masuk ke Folder Project
cd Projek-Sistem-Inventaris-Flask
3. Buat Virtual Environment
python -m venv venv
4. Aktifkan Virtual Environment

Untuk Windows:
venv\Scripts\activate
5. Install Dependencies
pip install -r requirements.txt
6. Jalankan Aplikasi
python app.py
Setelah aplikasi berjalan, buka browser dan akses alamat lokal yang ditampilkan pada terminal, biasanya:
http://127.0.0.1:5000
Catatan: Pastikan Python sudah terinstal dan seluruh dependencies berhasil dipasang sebelum menjalankan aplikasi.

👥 Kolaborasi Project
Project ini dikembangkan secara berkelompok. GitHub digunakan untuk menyimpan kode sumber, memantau perubahan, 
dan memudahkan anggota kelompok berkolaborasi selama proses pengembangan.

📝 Penutup
Melalui project ini, kami mempelajari penerapan Flask dalam pengembangan aplikasi web, pengelolaan struktur folder, 
penggunaan template HTML, pengaturan routes, serta pembuatan visualisasi data menggunakan Chart.js.
Diharapkan aplikasi ini dapat menjadi contoh sederhana penerapan sistem informasi untuk membantu pengelolaan inventaris pada gudang distribusi barang.
