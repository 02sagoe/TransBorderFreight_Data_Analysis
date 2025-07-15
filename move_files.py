import os
import shutil

def move_excel_files(root_folder, target_folder):
    # Create the target folder if it doesn't exist
    os.makedirs(target_folder, exist_ok=True)

    # Walk through all subdirectories
    for foldername, subfolders, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.lower().endswith(('.csv', '.xlsx')):
                file_path = os.path.join(foldername, filename)
                
                # Handle duplicate filenames by adding a number if needed
                new_filename = filename
                counter = 1
                base_name, ext = os.path.splitext(filename)
                dest_path = os.path.join(target_folder, new_filename)

                while os.path.exists(dest_path):
                    new_filename = f"{base_name}_{counter}{ext}"
                    dest_path = os.path.join(target_folder, new_filename)
                    counter += 1

                # Move the file
                shutil.move(file_path, dest_path)
                print(f"Moved: {filename} -> {new_filename}")

if __name__ == "__main__":
    extracted_dir = "./extracted"     # Folder where everything was extracted
    excel_files_dir = "./csv_files"     # Target folder to collect Excel files

    move_excel_files(extracted_dir, excel_files_dir)