from datetime import datetime
import os
import shutil

print(f"-- File Organizer - {datetime.now().strftime('%H:%M')} --\n")

folder = "Folder-Test"
files = [
    "photo.jpg",
    "document.pdf",
    "music.mp3",
    "homework.docx",
    "image.png",
    "script.py"
]

folders = {
    ".jpg": "Pics",
    ".png": "Pics",
    ".pdf": "Docs",
    ".docx": "Docs",
    ".mp3": "Music",
    ".py": "Python"
}

def organize_files():
    listed_folder = os.listdir(folder)
    print(f"\nFiles in {folder}: {listed_folder}\n")

    for filename in listed_folder:
        source = os.path.join(folder, filename)
        
        if not os.path.isfile(source):
            continue
        
        _, extension = os.path.splitext(filename)
        
        destination = folders.get(extension)

        if destination is None:
            print(f"No folder configured for {filename}.")
            continue
        
        destination_path = os.path.join(folder, destination)
        
        if not os.path.exists(destination_path):
            os.mkdir(destination_path)
            print(f"Folder '{destination}' created.")
            
        shutil.move(source, os.path.join(destination_path, filename))
        
        print(f"{filename} moved to {destination}.")

if not os.path.exists(folder):
    os.mkdir(folder)

    for i in files:
        open(f"{folder}/{i}", "w")
        print(f"File {i} created.")

else:
    print("Test folder already exists.\n")

organize_files()