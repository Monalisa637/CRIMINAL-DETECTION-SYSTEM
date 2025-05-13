# 🕵️ Criminal Management System

A desktop-based Criminal Management System using **Python**, **Tkinter**, **OpenCV**, and **MySQL**. It enables users to manage criminal records, capture facial images via webcam, and train a face recognition model.

---

## 💡 Features

- Register, update, delete, and search criminal records
- Real-time face image capture using webcam
- LBPH-based face recognition training
- MySQL database integration
- Clean UI with Tkinter and images

---

## 🗂️ Project Structure

criminal-management/
├── criminal.py # Main GUI app
├── haarcascade_frontalface_default.xml
├── classifier.xml (generated)
├── data/ (auto-created for face images)
├── IMAGES/
│ ├── logo.png
│ └── law.png


---

## 🔧 Requirements

Install with:
```bash
pip install opencv-python pillow numpy mysql-connector-python

CREATE DATABASE details;

CREATE TABLE crime (
  caseid VARCHAR(20),
  criminalno VARCHAR(20),
  dateofcrime VARCHAR(20),
  age VARCHAR(10),
  gender VARCHAR(10),
  criminalname VARCHAR(50),
  status VARCHAR(20),
  address VARCHAR(100),
  criminaltype VARCHAR(30)
);


python criminal.py



 Build Executable
bash
Copy
Edit
pyinstaller --onefile --noconsole \
--add-data "IMAGES/logo.png;IMAGES" \
--add-data "IMAGES/law.png;IMAGES" \
--add-data "haarcascade_frontalface_default.xml;." \
criminal.py
Replace ; with : on Linux/macOS.


📸 Usage Flow
Fill the form and click "Save"

Click "Take Photo" to capture 100 face samples

Click "Save Photo" to train the model

Use Search to find records

## Author

Made with ❤️ by Monalisa Ray  
GitHub: https://github.com/Monalisa637  


If you find this project useful, please ⭐ star it and share!
        
