import os
import zipfile
import shutil

def extract_zip(zip_path, extract_to):
    """Extract a zip file to a specified folder."""
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Extracted: {zip_path}")

def find_and_extract_zips(start_folder, output_folder):
    """Recursively find and extract zip files, collect Excel files."""
    for root, dirs, files in os.walk(start_folder):
        for file in files:
            file_path = os.path.join(root, file)
            if file.lower().endswith('.zip'):
                # Create a folder for each nested zip extraction
                relative_path = os.path.relpath(root, start_folder)
                new_extract_folder = os.path.join(output_folder, "extracted", relative_path, os.path.splitext(file)[0])
                extract_zip(file_path, new_extract_folder)
            elif file.lower().endswith(('.xls', '.xlsx', 'csv')):
                # Copy Excel files to output folder
                dest_path = os.path.join(output_folder, "csv_files", file)
                counter = 1
                while os.path.exists(dest_path):
                    dest_path = os.path.join(output_folder, "csv_files", f"{os.path.splitext(file)[0]}_{counter}{os.path.splitext(file)[1]}")
                    counter += 1
                shutil.copy(file_path, dest_path)
                print(f"Copied Excel file: {file_path} -> {dest_path}")

def main(main_zip_path, temp_extract_folder, final_excel_folder):
    # Step 1: Clear previous runs
    if os.path.exists(temp_extract_folder):
        shutil.rmtree(temp_extract_folder)
    if os.path.exists(final_excel_folder):
        shutil.rmtree(final_excel_folder)

    os.makedirs(temp_extract_folder)

    # Step 2: Extract the main zip
    extract_zip(main_zip_path, temp_extract_folder)

    # Step 3: Process nested zips and collect Excel files
    find_and_extract_zips(temp_extract_folder, output_folder=os.path.dirname(final_excel_folder))

if __name__ == "__main__":
    main_zip_path = "data.zip"  # <-- Replace with your zip path
    temp_extract_folder = "./unpacked_main"
    final_excel_folder="./csv_files"

    main(main_zip_path, temp_extract_folder, final_excel_folder)