# Python File Organizer

## 📌 Project Overview

Python File Organizer is an automation script developed using Python. The project automatically organizes files in a selected folder into separate categories based on their file extensions. This helps users keep their files structured and easy to access.

## 🎯 Objective

The main objective of this project is to automate file management by sorting files into appropriate folders such as Images, Documents, PDFs, Videos, and Others.

## 🚀 Features

* Automatically scans a selected folder.
* Organizes image files into an Images folder.
* Organizes PDF files into a PDFs folder.
* Organizes document files into a Documents folder.
* Organizes video files into a Videos folder.
* Moves unsupported file types into an Others folder.
* Creates folders automatically if they do not exist.

## 🛠 Technologies Used

* Python 3.x
* OS Module
* Shutil Module

## 📂 Supported File Types

| Category  | Extensions              |
| --------- | ----------------------- |
| Images    | .jpg, .jpeg, .png, .gif |
| PDFs      | .pdf                    |
| Documents | .doc, .docx, .txt       |
| Videos    | .mp4, .avi, .mkv        |

## ▶️ How to Run

1. Open the project folder in VS Code.
2. Open the terminal.
3. Run the command:

python file_organizer.py

4. Enter the folder path when prompted.
5. The files will be automatically organized into folders.

## 📋 Sample Output

Before Organization:

TestFiles/

* photo.jpg
* report.pdf
* notes.txt
* movie.mp4

After Organization:

TestFiles/

* Images/photo.jpg
* PDFs/report.pdf
* Documents/notes.txt
* Videos/movie.mp4

## 📈 Benefits

* Saves time by automating file organization.
* Reduces manual effort.
* Improves file management and accessibility.
* Easy to use and beginner-friendly.

## 👩‍💻 Author

Adepu Meenakshi

B.Tech Computer Science and Engineering
