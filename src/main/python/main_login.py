from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PyQt5.QtWidgets import (QMainWindow,
    QWidget,
    QTabWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGroupBox,
    QStatusBar,
    QFormLayout,
    QLineEdit,
    QDateEdit,
    QMessageBox,
    QTableWidget,
    QTableView,
    QHeaderView,
    QLabel,
    QComboBox,
    QCheckBox,
    QListWidget)
from PyQt5.uic import loadUi
import sys
import os
import sqlite3
from sqlite3 import Error
import numpy as np
from argon2 import PasswordHasher

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUI()

    def setupUI(self):  
        loadUi(os.path.join('src','main','python','ui','main.ui' ), self)  
        self.setWindowTitle('QDB ')


class login(QWidget):
    def __init__(self, parent=None):
        super(login,self).__init__(parent)
        self.setupUI_login()

    def setupUI_login(self):  
        loadUi(os.path.join('src','main','python','ui','login.ui' ), self)  
        self.setWindowTitle('QDB login')

        self.signin_button.clicked.connect(self.sign_in)
        self.forgot_password_button.clicked.connect(self.change_password)

    def change_password(self):

        provided_username = self.username_line.text()
        if provided_username == None:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Please provide the username')
            msg.setWindowTitle("Error")
            msg.exec_()
        else:
            database = r"users.db"
            conn = self.create_connection(database)
            cur = conn.cursor()
            cur.execute("SELECT * FROM users WHERE username=?", (provided_username,))
            rows = cur.fetchall()

            if len(rows) == 0:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText('Unknown username')
                msg.setWindowTitle("Error")
                msg.exec_()
            else:
                row = rows[0]
                user_mobile = row[5]
                user_email = row[4]
        
                print('forgot password action')
                change_password_window.username_line.setText(provided_username)
                change_password_window.show()
                self.hide()


    def sign_in(self):
        # get the data provided by user
        provided_username = self.username_line.text()
        provided_password = self.password_line.text()

        database = r"users.db"
        conn = self.create_connection(database)
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username=?", (provided_username,))
        row = cur.fetchall()[0] # we select the first row because there should be only one
        first = row[1]
        last = row[2]
        hash = row[6]
        salt = row[7]
        role = row[8]
        salted_password = provided_password+str(salt)
        ph = PasswordHasher()
        try: 
            ph.verify(hash, salted_password)
            window.user_label.setText(first+' '+last+' is logged in')
            if role == 'administrator':
                window.users_button.setEnabled(True)
            window.showMaximized()
            window.show()
            self.hide()

        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Password is incorrect')
            msg.setWindowTitle("Error")
            msg.exec_() 







    def create_connection(self,db_file):
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


class ChangePassword(QWidget):
    def __init__(self, parent=None):
        super(ChangePassword,self).__init__(parent)
        self.setupUI_password()

    def setupUI_password(self):  
        loadUi(os.path.join('src','main','python','ui','change_password.ui' ), self)  
        self.setWindowTitle('QDB change password')


if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    #window = MainWindow()
    #window.showMaximized()
    #window.show()

    # instantiate the login window and show
    login_window = login()
    login_window.show()

    window = MainWindow()
    change_password_window = ChangePassword()
    #

    exit_code = appctxt.app.exec()      # 2. Invoke appctxt.app.exec()
    sys.exit(exit_code)