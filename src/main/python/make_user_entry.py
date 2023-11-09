import sqlite3
from sqlite3 import Error
import numpy as np
from argon2 import PasswordHasher


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def create_user(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO users(user_id,firstname, lastname, username, email, mobile_number, password_hash, salt, role)
              VALUES(?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid

if __name__ == '__main__':
    database = r"users.db"
    # create a database connection
    conn = create_connection(database)

    password = '7684101219$Corsidecap'
    salt_numbers = np.random.randint(0,9,size=6)
    salt = ''
    for i in range(0,len(salt_numbers)):
        salt = salt+str(salt_numbers[i])
    
    salted_password = password+salt
    ph = PasswordHasher()
    hash = ph.hash(salted_password)
    print(hash)

    role = 'administrator'

    with conn:
        user = (1,'david','boutelier','david','boutelier.david@gmail.com','0433665810', hash, salt, role)
        create_user(conn, user)