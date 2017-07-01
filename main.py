#!/usr/bin/env python3
"""
@author: dodo
"""
import sys

# Importieren des PySide Moduls
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# Das backend wird importiert
from backend import *

try:
    from twitter import tweet_job 
except ImportError:
    twitter_integration = False
else:
    twitter_integration = True

global rating
rating = [0]
rating_strings = ("Easy", "Normal", "Hard", "Impossible")

# So können Argumente für Qt5 dem Programm übergeben werden
app = QApplication(sys.argv)

# Das Fenster wird erstellt
main_window = QWidget()
rate_window = QWidget()

# Gitter Layout
layout = QGridLayout()

# Bewertungsfenster Layout:
rate_layout = QVBoxLayout()

# 1. Label "Schreibe"
write_label = QLabel("Schreibe")
# 2. Label "in"
in_label = QLabel("in")

# Hauptfenster:

# 1. Textfeld: Projekt
project = QLineEdit(main_window)
project.setFixedWidth(300)
# 2. Textfeld: Programmiersprache
language = QLineEdit(main_window)
language.setFixedWidth(300)
# 3. Textfeld: Herausforderung
constraint = QLineEdit(main_window)
constraint.setFixedWidth(300)

# 1. Checkbox: Projekt fixieren
project_checkbox = QCheckBox("Fix?")
# 2. Checkbox: Sprache fixieren
language_checkbox = QCheckBox("Fix?")
# 3. Checkbox: Hürde fixieren
constraint_checkbox = QCheckBox("Fix?")

# Die Knöpfe werden initialisiert
new_button = QPushButton("New", main_window)
save_button = QPushButton("Save", main_window)
load_button = QPushButton("Load", main_window)
rate_button = QPushButton("Rate", main_window)
if twitter_integration:
    tweet_button = QPushButton("Tweet", main_window)

# Bewertungsfenster:

# Radiobuttons für die Bewertung
easy_rButton = QRadioButton("Easy")
normal_rButton = QRadioButton("Normal")
hard_rButton = QRadioButton("Hard")
impossible_rButton = QRadioButton("Impossible")
# Button zum Beenden der Bewertung:
rate_quit_button = QPushButton("Rate")

# Funktion zum Anzeigen eines Ergebnises in einer
# Messagebox
def job_messagebox(job):
    mb = QMessageBox(QMessageBox.Information, "Aufgabe", job, QMessageBox.Ok, main_window)
    mb.show()

# Funktion um die aktuelle Aufgabe zu erhalten
def get_current_job():
    current_project = project.text().strip("\n")
    current_language = language.text().strip("\n")
    current_constraint = constraint.text().strip("\n")
    return (current_project, current_language, current_constraint)


# Die Aktionen beim Drücken der Knöpfe werden definiert
def onClick_new():
    if project_checkbox.checkState():
        project_str = project.text()
    else:
        project_str = get_project()
        project.setText(project_str)
    
    if language_checkbox.checkState():
        language_str = language.text()
    else:
        language_str = get_language()
        language.setText(language_str)
    
    if constraint_checkbox.checkState():
        constraint_str = constraint.text()
    else:
        constraint_str = get_constraint()
        constraint.setText(constraint_str)
        
    result_str = get_job(project_str, language_str, constraint_str)
    job_messagebox(result_str)

def onClick_save():
    project_str = project.text()
    language_str = language.text()
    constraint_str = constraint.text()
    job = get_job(project_str, language_str, constraint_str)
    save_job(job)

def onClick_load():
    job = load_rating()
    current_project = job[0]
    current_language = job[1]
    current_constraint = job[2]
    current_rating = job[3]
    job_str= get_job(current_project, current_language, current_constraint)
    rating_str = rating_strings[int(current_rating) - 1]
    mb = QMessageBox(QMessageBox.Information, rating_str, job_str, QMessageBox.Ok, main_window)
    mb.show()
    
def onClick_rate():
    rate_window.show()
    
def onClick_tweet():
    project_str = project.text()
    language_str = language.text()
    constraint_str = constraint.text()
    job = get_job(project_str, language_str, constraint_str)
    if twitter_integration:
        result = tweet_job(job)
    mb = QMessageBox(QMessageBox.Information, "Twitter Feedback", "Der Tweet wurde gesendet", QMessageBox.Ok, main_window)
    if not result:
        mb = QMessageBox(QMessageBox.Information, "Twitter Feedback", "Der Tweet war zu lang", QMessageBox.Ok, main_window)
    mb.show()

def onClick_rate_quit():
    if easy_rButton.pressed:
        rating[0] = 1
    if normal_rButton.pressed:
        rating[0] = 2
    if hard_rButton.pressed:
        rating[0] = 3
    if impossible_rButton.pressed:
        rating[0] = 4
    
    current_job= get_current_job()
    current_project = current_job[0]
    current_language = current_job[1]
    current_constraint = current_job[2]
    current_rating = rating[0]
    save_rating(current_project, current_language, current_constraint, current_rating)
    mb = QMessageBox(QMessageBox.Information, "Bewertung erfolgreich", "Deine Bewertung wurde gespeichert.", QMessageBox.Ok, main_window)
    mb.show()
    rate_window.close()

# Den Knöpfen werden ihre Aktionen zugeordnet
new_button.clicked.connect(onClick_new)
save_button.clicked.connect(onClick_save)
load_button.clicked.connect(onClick_load)
rate_button.clicked.connect(onClick_rate)
if twitter_integration:
    tweet_button.clicked.connect(onClick_tweet)

rate_quit_button.clicked.connect(onClick_rate_quit)

# Die Elemente werden in das Hauptlayout hinzugefügt:
layout.addWidget(write_label,0,0)
layout.addWidget(project, 0, 1)
layout.addWidget(project_checkbox, 0, 2)
layout.addWidget(in_label, 1, 0)
layout.addWidget(language, 1, 1)
layout.addWidget(language_checkbox, 1, 2)
layout.addWidget(constraint, 2, 1)
layout.addWidget(constraint_checkbox, 2, 2)
layout.addWidget(new_button, 3, 0)
layout.addWidget(save_button, 3, 1)
layout.addWidget(load_button, 3, 2)
layout.addWidget(rate_button, 4, 0)
if twitter_integration:
    layout.addWidget(tweet_button, 4, 1)

# Die Elemente werden in das Bewertungslayout hinzugefügt:
rate_layout.addWidget(easy_rButton)
rate_layout.addWidget(normal_rButton)
rate_layout.addWidget(hard_rButton)
rate_layout.addWidget(impossible_rButton)
rate_layout.addWidget(rate_quit_button)

# Das Layout wird zum Fenster hinzugefügt
main_window.setLayout(layout)
rate_window.setLayout(rate_layout)

# Fenster anzeigen
main_window.show()

# App ausführen
app.exec_()