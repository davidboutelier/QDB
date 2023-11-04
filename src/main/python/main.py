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

import sys
import os


# declare global variables here
company_filter = False

# create the Main Window as a base widget



class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()

        self.setWindowTitle('PyQt QTabWidget')

        main_layout = QVBoxLayout(self)
        self.setLayout(main_layout)

        tabs = QTabWidget()
        main_layout.addWidget(tabs)

        self.statusbar = QStatusBar(self)
        self.statusbar.showMessage('Ready', 10000)
        main_layout.addWidget(self.statusbar)

        companies_tab = QWidget()
        companies_tab_layout = QHBoxLayout()
        companies_tab.setLayout(companies_tab_layout)
        tabs.addTab(companies_tab,"Companies")

        contacts_tab = QWidget()
        contacts_tab_layout = QHBoxLayout()
        contacts_tab.setLayout(contacts_tab_layout)
        tabs.addTab(contacts_tab,"Contacts")

        #companies_left_widget = QWidget()
        #companies_left_widget.setMaximumWidth(300)
        #companies_left_widget.setMinimumWidth(200)
        #companies_left_layout = QVBoxLayout()
        #companies_left_widget.setLayout(companies_left_layout)
        #companies_tab_layout.addWidget(companies_left_widget)

        companies_center_widget = QWidget()
        companies_center_widget.setMinimumWidth(200)
        companies_center_layout = QVBoxLayout()
        companies_center_widget.setLayout(companies_center_layout)
        companies_tab_layout.addWidget(companies_center_widget)

        companies_right_widget = QWidget()
        companies_right_widget.setMaximumWidth(300)
        companies_right_widget.setMinimumWidth(200)
        companies_right_layout = QVBoxLayout()
        companies_right_widget.setLayout(companies_right_layout)
        companies_tab_layout.addWidget(companies_right_widget)

        #companies_topleft_groupbox = QGroupBox("Top left")
        #companies_bottomleft_groupbox = QGroupBox("Bottom left")
        #companies_left_layout.addWidget(companies_topleft_groupbox)
        #companies_left_layout.addWidget(companies_bottomleft_groupbox)

        companies_topcenter_groupbox = QGroupBox("Top center")
        companies_bottomcenter_groupbox = QGroupBox("Bottom center")
        companies_center_layout.addWidget(companies_topcenter_groupbox)
        companies_center_layout.addWidget(companies_bottomcenter_groupbox)

        companies_topright_groupbox = QGroupBox("Top right")
        companies_bottomright_groupbox = QGroupBox("Bottom right")
        companies_right_layout.addWidget(companies_topright_groupbox)
        companies_right_layout.addWidget(companies_bottomright_groupbox)

        # populate the topcenter

        companies_topcenter_groupbox_layout =QVBoxLayout()
        companies_topcenter_groupbox.setLayout(companies_topcenter_groupbox_layout)

        if not self.createConnection():
            sys.exit(1)

        self.model = QSqlTableModel(self)
        self.model.setTable("companies")
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        
        if company_filter:
            text = 'Orka'
            self.model.setFilter("name = '%s'" % text)
        self.model.select()
        self.companies_view = QTableView()
        self.companies_view.setModel(self.model)
        self.companies_view.resizeColumnsToContents()

        selection_companies_model = self.companies_view.selectionModel()
        selection_companies_model.selectionChanged.connect(self.on_companies_selectionChanged)

        companies_topcenter_groupbox_layout.addWidget(self.companies_view)

        companies_bottomcenter_groupbox_layout = QHBoxLayout()
        companies_bottomcenter_groupbox.setLayout(companies_bottomcenter_groupbox_layout)

        self.companies_filter_checkbox = QCheckBox('Filter the companies ')
        self.companies_filter_checkbox.setChecked(False)

        companies_filter_label = QLabel('Field: ')
        self.companies_filter_field_list = QComboBox()
        self.companies_filter_field_list.addItems(['name','website', 'suite','street','city','state','postcode','country','market', 'ticker','email','phone','geothermal'])

        companies_filter_label_value = QLabel('Value: ')
        self.companies_filter_value_textbox = QLineEdit()


        companies_bottomcenter_groupbox_layout.addWidget(self.companies_filter_checkbox)
        companies_bottomcenter_groupbox_layout.addWidget(companies_filter_label)
        companies_bottomcenter_groupbox_layout.addWidget(self.companies_filter_field_list)
        companies_bottomcenter_groupbox_layout.addWidget(companies_filter_label_value)
        companies_bottomcenter_groupbox_layout.addWidget(self.companies_filter_value_textbox)
        companies_bottomcenter_groupbox_layout.addStretch()

        # populate a list of contacts in topright
        companies_topright_groupbox_layout = QVBoxLayout()
        companies_topright_groupbox.setLayout(companies_topright_groupbox_layout)
        self.associated_contacts_list = QListWidget()
        companies_topright_groupbox_layout.addWidget(self.associated_contacts_list)

    def execute_read_query(connection, query):
        cursor = connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except :
            print(f"The error occurred")


    def on_companies_selectionChanged(self, selected):
        self.associated_contacts_list.clear()
        if len(selected) == 1:
            for ix in selected.indexes():
                selected_company_id = str(self.companies_view.currentIndex().siblingAtColumn(0).data())

                print(selected_company_id)

                query = QSqlQuery("SELECT firstname, lastname FROM contacts WHERE company_ID ='"+selected_company_id+"'")

                while query.next():
                    first = query.value(0)
                    last = query.value(1)
                    fullname= first+" "+last
                    
                    print(first, last)
                    self.associated_contacts_list.addItem(fullname)
                
                
                









    def createConnection(self):
        con = QSqlDatabase.addDatabase("QSQLITE")
        con.setDatabaseName("DB.db")
        if not con.open():
            QMessageBox.critical(None, "Error!","Database Error: %s" % con.lastError().databaseText(),)
            return False
        return True





if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = MainWindow()
    window.showMaximized()
    window.show()

    exit_code = appctxt.app.exec()      # 2. Invoke appctxt.app.exec()
    sys.exit(exit_code)