import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


if __name__ == '__main__':
    database = "users.db"

    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                        user_id integer PRIMARY KEY,
                                        firstname text NOT NULL,
                                        lastname text NOT NULL,
                                        username text NOT NULL UNIQUE,
                                        email text NO NULL UNIQUE,
                                        mobile_number text NOT NULL UNIQUE,
                                        password_hash text NOT NULL,
                                        salt integer NOT NULL,
                                        role text NOT NULL
                                    ); """

    # create a database connection
    conn = create_connection(database)

    # create table
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_users_table)