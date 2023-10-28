from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QWidget, QTabWidget,QVBoxLayout, QStatusBar
import sys
import os
import sqlite3


class MainWindow(QWidget):

     def __init__(self):
        super().__init__()

        self.tabs = QTabWidget()
        self.companies_tab = QWidget()
        self.lines_tab = QWidget()
        self.points_tab = QWidget()
        self.foldmap_tab = QWidget()

        self.tabs.addTab(self.companies_tab,"Companies")


        self.statusbar = QStatusBar(self)
        self.statusbar.showMessage('Ready', 10000)
        self.main_vlayout = QVBoxLayout()
        self.main_vlayout = QVBoxLayout()
        self.main_vlayout.addWidget(self.tabs)
        self.main_vlayout.addWidget(self.statusbar)
        self.setLayout(self.main_vlayout)




if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = MainWindow()
    window.showMaximized()
    window.show()
    exit_code = appctxt.app.exec()      # 2. Invoke appctxt.app.exec()
    sys.exit(exit_code)