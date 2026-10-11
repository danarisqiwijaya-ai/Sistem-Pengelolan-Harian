import unittest

from .processing import (
    hitung_total,
    hitung_rata_rata,
    cari_terbesar,
    cari_terkecil,
    urutkan_data
)

from .models import Pengeluaran


class TestPengeluaran(unittest.TestCase):

    def setUp(self):
        self.data = [
            Pengeluaran(
                "2026-10-01",
                "Makanan",
                "Makan siang",
                25000
            ),
            Pengeluaran(
                "2026-10-02",
                "Transportasi",
                "Ojek",
                15000
            ),
            Pengeluaran(
                "2026-10-03",
                "Makanan",
                "Makan malam",
                30000
            ),
            Pengeluaran(
                "2026-10-04",
                "Kuliah",
                "Print tugas",
                10000
            )
        ]

    def test_hitung_total(self):
        hasil = hitung_total(
            25000,
            15000,
            30000,
            10000
        )

        self.assertEqual(hasil, 80000)

    def test_hitung_rata_rata(self):
        hasil = hitung_rata_rata(self.data)

        self.assertEqual(hasil, 20000)

    def test_pengeluaran_terbesar(self):
        hasil = cari_terbesar(self.data)

        self.assertEqual(hasil.nominal, 30000)

    def test_pengeluaran_terkecil(self):
        hasil = cari_terkecil(self.data)

        self.assertEqual(hasil.nominal, 10000)

    def test_urutkan_data(self):
        hasil = urutkan_data(self.data)

        self.assertEqual(hasil[0].nominal, 30000)

    def test_jumlah_data(self):
        self.assertEqual(len(self.data), 4)


if __name__ == "__main__":
    unittest.main()
