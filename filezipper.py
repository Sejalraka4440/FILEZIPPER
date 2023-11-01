import zipfile
import os

def create_zip_archive(zip_filename, files_to_zip):
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for file_path in files_to_zip:
            if os.path.exists(file_path):
                file_name = os.path.basename(file_path)
                zip_file.write(file_path, file_name)
                print(f"Added '{file_name}' to '{zip_filename}'")
            else:
                print(f"Warning: File '{file_path}' not found, skipping.")

if __name__ == "__main__":
    files_to_zip = ['file1.txt', 'file2.txt']  # Add the file paths you want to zip
    zip_filename = 'my_archive.zip'  # Choose a name for your ZIP archive

    create_zip_archive(zip_filename, files_to_zip)

    print(f"ZIP archive '{zip_filename}' has been created.")
