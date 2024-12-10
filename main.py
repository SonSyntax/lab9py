from view.input_form import input_data
from data.mahasiswa import Mahasiswa
from view.mahasiswa import tampilkan_mahasiswa

def main():
    nama, nim = input_data()
    mahasiswa = Mahasiswa(nama, nim)
    tampilkan_mahasiswa(mahasiswa)

if __name__ == "__main__":
    main()