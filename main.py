import os
import hashlib

def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        while True:
            data = f.read(65536)
            if not data:
                break
            sha256_hash.update(data)
    return sha256_hash.hexdigest()

def get_file_description(file_name):
    if file_name.endswith(('.txt', '.log')):
        return "Text File"
    elif file_name.endswith(('.jpg', '.jpeg', '.png', '.gif')):
        return "Image File"
    elif file_name.endswith(('.mp4', '.mkv', '.avi')):
        return "Video File"
    elif file_name.endswith(('.mp3', '.wav')):
        return "Audio File"
    elif file_name.endswith(('.py', '.java', '.c', '.cpp')):
        return "Code File"
    elif file_name.endswith(('.pdf', '.docx', '.xlsx')):
        return "Document File"
    else:
        return "Other File"

def check_integrity(directory_path):
    if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
        print(f"Directory {directory_path} does not exist")
        return
    
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            calculated_hash = calculate_sha256(file_path)
            file_description = get_file_description(file_name)
            print(f"File: {file_path}")
            print(f"Type: {file_description}")
            print(f"SHA-256 Hash: {calculated_hash}\n")

if __name__ == "__main__":
    directory_to_check = input("Enter the directory path to check integrity: ")
    check_integrity(directory_to_check)