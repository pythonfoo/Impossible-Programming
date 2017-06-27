#!/usr/bin/env python3

# Importieren des PySide Moduls
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# Das backend wird importiert
from backend import *

import sys

# So können Argumente für Qt5 dem Programm übergeben werden
app = QApplication(sys.argv)

# Das Fenster wird erstellt
window = QWidget()

# Vertikales Layout
layout = QVBoxLayout()

# 1. Label "Schreibe"
write_label = QLabel("Schreibe")
# 2. Label "in"
in_label = QLabel("in")

# 3. Label "mit"
# with_label = QLabel("mit")



# 1. Textfeld: Projekt
project = QLineEdit(window)
# 2. Textfeld: Programmiersprache
language = QLineEdit(window)
# 3. Textfeld: Herausforderung
constraint = QLineEdit(window)

# Die beiden Knöpfe werden initialisiert
new_button = QPushButton("New", window)
save_button = QPushButton("Save", window)
load_button = QPushButton("Load", window)

# Die Aktionen beim Drücken der Knöpfe werden definiert
def onClick_new():
    project_str = get_project()
    language_str = get_language()
    constraint_str = get_constraint()
    project.setText(project_str)
    language.setText(language_str)
    constraint.setText(constraint_str)
    result_str = get_job(project_str, language_str, constraint_str)
    mb = QMessageBox(QMessageBox.Information, "Aufgabe", result_str, QMessageBox.Ok, window)
    mb.show()
    

def onClick_save():
    project_str = project.text()
    language_str = language.text()
    constraint_str = constraint.text()
    result_str = get_job(project_str, language_str, constraint_str)
    save_job(result_str)

def onClick_load():
    pass

# Den Knöpfen werden ihre Aktionen zugeordnet
new_button.clicked.connect(onClick_new)
save_button.clicked.connect(onClick_save)
load_button.clicked.connect(onClick_load)

# Die Elemente werden in das Layout hinzugefügt:
layout.addWidget(write_label)
layout.addWidget(project)
layout.addWidget(in_label)
layout.addWidget(language)
# layout.addWidget(with_label)
layout.addWidget(constraint)
layout.addWidget(new_button)
layout.addWidget(save_button)
layout.addWidget(load_button)

# Das Layout wird zum Fenster hinzugefügt
window.setLayout(layout)

# Fenster anzeigen
window.show()

# App ausführen
app.exec_()