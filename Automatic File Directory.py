import os
import shutil

# Tentukan direktori yang ingin diatur
source_directory = r'D:\Teknik Komputer\UAS\UAS SEMESTER 5\Python Lanjut\TEST FOLDER'
image_directory = os.path.join(source_directory, 'Gambar')
document_directory = os.path.join(source_directory, 'Dokumen')

# Buat folder jika belum ada
os.makedirs(image_directory, exist_ok=True)
os.makedirs(document_directory, exist_ok=True)

# Daftar ekstensi file untuk gambar dan dokumen
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
document_extensions = ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx']

# Fungsi untuk memindahkan file
def organize_files():
    for filename in os.listdir(source_directory):
        file_path = os.path.join(source_directory, filename)

        # Cek apakah itu file
        if os.path.isfile(file_path):
            # Cek ekstensi file
            _, extension = os.path.splitext(filename)

            if extension.lower() in image_extensions:
                shutil.move(file_path, image_directory)
                print(f'Memindahkan {filename} ke folder Gambar')
            elif extension.lower() in document_extensions:
                shutil.move(file_path, document_directory)
                print(f'Memindahkan {filename} ke folder Dokumen')

# Jalankan fungsi
if __name__ == "__main__":
    organize_files()
