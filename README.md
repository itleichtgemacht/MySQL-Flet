<<<<<<< HEAD
# MySQL-Flet
Vollständiges MySQL Flet Projekt mit den Standard 'CRUD' und MySQL Stored Procedure's
=======
"# MeinFletProjekt"

Python Allgemein

Ggf. "pip" aktualisieren
[shell] py -m pip install --upgrade pip

Version von pip prüfen
[shell] py -m pip --version

Flet Projekt

Virtuelle Umgebung erstellen
[shell] pip install pipenv
Virtuelle Umgebung wird unter: C:\Users\Armin Huenniger\.virtualenvs\... erstellt

Virtuelle Umgebung aktivieren und Virtuellen Namen anzeigen lassen
--> (Achtung nach Start von VS Code immer darauf achten, dass man in der richtigen Virtuellen Umgebung ist!)

    [shell] pipenv shell
    es erscheint nun in der cmd: "(meinProjekt-D_m_xrGd) C:\_dev\Python-Projekte\django\meinProjekt>"

Flet in der Virtuellen Umgebung installieren
[shell] pipenv install flet

Starten des Entwicklungsservers mit automatischer Aktualisierung der App bei Änderungen
[shell] flet run -r main.py

Prüfen GIT Befehle
Git init
echo "# MeinFletProjekt" >> README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/itleichtgemacht/MeinFletProjekt.git


MySQL:
https://www.mysqltutorial.org/python-mysql/


# ### AH
# Text (Passwort) verschlüsseln mit Benutzereingabe
# ---
# py-Package:  [shell] pipenv install pybase64 
# Hilfe unter: https://www.pythonhelp.org/tutorials/how-to-install-base64/
# ###


Listen und Arrays
https://snakify.org/de/lessons/two_dimensional_lists_arrays/

>>>>>>> 1a2249c (Initial Commit)
