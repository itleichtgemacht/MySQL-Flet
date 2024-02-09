# MySQL CRUD Flet-Projekt

> [!NOTE]
> In diesem Beispiel wird folgendes behandelt:
> - MySQL - **C**reate**R**ead**U**pdate**D**elete
> - Flet Framework
> - ResponsiveRow
> - NavigationsBar


| Dokumentationen       |  Link                                                    |
| --------------------- | -------------------------------------------------------- |
| Flet - Controls:      | https://flet.dev/docs/controls/                          |
| Flet - Icon Browser:  | https://gallery.flet.dev/icons-browser/                  |
| MySQL Server:		| https://dev.mysql.com/doc/refman/8.3/en/installing.html  |

 
# Python Allgemein

pip aktualisieren, Version prüfen
```Shell
[shell] py -m pip install --upgrade pip
[shell] py -m pip --version
```

# Flet Projekt

* Virtuelle Umgebung erstellen
```Shell  
  [shell] pip install pipenv
```

  Virtuelle Umgebung wird unter: C:\Users\[UserName]]\.virtualenvs\... erstellt

* Virtuelle Umgebung aktivieren und Virtuellen Namen anzeigen lassen
  ** Achtung nach Start von VS Code immer darauf achten, dass man in der richtigen Virtuellen Umgebung ist! **
```Shell
  [shell] pipenv shell
```
  es erscheint nun in der cmd: "(MySQL-Flet-...) [Pfad zum Projektverzeichnis]\MySQL-Flet"

* Python Pakete, die in diesem Projekt verwendet werden

Flet, MySQL Connector, Base64 in der Virtuellen Umgebung installieren

```Shell
[shell] pipenv install flet

[shell] pipenv install mysql-connector-python

[shell] pipenv install pybase64
```

* Starten des Entwicklungsservers mit automatischer Aktualisierung der App bei Änderungen
* 
[shell] flet run -r main.py

<!--
Allgemeines zu git
==================
https://boolie.org/git-github-anfaenger-tutorial/
-->

# MySQL Stored Procedure

```MySQL
CREATE PROCEDURE `update_by_id`(
	IN p_id INT, p_title VARCHAR(255), p_isbn VARCHAR(100)
)
BEGIN
    IF p_id=0 THEN
		INSERT INTO books VALUES (0,p_title,p_isbn);
    ELSE
		UPDATE books SET title=p_title, isbn=p_isbn
		WHERE id = p_id;
	END IF;
END

CREATE PROCEDURE `find_by_id`(
	IN p_id INT,
    OUT  p_title VARCHAR(255), p_isbn VARCHAR(255)
)
BEGIN
	SELECT 
			id,
			title, 
			isbn
	FROM books 
	WHERE id = p_id;
END

CREATE PROCEDURE `delete_by_id`(
	IN p_id INT, p_2 INT
)
BEGIN
	DELETE FROM books
	WHERE id = p_id;
END

CREATE PROCEDURE `find_all`()
BEGIN
	SELECT 
		books.id,
		title, 
		isbn, 
        CONCAT(first_name,' ',last_name) AS author
	FROM books
	INNER JOIN book_author 
		ON book_author.book_id =  books.id
	INNER JOIN authors
		ON book_author.author_id = authors.id
	ORDER BY title;
END
```
