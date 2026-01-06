# Aplikasi Inventory Management System (IMS) Apotik

Aplikasi ini adalah Sistem Manajemen Inventaris (IMS) yang dibuat khusus untuk apotik. Dibangun menggunakan framework Django, aplikasi ini membantu dalam mengelola stok obat, mencatat penjualan dan pembelian, serta menghasilkan laporan.

## Fitur Utama

*   **Manajemen Stok:** Kelola data obat, termasuk nama, kategori, stok, dan tanggal kedaluwarsa.
*   **Transaksi:** Catat transaksi pembelian dari pemasok dan penjualan kepada pasien/pelanggan.
*   **Manajemen Pasien:** Simpan data pasien untuk melacak riwayat pembelian.
*   **Pelaporan:** Hasilkan laporan penjualan, laporan pembelian, dan laporan laba-rugi untuk menganalisis kinerja apotik.
*   **Antarmuka Web:** Antarmuka yang mudah digunakan untuk mengelola semua aspek operasional apotik.

## Menjalankan Proyek

Untuk menjalankan proyek ini, ikuti langkah-langkah berikut:

1.  **Aktifkan Lingkungan Virtual:**
    ```bash
    source .venv/bin/activate
    ```

2.  **Instal Ketergantungan:**
    ```bash
    pip install -r mysite/requirements.txt
    ```

3.  **Jalankan Migrasi:**
    ```bash
    python mysite/manage.py migrate
    ```

4.  **Jalankan Server Pengembangan:**
    ```bash
    ./devserver.sh
    ```

## Struktur Proyek

Proyek ini mengikuti struktur proyek Django pada umumnya:

*   `mysite/`: Direktori utama proyek.
*   `inventory/`: Aplikasi Django untuk mengelola inventaris (obat, pasien, pembelian, penjualan).
*   `reports/`: Aplikasi Django untuk membuat laporan (penjualan, laba-rugi).
*   `db.sqlite3`: File database SQLite.
*   `requirements.txt`: Daftar pustaka Python yang dibutuhkan.

## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT. Lihat file `LICENSE` untuk detailnya.
