import os
import mimetypes
import shutil
import re

DOWNLOAD_PATH = "/path/to/downloads/folder"
PATH_TO_NEW_DIRECTORY = "/new/path/to/folder"


def list_files(directory_path):
    try:
        entries = os.listdir(directory_path)
        for entry in entries:
            full_path = os.path.join(directory_path, entry)
            if os.path.isfile(full_path):
                mime_type, encoding = mimetypes.guess_type(full_path)
                mime_type = mime_type or "unknown"
                mime_type = re.sub(r'[^\w\-_]', '_', mime_type)
                #print(f"File: {entry}, MIME type: {mime_type}")
                #print(type(mime_type))
                destination = create_directory(PATH_TO_NEW_DIRECTORY, mime_type)
                shutil.move(full_path, destination)
                print(f"{entry} moved from {directory_path} to {destination}")
            elif os.path.isdir(full_path):
                print(f"Folder: {entry}")
            else:
                print(f"Not a file: {entry}")
    except FileNotFoundError:
        print(f"The directory {directory_path} does not exist")
    except PermissionError:
        print(f"You do not have permission to access {directory_path}")


def create_directory(base_path, folder_name):
    sanitized_folder_name = re.sub(r'[^\w\-_]', '_', folder_name or "unknown")
    directory_path = os.path.join(base_path, sanitized_folder_name)
    try:
        os.makedirs(directory_path, exist_ok=True)
        #print(f"{file_path} created")
    except Exception as e:
        #print("Directory already exists")
        print(f"Failed to create directory {directory_path}: {e}")
    return directory_path


def main():
   list_files(DOWNLOAD_PATH)
   

if __name__=="__main__":
    main()