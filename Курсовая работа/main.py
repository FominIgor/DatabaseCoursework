import sys
import sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidgetItem
from PyQt5.uic import loadUi
import io
from PIL import Image
from PyQt5.QtGui import QPixmap


db = sqlite3.connect("database coursework.db")
sql = db.cursor()



class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("login.ui",self)

        
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        
        self.logo.clicked.connect(self.loginfunction)

    def loginfunction(self):

        email=self.email.text()
        password=self.password.text()
        
        if email == "0000" and password == "0000":
            print("Вы зашли как админ")
            loginbutton=Documents()
            widget.addWidget(loginbutton)
            widget.setCurrentIndex(widget.currentIndex()+1)
        else:
            print("Неверный логин или пароль")

class Documents(QDialog):
    def __init__(self):
        super(Documents,self).__init__()
        loadUi("documents.ui",self)
        self.apdate.clicked.connect(self.insert_staff)
        self.open.clicked.connect(self.open_file)
        self.dell.clicked.connect(self.delete_staff)
        self.what.clicked.connect(self.find_for_val)
        self.conn = None
 
 
    def open_file(self):
        try:
            self.conn = sqlite3.connect('database coursework.db')
            cur = self.conn.cursor()
            data = cur.execute("select * from Документы")
            col_name = [i[0] for i in data.description]
            data_rows = data.fetchall()
        except Exception as e:
            print(f"Проблемы с подключением к БД. {e}")
            return e
        self.twStaffs.setColumnCount(len(col_name))
        self.twStaffs.setHorizontalHeaderLabels(col_name)
        self.twStaffs.setRowCount(0)
        self.typdoc_2.addItems(col_name)
        for i, row in enumerate(data_rows):
            self.twStaffs.setRowCount(self.twStaffs.rowCount() + 1)
            for j, elem in enumerate(row):
                self.twStaffs.setItem(i, j, QTableWidgetItem(str(elem)))
        self.twStaffs.resizeColumnsToContents()
        

    def update_twStaffs(self, query="select * from Документы"):
        try:
            cur = self.conn.cursor()
            data = cur.execute(query).fetchall()
        except Exception as e:
            print(f"Проблемы с подключением к БД. {e}")
            return e
        self.twStaffs.setRowCount(0)
        for i, row in enumerate(data):
            self.twStaffs.setRowCount(self.twStaffs.rowCount() + 1)
            for j, elem in enumerate(row):
                self.twStaffs.setItem(i, j, QTableWidgetItem(str(elem)))
        self.twStaffs.resizeColumnsToContents()
        

    def insert_staff(self, index):
       

        IDTypeofDocument = self.typdoc.itemData(index)
        IDdocumentstatus = self.statusdoc.itemData(index)

        try:
            cur = self.conn.cursor()
            cur.execute(f"""insert into Документы(DocumentNumber, Dateofcreation, IDauthor, IDTypeofDocument, IDdocumentstatus, Dateofcompletion, Acomment)
            values('{self.namber.text()}', '{self.datestart.text()}', '{self.author.text()}', '{IDTypeofDocument}', '{IDdocumentstatus}', '{self.datefinish.text()}', '{self.comm.text()}')""")
            db.commit()
            self.conn.commit()
            cur.close()
        except Exception as e:
            print(f"Исключение1: {e}")
            return e
        self.update_twStaffs()

    def delete_staff(self):
        row = self.twStaffs.currentRow()
        num = self.twStaffs.item(row, 0).text()
        try:
            cur = self.conn.cursor()
            cur.execute(f"delete from Документы where IDdocument = {num}")
            self.conn.commit()
            cur.close()
        except Exception as e:
            print(f"Исключение: {e}")
            return e
        self.update_twStaffs()


    def find_for_val(self):
        val = self.whattext.text()
        col = self.typdoc_2.itemText(self.typdoc_2.currentIndex())
        self.update_twStaffs(f"select * from Документы where '{col}' like '{val}'")

app=QApplication(sys.argv)
mainwindow=Login()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(800)
widget.setFixedHeight(800)
widget.show()
app.exec_()