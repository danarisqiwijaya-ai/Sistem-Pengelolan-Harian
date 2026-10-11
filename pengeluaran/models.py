class Pengeluaran:
    def __init__(self, tanggal, kategori, keterangan, nominal):
        self.tanggal = tanggal
        self.kategori = kategori
        self.keterangan = keterangan
        self.nominal = nominal

    def to_dict(self):
        # Mengubah objek menjadi dictionary.
        return {
            "tanggal": self.tanggal,
            "kategori": self.kategori,
            "keterangan": self.keterangan,
            "nominal": self.nominal
        }

    def to_line(self):
        # Mengubah data menjadi satu baris untuk file.
        return f"{self.tanggal};{self.kategori};{self.keterangan};{self.nominal}"


class ManajerPengeluaran:
    def __init__(self, data=None):
        self.data = data if data is not None else []

    def tambah(self, pengeluaran):
        # Menambahkan data pengeluaran.
        self.data.append(pengeluaran)

    def jumlah_data(self):
        # Menghitung jumlah data.
        return len(self.data)

    def semua_data(self):
        # Mengembalikan seluruh data.
        return self.data


def buat_pengeluaran(**kwargs):
    # Membuat objek menggunakan keyword arguments.
    return Pengeluaran(
        tanggal=kwargs["tanggal"],
        kategori=kwargs["kategori"],
        keterangan=kwargs["keterangan"],
        nominal=kwargs["nominal"]
    )
