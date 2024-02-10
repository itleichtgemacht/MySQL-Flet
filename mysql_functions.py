from mysql.connector import MySQLConnection, Error
from configparser import ConfigParser
import base64
from Log.makelog import * 


# ### AH
# read_config: Liest die Paramater für den MySQL Connector aus der app.ini 
# ###
def read_config(filename='.\\MySQLconfig\\app.ini', section='MySQL'):
    logging.info(f'Lese INI {filename} und Sektion {section}')
    # Create a ConfigParser object to handle INI file parsing
    config = ConfigParser()
    
    # Read the specified INI configuration file
    config.read(filename)

    # Initialize an empty dictionary to store configuration data
    data = {}

    # prüft ob die oben angegebene Section mysql in der INI vorhanden ist
    if config.has_section(section):
        # Retrieve all key-value pairs within the specified section
        items = config.items(section)

        # Populate the data dictionary with the key-value pairs
        for item in items:
            if item[0] == 'password':
                # ### AH
                #  Passwort entschlüsseln aus der INI
                # ###
                decoded_bytes = base64.b64decode(item[1])
                decoded_message = decoded_bytes.decode('utf-8')
                data[item[0]] = decoded_message
            else:
                data[item[0]] = item[1]
    else:
        # Raise an exception if the specified section is not found
        raise Exception(f'Sektion: {section} wurde in der Datei {filename} nicht gefunden')

    # Return the populated data dictionary
    return data

def find_book_by_isbn(isbn):
    args = (isbn, 0)
    try:
        # DB MySQL Parameter für den Connector einlesen aus der app.ini
        config = read_config()

        # Verbindung zur MySQL Datenbank herstellen
        with MySQLConnection(**config) as conn:
            with conn.cursor() as cursor:
                result_args = cursor.callproc('find_by_isbn', args)
                book_title = result_args[1]
                return book_title
    except Error as e:
        print(e)
        raise e
    
    
def find_by_id(id):
    args = (id,0,0)
    try:
        config = read_config()
        with MySQLConnection(**config) as conn:
            with conn.cursor() as cursor:
                cursor.callproc('find_by_id',args)
                results = []
                for result in cursor.stored_results():
                    results.append(result.fetchall())
                return results
    except Error as e:
        logging.ERROR(f'find_by_id {id}: {e}')
        raise e
    
    
def update_by_id(id, title, isbn):
    args = (id,title,isbn)
    print(f"update_by_id: {id} {title} {isbn}")
    try:
        config = read_config()
        with MySQLConnection(**config) as conn:
            with conn.cursor() as cursor:
                cursor.callproc('update_by_id',args)
                # ### AH
                # conn.commit, wird zum speichern der Daten benötigt
                # ###
                conn.commit()
    except Error as e:
        logging.ERROR(f'find_by_id {id} - {title} - {isbn}: {e}')
        raise e


def delete_by_id(id):
    args = (id,0)
    print(f"delete_by_id: {id}")
    try:
        config = read_config()
        with MySQLConnection(**config) as conn:
            with conn.cursor() as cursor:
                cursor.callproc('delete_by_id',args)
                conn.commit()
    except Error as e:
        logging.ERROR(f'delete_by_id {id}: {e}')
        print(e)
        raise e


def find_all_books():
    try:
        config = read_config()
        with MySQLConnection(**config) as conn:
            with conn.cursor() as cursor:
                cursor.callproc('find_all')
                results = []
                for result in cursor.stored_results():
                    results.append(result.fetchall())
                return results
    except Error as e:
        logging.ERROR(f'find_all_books: {e}')
        raise e

    