from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QWidget, QTabWidget,QVBoxLayout, QStatusBar,QHBoxLayout, QVBoxLayout, QGroupBox, QTableWidget,QTableWidgetItem,QHeaderView
import sys
import os
import sqlite3


# declare global variables here




class MainWindow(QWidget):

     def __init__(self):
        super().__init__()

        self.tabs = QTabWidget()
        self.companies_tab = QWidget()
        self.lines_tab = QWidget()
        self.points_tab = QWidget()
        self.foldmap_tab = QWidget()

        self.tabs.addTab(self.companies_tab,"Companies")
        self.companies_tab_layout = QHBoxLayout()

        self.companies_left_widget = QWidget()
        self.companies_left_widget.setMaximumWidth(300)
        self.companies_left_widget.setMinimumWidth(200)
        self.companies_left_layout = QVBoxLayout()
        self.companies_left_widget.setLayout(self.companies_left_layout)

        self.companies_right_widget = QWidget()
        self.companies_right_widget.setMaximumWidth(300)
        self.companies_right_widget.setMinimumWidth(200)
        self.companies_right_layout = QVBoxLayout()
        self.companies_right_widget.setLayout(self.companies_right_layout)

        self.companies_center_widget = QWidget()
        self.companies_center_layout = QVBoxLayout()
        self.companies_center_widget.setLayout(self.companies_center_layout)

        self.companies_groupbox = QGroupBox("Companies")
        self.companies_center_layout.addWidget(self.companies_groupbox)

        self.tableWidget = QTableWidget() 
        self.tableWidget.setRowCount(4)  
        self.tableWidget.setColumnCount(2)   
  
        self.tableWidget.setItem(0,0, QTableWidgetItem("Name")) 
        self.tableWidget.setItem(0,1, QTableWidgetItem("City")) 
        self.tableWidget.setItem(1,0, QTableWidgetItem("Aloysius")) 
        self.tableWidget.setItem(1,1, QTableWidgetItem("Indore")) 
        self.tableWidget.setItem(2,0, QTableWidgetItem("Alan")) 
        self.tableWidget.setItem(2,1, QTableWidgetItem("Bhopal")) 
        self.tableWidget.setItem(3,0, QTableWidgetItem("Arnavi")) 
        self.tableWidget.setItem(3,1, QTableWidgetItem("Mandsaur")) 

        self.companies_groupbox_layout = QVBoxLayout()
        self.companies_groupbox_layout.addWidget(self.tableWidget)
        self.companies_groupbox.setLayout(self.companies_groupbox_layout)
        

   
        #Table will fit the screen horizontally 
        self.tableWidget.horizontalHeader().setStretchLastSection(True) 
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) 

        self.companies_topright_groupbox = QGroupBox("Top right")
        self.companies_bottomright_groupbox = QGroupBox("Bottom right")
        self.companies_right_layout.addWidget(self.companies_topright_groupbox)
        self.companies_right_layout.addWidget(self.companies_bottomright_groupbox)

        self.companies_topleft_groupbox = QGroupBox("Top left")
        self.companies_bottomleft_groupbox = QGroupBox("Bottom left")
        self.companies_left_layout.addWidget(self.companies_topleft_groupbox)
        self.companies_left_layout.addWidget(self.companies_bottomleft_groupbox)


        self.companies_tab_layout.addWidget(self.companies_left_widget)
        self.companies_tab_layout.addWidget(self.companies_center_widget)
        self.companies_tab_layout.addWidget(self.companies_right_widget)
        self.companies_tab.setLayout(self.companies_tab_layout)


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