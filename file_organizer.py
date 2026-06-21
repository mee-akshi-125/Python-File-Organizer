import os
import shutil

folder_path = input("Enter folder path: ")

file_types = {
    "Images": [".jpg", ".jpeg", ".png"],
    "PDFs": [".pdf"],
    "Documents": [".doc", ".docx", ".txt"],
    "Videos": [".mp4", ".avi"]
}

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    if os.path.isfile(file_path):
        moved = False

        for folder, extensions in file_types.items():
            if filename.lower().endswith(tuple(extensions)):
                target_folder = os.path.join(folder_path, folder)

                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)

                shutil.move(file_path,
                            os.path.join(target_folder, filename))

                print(f"Moved {filename} to {folder}")
                moved = True
                break

        if not moved:
            other_folder = os.path.join(folder_path, "Others")

            if not os.path.exists(other_folder):
                os.makedirs(other_folder)

            shutil.move(file_path,
                        os.path.join(other_folder, filename))

            print(f"Moved {filename} to Others")

print("File organization completed!")