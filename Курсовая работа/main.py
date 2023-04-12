import sys
import sqlite3
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtSql import QSqlQueryModel, QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidgetItem


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
        self.open.clicked.connect(self.Fomin)
        self.otdel.clicked.connect(self.gotootdel)
        self.client.clicked.connect(self.gotoclient)
        self.sviz.clicked.connect(self.gotosvz)
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


    def Fomin(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("database coursework.db")
        db.open()

        typdocs = QSqlQueryModel()
        typdocs.setQuery("SELECT Thenameofthetypeofdocument FROM ТипДокумента", db)
        self.typdoc.setModel(typdocs)
        self.typdoc.setModelColumn(0)

        statesdocs = QSqlQueryModel()
        statesdocs.setQuery("SELECT Thestatusofadocument FROM СтатусДокумента", db)
        self.statusdoc.setModel(statesdocs)
        self.statusdoc.setModelColumn(0)

        authors = QSqlQueryModel()
        authors.setQuery("SELECT Fullname FROM Сотрудники", db)
        self.author.setModel(authors)
        self.author.setModelColumn(0)


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
        

    def insert_staff(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("database coursework.db")
        db.open()

        typdoc = self.typdoc.currentText()
        query = QSqlQuery(db) 
        query.prepare("SELECT IDTypeofDocument FROM ТипДокумента WHERE Thenameofthetypeofdocument = :name")
        query.bindValue(":name", typdoc)
        query.exec_()
        query.next()
        id_typdoc = query.value(0)  # получить id выбранной записи
   
        tytstatusdoc = self.statusdoc.currentText()
        query = QSqlQuery(db)
        query.prepare("SELECT IDdocumentstatus FROM СтатусДокумента WHERE Thestatusofadocument = :name")
        query.bindValue(":name", tytstatusdoc)
        query.exec_()
        query.next()
        id_tytstatusdoc = query.value(0)  # получить id выбранной записи

        author = self.author.currentText()
        query = QSqlQuery(db)
        query.prepare("SELECT IDemployee FROM Сотрудники WHERE Fullname = :name")
        query.bindValue(":name", author)
        query.exec_()
        query.next()
        id_author = query.value(0)  # получить id выбранной записи

        # выполнить вставку в другую таблицу, используя id
        try:
            cur = self.conn.cursor()
            cur.execute(f"""insert into Документы(DocumentNumber, Dateofcreation, IDauthor, IDTypeofDocument, IDdocumentstatus, Dateofcompletion, Acomment)
            values('{self.namber.text()}', '{self.datestart.text()}', '{id_author}', '{id_typdoc}', '{id_tytstatusdoc}', '{self.datefinish.text()}', '{self.comm.text()}')""")
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
        self.update_twStaffs(f"select * from Документы where '{col}' like '{val}';")
    
    
    def gotoclient(self):
        client=Clients()
        widget.addWidget(client)
        widget.setCurrentIndex(widget.currentIndex()+1)


    def gotootdel(self):
        otdel=Otdel()
        widget.addWidget(otdel)
        widget.setCurrentIndex(widget.currentIndex()+1)


    def gotosvz(self):
        sviz=Svz()
        widget.addWidget(sviz)
        widget.setCurrentIndex(widget.currentIndex()+1)


class Clients(QDialog):
    def __init__(self):
        super(Clients,self).__init__()
        loadUi("client.ui",self)
        self.apdate.clicked.connect(self.insert_staff)
        self.open.clicked.connect(self.open_file)
        self.dell.clicked.connect(self.delete_staff)
        self.what.clicked.connect(self.find_for_val)
        self.open.clicked.connect(self.Fomin)
        self.otdel.clicked.connect(self.gotootdel)
        self.docs.clicked.connect(self.gotodocs)
        self.sviz.clicked.connect(self.gotosvz)
        self.conn = None
 
 
    def open_file(self):
        try:
            self.conn = sqlite3.connect('database coursework.db')
            cur = self.conn.cursor()
            data = cur.execute("select * from Сотрудники")
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


    def Fomin(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("database coursework.db")
        db.open()

        typdocs = QSqlQueryModel()
        typdocs.setQuery("SELECT Jobtitle FROM Должности", db)
        self.dolg.setModel(typdocs)
        self.dolg.setModelColumn(0)

        statesdocs = QSqlQueryModel()
        statesdocs.setQuery("SELECT Thenameofthedepartment FROM Отделы", db)
        self.otdels.setModel(statesdocs)
        self.otdels.setModelColumn(0)



    def update_twStaffs(self, query="select * from Сотрудники"):
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
        

    def insert_staff(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("database coursework.db")
        db.open()

        typdoc = self.dolg.currentText()
        query = QSqlQuery(db) 
        query.prepare("SELECT IDposition FROM Должности WHERE Jobtitle = :name")
        query.bindValue(":name", typdoc)
        query.exec_()
        query.next()
        id_dolgnost = query.value(0)  # получить id выбранной записи
   
        tytstatusdoc = self.otdels.currentText()
        query = QSqlQuery(db)
        query.prepare("SELECT IDofthedepartment FROM Отделы WHERE Thenameofthedepartment = :name")
        query.bindValue(":name", tytstatusdoc)
        query.exec_()
        query.next()
        id_otdel = query.value(0)  # получить id выбранной записи


        # выполнить вставку в другую таблицу, используя id
        try:
            cur = self.conn.cursor()
            cur.execute(f"""insert into Сотрудники(Fullname, IDposition, IDofthedepartment, Thedateofemployment, Telephone, Email)
            values('{self.fio.text()}', '{id_dolgnost}', '{id_otdel}','{self.datestart.text()}','{self.phone.text()}', '{self.mail.text()}')""")
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
            cur.execute(f"delete from Сотрудники where IDemployee = {num}")
            self.conn.commit()
            cur.close()
        except Exception as e:
            print(f"Исключение: {e}")
            return e
        self.update_twStaffs()


    def find_for_val(self):
        val = self.whattext.text()
        col = self.typdoc_2.itemText(self.typdoc_2.currentIndex())
        self.update_twStaffs(f"select * from Сотрудники where '{col}' like '{val}';")


    def gotodocs(self):
        docs=Documents()
        widget.addWidget(docs)
        widget.setCurrentIndex(widget.currentIndex()+1)


    def gotootdel(self):
        otdel=Otdel()
        widget.addWidget(otdel)
        widget.setCurrentIndex(widget.currentIndex()+1)


    def gotosvz(self):
        sviz=Svz()
        widget.addWidget(sviz)
        widget.setCurrentIndex(widget.currentIndex()+1)


class Otdel(QDialog):
    def __init__(self):
        super(Otdel,self).__init__()
        loadUi("otdel.ui",self)
        self.apdate.clicked.connect(self.insert_staff)
        self.open.clicked.connect(self.open_file)
        self.dell.clicked.connect(self.delete_staff)
        self.what.clicked.connect(self.find_for_val)
        self.open.clicked.connect(self.Fomin)
        self.client.clicked.connect(self.gotoclient)
        self.docs.clicked.connect(self.gotodocs)
        self.sviz.clicked.connect(self.gotosvz)
        self.conn = None
 
 
    def open_file(self):
        try:
            self.conn = sqlite3.connect('database coursework.db')
            cur = self.conn.cursor()
            data = cur.execute("select * from Отделы")
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


    def Fomin(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("database coursework.db")
        db.open()

        typdocs = QSqlQueryModel()
        typdocs.setQuery("SELECT Fullname FROM Сотрудники", db)
        self.king.setModel(typdocs)
        self.king.setModelColumn(0)


    def update_twStaffs(self, query="select * from Отделы"):
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
        

    def insert_staff(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("database coursework.db")
        db.open()

        typdoc = self.king.currentText()
        query = QSqlQuery(db) 
        query.prepare("SELECT IDemployee FROM Сотрудники WHERE Fullname = :name")
        query.bindValue(":name", typdoc)
        query.exec_()
        query.next()
        id_king = query.value(0)  # получить id выбранной записи
   

        # выполнить вставку в другую таблицу, используя id
        try:
            cur = self.conn.cursor()
            cur.execute(f"""insert into Отделы(Thenameofthedepartment, SotrokdnikIDBrutder)
            values('{self.name.text()}', '{id_king}')""")
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
            cur.execute(f"delete from Отделы where IDofthedepartment = {num}")
            self.conn.commit()
            cur.close()
        except Exception as e:
            print(f"Исключение: {e}")
            return e
        self.update_twStaffs()


    def find_for_val(self):
        val = self.whattext.text()
        col = self.typdoc_2.itemText(self.typdoc_2.currentIndex())
        self.update_twStaffs(f"select * from Отделы where '{col}' like '{val}';")


    def gotodocs(self):
        docs=Documents()
        widget.addWidget(docs)
        widget.setCurrentIndex(widget.currentIndex()+1)


    def gotoclient(self):
        client=Clients()
        widget.addWidget(client)
        widget.setCurrentIndex(widget.currentIndex()+1)


    def gotosvz(self):
        sviz=Svz()
        widget.addWidget(sviz)
        widget.setCurrentIndex(widget.currentIndex()+1)


class Svz(QDialog):
    def __init__(self):
        super(Svz,self).__init__()
        loadUi("svz_ispoln.ui",self)
        self.apdate.clicked.connect(self.insert_staff)
        self.open.clicked.connect(self.open_file)
        self.dell.clicked.connect(self.delete_staff)
        self.what.clicked.connect(self.find_for_val)
        self.open.clicked.connect(self.Fomin)

        self.apdate_2.clicked.connect(self.insert_staff2)
        self.open_2.clicked.connect(self.open_file2)
        self.dell_2.clicked.connect(self.delete_staff2)
        self.what_2.clicked.connect(self.find_for_val2)
        self.open_2.clicked.connect(self.Fomin2)


        self.otdel.clicked.connect(self.gotootdel)
        self.docs.clicked.connect(self.gotodocs)
        self.client.clicked.connect(self.gotoclient)
        self.conn = None
 
 
    def open_file(self):
        try:
            self.conn = sqlite3.connect('database coursework.db')
            cur = self.conn.cursor()
            data = cur.execute("select * from СвязанныеДокументы")
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

    def open_file2(self):
        try:
            self.conn = sqlite3.connect('database coursework.db')
            cur = self.conn.cursor()
            data = cur.execute("select * from ИсполнителиДокументов")
            col_name = [i[0] for i in data.description]
            data_rows = data.fetchall()
        except Exception as e:
            print(f"Проблемы с подключением к БД. {e}")
            return e
        self.twStaffs.setColumnCount(len(col_name))
        self.twStaffs.setHorizontalHeaderLabels(col_name)
        self.twStaffs.setRowCount(0)
        self.typdoc_3.addItems(col_name)
        for i, row in enumerate(data_rows):
            self.twStaffs.setRowCount(self.twStaffs.rowCount() + 1)
            for j, elem in enumerate(row):
                self.twStaffs.setItem(i, j, QTableWidgetItem(str(elem)))
        self.twStaffs.resizeColumnsToContents()


    def Fomin(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("database coursework.db")
        db.open()

        typdocs = QSqlQueryModel()
        typdocs.setQuery("SELECT DocumentNumber FROM Документы", db)
        self.docs1.setModel(typdocs)
        self.docs1.setModelColumn(0)

        typdocs = QSqlQueryModel()
        typdocs.setQuery("SELECT DocumentNumber FROM Документы", db)
        self.docs2.setModel(typdocs)
        self.docs2.setModelColumn(0)


    def Fomin2(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("database coursework.db")
        db.open()

        typdocs = QSqlQueryModel()
        typdocs.setQuery("SELECT DocumentNumber FROM Документы", db)
        self.docs3.setModel(typdocs)
        self.docs3.setModelColumn(0)

        typdocs = QSqlQueryModel()
        typdocs.setQuery("SELECT Fullname FROM Сотрудники", db)
        self.sotrudnic.setModel(typdocs)
        self.sotrudnic.setModelColumn(0)


    def update_twStaffs(self, query="select * from СвязанныеДокументы"):
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


    def update_twStaffs2(self, query="select * from ИсполнителиДокументов"):
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
        

    def insert_staff(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("database coursework.db")
        db.open()

        typdoc = self.docs1.currentText()
        query = QSqlQuery(db) 
        query.prepare("SELECT IDdocument FROM Документы WHERE DocumentNumber = :name")
        query.bindValue(":name", typdoc)
        query.exec_()
        query.next()
        docs2 = query.value(0)  # получить id выбранной записи
   
        tytstatusdoc = self.docs2.currentText()
        query = QSqlQuery(db)
        query.prepare("SELECT IDdocument FROM Документы WHERE DocumentNumber = :name")
        query.bindValue(":name", tytstatusdoc)
        query.exec_()
        query.next()
        docs3 = query.value(0)  # получить id выбранной записи


        # выполнить вставку в другую таблицу, используя id
        try:
            cur = self.conn.cursor()
            cur.execute(f"""insert into СвязанныеДокументы(IDdocumentSource, IDofthedocumentRelated)
            values('{docs2}', '{docs3}')""")
            db.commit()
            self.conn.commit()
            cur.close()
        except Exception as e:
            print(f"Исключение1: {e}")
            return e
        self.update_twStaffs()


    def insert_staff2(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("database coursework.db")
        db.open()

        typdoc = self.docs3.currentText()
        query = QSqlQuery(db) 
        query.prepare("SELECT IDdocument FROM Документы WHERE DocumentNumber = :name")
        query.bindValue(":name", typdoc)
        query.exec_()
        query.next()
        docs2 = query.value(0)  # получить id выбранной записи
   
        typdoc1 = self.sotrudnic.currentText()
        query = QSqlQuery(db) 
        query.prepare("SELECT IDemployee FROM Сотрудники WHERE Fullname = :name")
        query.bindValue(":name", typdoc1)
        query.exec_()
        query.next()
        sotrudnic = query.value(0)  # получить id выбранной записи


        # выполнить вставку в другую таблицу, используя id
        try:
            cur = self.conn.cursor()
            cur.execute(f"""insert into ИсполнителиДокументов(IDdocument, IDemployee)
            values('{docs2}', '{sotrudnic}')""")
            db.commit()
            self.conn.commit()
            cur.close()
        except Exception as e:
            print(f"Исключение1: {e}")
            return e
        self.update_twStaffs2()


    def delete_staff(self):
        row = self.twStaffs.currentRow()
        num = self.twStaffs.item(row, 0).text()
        try:
            cur = self.conn.cursor()
            cur.execute(f"delete from СвязанныеДокументы where IDrelateddocuments = {num}")
            self.conn.commit()
            cur.close()
        except Exception as e:
            print(f"Исключение: {e}")
            return e
        self.update_twStaffs()


    def delete_staff2(self):
        row = self.twStaffs.currentRow()
        num = self.twStaffs.item(row, 0).text()
        try:
            cur = self.conn.cursor()
            cur.execute(f"delete from ИсполнителиДокументов where IDexecutorsofdocuments = {num}")
            self.conn.commit()
            cur.close()
        except Exception as e:
            print(f"Исключение: {e}")
            return e
        self.update_twStaffs2()


    def find_for_val(self):
        val = self.whattext.text()
        col = self.typdoc_2.itemText(self.typdoc_2.currentIndex())
        self.update_twStaffs(f"select * from СвязанныеДокументы where '{col}' like '{val}';")


    def find_for_val2(self):
        val = self.whattext_2.text()
        col = self.typdoc_3.itemText(self.typdoc_3.currentIndex())
        self.update_twStaffs2(f"select * from ИсполнителиДокументов where '{col}' like '{val}';")

    def gotodocs(self):
        docs=Documents()
        widget.addWidget(docs)
        widget.setCurrentIndex(widget.currentIndex()+1)


    def gotootdel(self):
        otdel=Otdel()
        widget.addWidget(otdel)
        widget.setCurrentIndex(widget.currentIndex()+1)


    def gotoclient(self):
        client=Clients()
        widget.addWidget(client)
        widget.setCurrentIndex(widget.currentIndex()+1)


app=QApplication(sys.argv)
mainwindow=Login()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(800)
widget.setFixedHeight(650)
widget.show()
app.exec_()