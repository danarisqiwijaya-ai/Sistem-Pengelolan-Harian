def hitung_total(*nominal):
    # Menghitung total menggunakan *args.
    return sum(nominal)


def hitung_rata_rata(data):
    # Menghitung rata-rata pengeluaran.
    if not data:
        return 0

    total = hitung_total(*(item.nominal for item in data))

    return total / len(data)


def cari_terbesar(data):
    # Mencari pengeluaran terbesar menggunakan lambda.
    if not data:
        return None

    return max(
        data,
        key=lambda item: item.nominal
    )


def cari_terkecil(data):
    # Mencari pengeluaran terkecil menggunakan lambda.
    if not data:
        return None

    return min(
        data,
        key=lambda item: item.nominal
    )


def urutkan_data(data, descending=True):
    # Mengurutkan data berdasarkan nominal.
    return sorted(
        data,
        key=lambda item: item.nominal,
        reverse=descending
    )


def hitung_per_kategori(data):
    # Menghitung total pengeluaran setiap kategori.
    hasil = {}

    for item in data:
        hasil[item.kategori] = (
            hasil.get(item.kategori, 0) + item.nominal
        )

    return hasil


def buat_laporan(data, *, judul="LAPORAN PENGELUARAN HARIAN"):
    # Membuat laporan menggunakan keyword argument.
    total = hitung_total(
        *(item.nominal for item in data)
    )

    rata = hitung_rata_rata(data)
    terbesar = cari_terbesar(data)
    terkecil = cari_terkecil(data)

    laporan = []

    laporan.append(judul)
    laporan.append("=" * len(judul))
    laporan.append(f"Jumlah data: {len(data)}")
    laporan.append(f"Total pengeluaran: Rp{total}")
    laporan.append(
        f"Rata-rata pengeluaran: Rp{rata:.2f}"
    )

    if terbesar:
        laporan.append(
            f"Pengeluaran terbesar: "
            f"Rp{terbesar.nominal} - {terbesar.keterangan}"
        )

    if terkecil:
        laporan.append(
            f"Pengeluaran terkecil: "
            f"Rp{terkecil.nominal} - {terkecil.keterangan}"
        )

    laporan.append("")
    laporan.append("Pengeluaran berdasarkan kategori:")

    for kategori, jumlah in hitung_per_kategori(data).items():
        laporan.append(
            f"- {kategori}: Rp{jumlah}"
        )

    laporan.append("")
    laporan.append("Daftar pengeluaran:")

    for item in urutkan_data(data):
        laporan.append(
            f"{item.tanggal} | "
            f"{item.kategori} | "
            f"{item.keterangan} | "
            f"Rp{item.nominal}"
        )

    return "\n".join(laporan)
