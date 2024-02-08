"# MySQL CRUD Flet-Projekt"

Python Allgemein
================
Ggf. "pip" aktualisieren
[shell] py -m pip install --upgrade pip

Version von pip prüfen
[shell] py -m pip --version


Flet Projekt
============
Virtuelle Umgebung erstellen
[shell] pip install pipenv

Virtuelle Umgebung wird unter: C:\Users\[UserName]]\.virtualenvs\... erstellt

Virtuelle Umgebung aktivieren und Virtuellen Namen anzeigen lassen
--> (Achtung nach Start von VS Code immer darauf achten, dass man in der richtigen Virtuellen Umgebung ist!)

[shell] pipenv shell
    es erscheint nun in der cmd: "(MySQL-Flet-...) [Pfad zum Projektverzeichnis]\MySQL-Flet"

Flet, MySQL Connector, Base64 in der Virtuellen Umgebung installieren
[shell] pipenv install flet
[shell] pipenv install mysql-connector-python
[shell] pipenv install pybase64


Starten des Entwicklungsservers mit automatischer Aktualisierung der App bei Änderungen
[shell] flet run -r main.py

