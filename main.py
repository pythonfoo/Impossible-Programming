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

# 1. Textfeld: Projekt
project = QLineEdit(window)
# project_str = get_project()
# project.setText(project_str)

# 2. Textfeld: Programmiersprache
language = QLineEdit(window)

# 3. Textfeld: Herausforderung
constraints = QLineEdit(window)

# Die beiden Knöpfe werden initialisiert
new_button = QPushButton("New", window)
save_button = QPushButton("Save", window)

# Die Aktionen beim Drücken der Knöpfe werden definiert
def onClick_new():
    pass

def onClick_save():
    pass

# Den Knöpfen werden ihre Aktionen zugeordnet
new_button.clicked.connect(onClick_new)
save_button.clicked.connect(onClick_save)

# Die Elemente werden in das Layout hinzugefügt:
layout.addWidget(project)
layout.addWidget(language)
layout.addWidget(constraints)
layout.addWidget(new_button)
layout.addWidget(save_button)

# Das Layout wird zum Fenster hinzugefügt
window.setLayout(layout)

# Fenster anzeigen
window.show()

# App ausführen
app.exec_()