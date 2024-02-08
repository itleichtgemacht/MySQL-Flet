from mysql.connector import MySQLConnection, Error
from configparser import ConfigParser
import base64

def read_config(filename='.\\MySQLconfig\\app.ini', section='mysql'):    
    # Create a ConfigParser object to handle INI file parsing
    config = ConfigParser()
    
    # Read the specified INI configuration file
    config.read(filename)

    # Initialize an empty dictionary to store configuration data
    data = {}

    # Check if the specified section exists in the INI file
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
        raise Exception(f'{section} section not found in the {filename} file')

    # Return the populated data dictionary
    return data

def find_book_by_isbn(isbn):
    args = (isbn, 0)
    try:
        # Read database configuration from the config file
        config = read_config()

        # Establish a connection to the MySQL database
        with MySQLConnection(**config) as conn:
            # Create a cursor to execute SQL queries
            with conn.cursor() as cursor:
                # Call the stored procedure 'find_by_isbn'
                result_args = cursor.callproc('find_by_isbn', args)
                book_title = result_args[1]
                return book_title

    except Error as e:
        print(e)
        raise e
    
    
def find_by_id(id):
    args = (id,0,0)
    try:
        # Read database configuration from the config file
        config = read_config()

        # Establish a connection to the MySQL database
        with MySQLConnection(**config) as conn:
            # Create a cursor to execute SQL queries
            with conn.cursor() as cursor:
                # Call the stored procedure 'find_by_isbn'
                cursor.callproc('find_by_id',args)
                results = []
                for result in cursor.stored_results():
                    results.append(result.fetchall())
                return results

    except Error as e:
        raise e
    
    
def update_by_id(id, title, isbn):
    args = (id,title,isbn)
    print(f"update_by_id: {id} {title} {isbn}")
    try:
        # Read database configuration from the config file
        config = read_config()

        # Establish a connection to the MySQL database
        with MySQLConnection(**config) as conn:
            # Create a cursor to execute SQL queries
            with conn.cursor() as cursor:
                # Call the stored procedure 'find_by_isbn'
                cursor.callproc('update_by_id',args)
                conn.commit()

    except Error as e:
        print(e)
        raise e


def delete_by_id(id):
    args = (id,0)
    print(f"delete_by_id: {id}")
    try:
        # Read database configuration from the config file
        config = read_config()

        # Establish a connection to the MySQL database
        with MySQLConnection(**config) as conn:
            # Create a cursor to execute SQL queries
            with conn.cursor() as cursor:
                # Call the stored procedure 'find_by_isbn'
                cursor.callproc('delete_by_id',args)
                conn.commit()

    except Error as e:
        print(e)
        raise e




def find_all_books():
    try:
        # Read database configuration from the config file
        config = read_config()

        # Establish a connection to the MySQL database
        with MySQLConnection(**config) as conn:
            # Create a cursor to execute SQL queries
            with conn.cursor() as cursor:
                # Call the stored procedure 'find_all'
                cursor.callproc('find_all')

                # Process the results of the stored procedure
                results = []
                for result in cursor.stored_results():
                    results.append(result.fetchall())

                return results

    except Error as e:
        raise e

def fetch_all_books():
    try:
        # Read database configuration from the config file
        config = read_config()
        
        # Establish a connection to the MySQL database using the provided configuration
        conn = MySQLConnection(**config)
        
        # Create a cursor to interact with the database
        cursor = conn.cursor()
        
        # Execute a SELECT query to retrieve all rows from the 'books' table
        cursor.execute("SELECT * FROM books")
        
        # Fetch all rows from the result set
        rows = cursor.fetchall()

        # Print the total number of rows returned by the query
        print('Total Row(s):', cursor.rowcount)
        
        # Loop through all rows and print them
        #for row in rows:
        #    print(row)
        return rows
    
    except Error as e:
        # Print an error message if an error occurs during the execution of the query
        print(e)

    finally:
        # Close the cursor and connection in the 'finally' block to ensure it happens
        crs =cursor.fetchall()
        
        #print('crs 1: ', crs)
        #cursor.close()
        #conn.close()   
        #print('crs 2: ', crs)
        #return crs 
    