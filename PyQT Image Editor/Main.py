import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QListWidget, QComboBox, QFileDialog)
from PIL import Image, ImageFilter, ImageEnhance
from PyQt5.QtGui import QPixmap

# Initialize screen
app = QApplication([])
window = QWidget()
window.setWindowTitle("Photo QT")
window.resize(800, 600)

# Creating required widgets
select_folder_button = QPushButton("Select Folder")
left_button = QPushButton("Left")
right_button = QPushButton("Right")
mirror_button = QPushButton("Mirror")
sharpness_button = QPushButton("Sharpness")
black_and_white_button = QPushButton("B/W")
color_button = QPushButton("Color")
contrast_button = QPushButton("Contrast")

dropdown_button = QComboBox()
dropdown_button.addItems(["Original", "Left", "Right", "Mirror", "Sharpen", "B/W", "Color", "Contrast", "Blur"])

file_list = QListWidget()
image_label = QLabel("Image Will Be Here")

# managing layout
master_layout = QHBoxLayout()

column_1 = QVBoxLayout()
column_1.addWidget(select_folder_button)
column_1.addWidget(file_list)
column_1.addWidget(dropdown_button)
column_1.addWidget(left_button)
column_1.addWidget(right_button)
column_1.addWidget(mirror_button)
column_1.addWidget(sharpness_button)
column_1.addWidget(black_and_white_button)
column_1.addWidget(color_button)
column_1.addWidget(contrast_button)

column_2 = QVBoxLayout()
column_2.addWidget(image_label)

master_layout.addLayout(column_1, 20)
master_layout.addLayout(column_2, 80)

window.setLayout(master_layout)

# Functions
working_directory = ""

def filter_files(files, extensions):
    results = [file for file in files for ext in extensions if file.endswith(ext)]
    return results

def current_directory():
    global working_directory
    working_directory = QFileDialog.getExistingDirectory()
    extensions = [".jpg", ".jpeg", ".png", ".svg"]
    filenames = filter_files(files=os.listdir(working_directory), extensions=extensions)

    file_list.clear()
    for filename in filenames:
        file_list.addItem(filename)


select_folder_button.clicked.connect(current_directory)



# Showing the window
window.show()
app.exec_()