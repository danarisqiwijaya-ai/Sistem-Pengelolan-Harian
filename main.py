import os

from pengeluaran.models import buat_pengeluaran
from pengeluaran.fileio import (
    buat_file_data,
    tambah_pengeluaran,
    baca_data,
    tulis_laporan
)
from pengeluaran.processing import buat_laporan
from pengeluaran.validasi import validasi_data


DATA_FILE = "data/pengeluaran.txt"
REPORT_FILE = "laporan/laporan_pengeluaran.txt"


def main():
    # Membuat folder data dan laporan jika belum tersedia.
    os.makedirs("data", exist_ok=True)
    os.makedirs("laporan", exist_ok=True)

    # Membuat file data pertama kali menggunakan mode x.
    file_baru = buat_file_data(DATA_FILE)

    # Jika file baru dibuat, masukkan data awal.
    if file_baru:
        data_awal = [
            buat_pengeluaran(
                tanggal="2026-10-01",
                kategori="Makanan",
                keterangan="Makan siang",
                nominal=25000
            ),
            buat_pengeluaran(
                tanggal="2026-10-02",
                kategori="Transportasi",
                keterangan="Ojek",
                nominal=15000
            ),
            buat_pengeluaran(
                tanggal="2026-10-03",
                kategori="Makanan",
                keterangan="Makan malam",
                nominal=30000
            ),
            buat_pengeluaran(
                tanggal="2026-10-04",
                kategori="Kuliah",
                keterangan="Print tugas",
                nominal=10000
            ),
            buat_pengeluaran(
                tanggal="2026-10-05",
                kategori="Internet",
                keterangan="Paket data",
                nominal=50000
            )
        ]

        for item in data_awal:
            validasi_data(
                tanggal=item.tanggal,
                kategori=item.kategori,
                keterangan=item.keterangan,
                nominal=item.nominal
            )
            tambah_pengeluaran(DATA_FILE, item)

    # Membaca seluruh data dari file.
    data = baca_data(DATA_FILE)

    if not data:
        print("Tidak ada data pengeluaran yang dapat diproses.")
        return

    # Membuat laporan menggunakan keyword argument.
    laporan = buat_laporan(
        data,
        judul="LAPORAN PENGELUARAN HARIAN"
    )

    # Menulis laporan menggunakan mode w.
    tulis_laporan(REPORT_FILE, laporan)

    # Menampilkan laporan ke layar.
    print(laporan)


if __name__ == "__main__":
    main()
