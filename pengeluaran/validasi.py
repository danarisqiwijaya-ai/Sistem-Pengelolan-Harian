class DataTidakValidError(ValueError):
    pass


def validasi_nominal(nominal):
    # Memastikan nominal berupa angka dan tidak negatif.
    if not isinstance(nominal, (int, float)):
        raise DataTidakValidError("Nominal harus berupa angka.")

    if nominal < 0:
        raise DataTidakValidError("Nominal tidak boleh negatif.")

    assert nominal >= 0, "Nominal harus bernilai positif atau nol."

    return True


def validasi_data(tanggal, kategori, keterangan, nominal):
    # Memastikan data utama tidak kosong.
    if not tanggal or not kategori or not keterangan:
        raise DataTidakValidError(
            "Tanggal, kategori, dan keterangan tidak boleh kosong."
        )

    validasi_nominal(nominal)

    return True
