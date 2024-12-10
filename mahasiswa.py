class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def get_info(self):
        return f"Nama: {self.nama}, NIM: {self.nim}"