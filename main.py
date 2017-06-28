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

# Gitter Layout
layout = QGridLayout()

# 1. Label "Schreibe"
write_label = QLabel("Schreibe")
# 2. Label "in"
in_label = QLabel("in")

# 1. Textfeld: Projekt
project = QLineEdit(window)
project.setFixedWidth(300)
# 2. Textfeld: Programmiersprache
language = QLineEdit(window)
language.setFixedWidth(300)
# 3. Textfeld: Herausforderung
constraint = QLineEdit(window)
constraint.setFixedWidth(300)

# Die beiden Knöpfe werden initialisiert
new_button = QPushButton("New", window)
save_button = QPushButton("Save", window)
load_button = QPushButton("Load", window)

# Funktion zum Anzeigen eines Ergebnises in einer
# Messagebox
def job_messagebox(job):
    mb = QMessageBox(QMessageBox.Information, "Aufgabe", job, QMessageBox.Ok, window)
    mb.show()

# Die Aktionen beim Drücken der Knöpfe werden definiert
def onClick_new():
    project_str = get_project()
    language_str = get_language()
    constraint_str = get_constraint()
    project.setText(project_str)
    language.setText(language_str)
    constraint.setText(constraint_str)
    result_str = get_job(project_str, language_str, constraint_str)
    job_messagebox(result_str)

def onClick_save():
    project_str = project.text()
    language_str = language.text()
    constraint_str = constraint.text()
    result_str = get_job(project_str, language_str, constraint_str)
    save_job(result_str)

def onClick_load():
    job = load_job()
    job_messagebox(job)
    
# Den Knöpfen werden ihre Aktionen zugeordnet
new_button.clicked.connect(onClick_new)
save_button.clicked.connect(onClick_save)
load_button.clicked.connect(onClick_load)

# Die Elemente werden in das Layout hinzugefügt:
layout.addWidget(write_label,0,0)
layout.addWidget(project, 0, 1)
layout.addWidget(in_label, 1, 0)
layout.addWidget(language, 1, 1)
layout.addWidget(constraint, 2, 1)
layout.addWidget(new_button, 3, 0)
layout.addWidget(save_button, 3, 1)
layout.addWidget(load_button, 3, 2)

# Das Layout wird zum Fenster hinzugefügt
window.setLayout(layout)

# Fenster anzeigen
window.show()

# App ausführen
app.exec_()

