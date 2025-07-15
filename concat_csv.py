import pandas as pd
import os

def combine_csv_files(folder_path, output_file):
    # List to hold DataFrames
    dfs = []

    # Loop through all files in the folder
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        # Process only CSV files
        if file.lower().endswith('.csv'):
            print(f"Reading CSV: {file}")
            df = pd.read_csv(file_path, header= 0,
                        encoding= 'unicode_escape')
            dfs.append(df)

        # Optionally handle Excel files too (.xls, .xlsx)
        elif file.lower().endswith(('.xls', '.xlsx')):
            print(f"Reading Excel: {file}")
            df = pd.read_excel(file_path)
            dfs.append(df)

    # Concatenate all DataFrames
    combined_df = pd.concat(dfs, ignore_index=True)

    # Save to output CSV
    combined_df.to_csv(output_file, index=False)
    print(f"All files combined and saved to: {output_file}")

# Example usage
input_folder = "./csv_files"
output_csv = "combined_data.csv" 

combine_csv_files(input_folder, output_csv)