import os
import shutil

source_directory = r'D:\Teknik Komputer\UAS\UAS SEMESTER 5\Python Lanjut\TEST FOLDER'
image_directory = os.path.join(source_directory, 'Gambar')
document_directory = os.path.join(source_directory, 'Dokumen')

os.makedirs(image_directory, exist_ok=True)
os.makedirs(document_directory, exist_ok=True)

image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
document_extensions = ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx']

def organize_files():
    for filename in os.listdir(source_directory):
        file_path = os.path.join(source_directory, filename)

        if os.path.isfile(file_path):
            _, extension = os.path.splitext(filename)

            if extension.lower() in image_extensions:
                shutil.move(file_path, image_directory)
                print(f'Memindahkan {filename} ke folder Gambar')
            elif extension.lower() in document_extensions:
                shutil.move(file_path, document_directory)
                print(f'Memindahkan {filename} ke folder Dokumen')

if __name__ == "__main__":
    organize_files()
