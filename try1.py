import os
import zipfile

# Function to unzip a file and return the list of extracted files
def unzip_file(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    return [os.path.join(extract_to, f) for f in os.listdir(extract_to)]

# Function to move files based on extension using os.rename
def move_files_by_extension(file_list, json_folder, csv_folder):
    for file_path in file_list:
        filename = os.path.basename(file_path)
        if file_path.endswith('.json'):
            os.rename(file_path, os.path.join(json_folder, filename))
        elif file_path.endswith('.csv'):
            os.rename(file_path, os.path.join(csv_folder, filename))

# Create folders for JSON and CSV files
os.makedirs('json_files', exist_ok=True)
os.makedirs('csv_files', exist_ok=True)

# List of zip files to process
zip_files = ['file1.zip', 'file2.zip', 'file3.zip']  # Replace with your actual zip file names

# Temporary extraction folder
temp_extract_folder = 'temp_extract'
os.makedirs(temp_extract_folder, exist_ok=True)

# Process each zip file
for zip_file in zip_files:
    extracted_files = unzip_file(zip_file, temp_extract_folder)
    move_files_by_extension(extracted_files, 'json_files', 'csv_files')
    # Clean up temp folder for next iteration
    for f in os.listdir(temp_extract_folder):
        os.remove(os.path.join(temp_extract_folder, f))

# Remove temporary folder
os.rmdir(temp_extract_folder)

print("✅ All JSON and CSV files have been organized into their respective folders.")
