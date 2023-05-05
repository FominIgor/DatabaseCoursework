import sys
import sqlite3
from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.uic import loadUi
from PyQt5.QtSql import QSqlQueryModel, QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidgetItem


class Login(QtWidgets.QDialog):
    def __init__(self):
        super(Login, self).__init__()
        uic.loadUi("login.ui", self)

        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.logo.clicked.connect(self.loginfunction)

    def loginfunction(self):
        email = self.email.text()
        password = self.password.text()

        conn = sqlite3.connect('database coursework.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM users WHERE email = ? AND password = ?', (email, password))
        user = cursor.fetchone()

        if user is not None:
            print("Вы зашли как админ")
            loginbutton = Documents()
            widget.addWidget(loginbutton)
            widget.setCurrentIndex(widget.currentIndex() + 1)
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
        self.open.clicked.connect(self.TD)
        self.what_5.clicked.connect(self.appdate)
        self.otdel.clicked.connect(self.gotootdel)
        self.client.clicked.connect(self.gotoclient)
        self.sviz.clicked.connect(self.gotosvz)
        self.conn = None
 
 
    def open_file(self):
        try:
            self.conn = sqlite3.connect('database coursework.db')
            cur = self.conn.cursor()
            data = cur.execute(f"""SELECT Документы.IDdocument ,
            Документы.DocumentNumber AS "Номер документа" , 
            Документы.Dateofcreation AS "Дата создания",
            Сотрудники.Fullname AS "Автор", ТипДокумента.
            Thenameofthetypeofdocument AS "Тип документа", 
            СтатусДокумента.Thestatusofadocument AS "Статус документа", 
            Документы.Dateofcompletion AS "Дата завершения",  
            Документы.Acomment AS "Комментарий"
FROM Документы
INNER JOIN Сотрудники ON Документы.IDauthor = Сотрудники.IDemployee
INNER JOIN ТипДокумента ON Документы.IDTypeofDocument = ТипДокумента.IDTypeofDocument
INNER JOIN СтатусДокумента ON Документы.IDdocumentstatus = СтатусДокумента.IDdocumentstatus; """)
            col_name = [i[0] for i in data.description]
            data_rows = data.fetchall()
        except Exception as e:
            print(f"Проблемы с подключением к БД. {e}")
            return e
        self.twStaffs.setColumnCount(len(col_name))
        self.twStaffs.setHorizontalHeaderLabels(col_name)
        self.twStaffs.setRowCount(0)
        for i, row in enumerate(data_rows):
            self.twStaffs.setRowCount(self.twStaffs.rowCount() + 1)
            for j, elem in enumerate(row):
                self.twStaffs.setItem(i, j, QTableWidgetItem(str(elem)))
        self.twStaffs.resizeColumnsToContents()

    def Fomin(self):
        conn = sqlite3.connect('database coursework.db')
        cursor = conn.cursor()
        typdocs = []
        for row in cursor.execute('SELECT Thenameofthetypeofdocument FROM ТипДокумента'):
            typdocs.append(row[0])
        self.typdoc.addItems(typdocs)

        statesdocs = []
        for row in cursor.execute('SELECT Thestatusofadocument FROM СтатусДокумента'):
            statesdocs.append(row[0])
        self.statusdoc.addItems(statesdocs)

        authors = []
        for row in cursor.execute('SELECT Fullname FROM Сотрудники'):
            authors.append(row[0])
        self.author.addItems(authors)

        conn.close()

    def update_twStaffs(self, query=(f"""SELECT Документы.IDdocument ,
    Документы.DocumentNumber AS "Номер документа" , 
    Документы.Dateofcreation AS "Дата создания",
    Сотрудники.Fullname AS "Автор", 
    ТипДокумента.Thenameofthetypeofdocument AS "Тип документа", 
    СтатусДокумента.Thestatusofadocument AS "Статус документа", 
    Документы.Dateofcompletion AS "Дата завершения",  
    Документы.Acomment AS "Комментарий"
FROM Документы
INNER JOIN Сотрудники ON Документы.IDauthor = Сотрудники.IDemployee
INNER JOIN ТипДокумента ON Документы.IDTypeofDocument = ТипДокумента.IDTypeofDocument
INNER JOIN СтатусДокумента ON Документы.IDdocumentstatus = СтатусДокумента.IDdocumentstatus; """)):
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
        conn = sqlite3.connect('database coursework.db')
        cursor = conn.cursor()
        typdoc = self.typdoc.currentText()
        cursor.execute('SELECT IDTypeofDocument FROM ТипДокумента WHERE Thenameofthetypeofdocument = ?', (typdoc,))
        id_typdoc_row = cursor.fetchone()
        if id_typdoc_row is not None:
            id_typdoc = id_typdoc_row[0]
        else:
            # Handle the case where the query returned no rows
            print("No rows found for IDTypeofDocument query")
            conn.close()
            return

        statusdoc = self.statusdoc.currentText()
        cursor.execute('SELECT IDdocumentstatus FROM СтатусДокумента WHERE Thestatusofadocument = ?', (statusdoc,))
        id_tytstatusdoc_row = cursor.fetchone()
        if id_tytstatusdoc_row is not None:
            id_tytstatusdoc = id_tytstatusdoc_row[0]
        else:
            # Handle the case where the query returned no rows
            print("No rows found for IDdocumentstatus query")
            conn.close()
            return

        author = self.author.currentText()
        cursor.execute('SELECT IDemployee FROM Сотрудники WHERE Fullname = ?', (author,))
        id_author_row = cursor.fetchone()
        if id_author_row is not None:
            id_author = id_author_row[0]
        else:
            # Handle the case where the query returned no rows
            print("No rows found for IDemployee query")
            conn.close()
            return

        try:
            cursor.execute("""INSERT INTO Документы(DocumentNumber, Dateofcreation, IDauthor, IDTypeofDocument, 
                IDdocumentstatus, Dateofcompletion, Acomment)
                VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (self.namber.text(), self.datestart.text(), id_author, id_typdoc, id_tytstatusdoc,
                self.datefinish.text(), self.comm.text()))
            conn.commit()
            self.update_twStaffs()
        except Exception as e:
            print(f"Исключение1: {e}")
            return e

        conn.close()


    def appdate(self):
        conn = sqlite3.connect('database coursework.db')
        cur = conn.cursor()

        typdoc = self.typdoc.currentText()
        cur.execute("SELECT IDTypeofDocument FROM ТипДокумента WHERE Thenameofthetypeofdocument = ?", (typdoc,))
        id_typdoc = cur.fetchone()[0]  # получить id выбранной записи

        tytstatusdoc = self.statusdoc.currentText()
        cur.execute("SELECT IDdocumentstatus FROM СтатусДокумента WHERE Thestatusofadocument = ?", (tytstatusdoc,))
        id_tytstatusdoc = cur.fetchone()[0]  # получить id выбранной записи

        author = self.author.currentText()
        cur.execute("SELECT IDemployee FROM Сотрудники WHERE Fullname = ?", (author,))
        id_author = cur.fetchone()[0]  # получить id выбранной записи

        # выполнить обновление данных в таблице Документы, используя id
        cur.execute("""UPDATE Документы SET DocumentNumber=?, 
        Dateofcreation=?, IDauthor=?, 
        IDTypeofDocument=?, IDdocumentstatus=?, 
        Dateofcompletion=?, Acomment=? WHERE IDdocument=?""",
                    (self.namber.text(), self.datestart.text(), id_author, id_typdoc, id_tytstatusdoc, self.datefinish.text(),
                    self.comm.text(), self.id.text()))
        conn.commit()
        conn.close()
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
    
    test = False
    def TD(self):
        
        if Documents.test == False:                                                      
            self.conn = sqlite3.connect('database coursework.db')
            cur = self.conn.cursor()
            data = cur.execute(f"SELECT * FROM Документы;")
            col_name = [i[0] for i in data.description]
            self.typdoc_2.addItems(col_name)
            Documents.test = True


    def find_for_val(self):
        val = self.whattext.text()
        col = self.typdoc_2.itemText(self.typdoc_2.currentIndex())
        self.update_twStaffs(f"""SELECT Документы.IDdocument ,
        Документы.DocumentNumber AS "Номер документа" , 
        Документы.Dateofcreation AS "Дата создания",
        Сотрудники.Fullname AS "Автор", 
        ТипДокумента.Thenameofthetypeofdocument AS "Тип документа", 
        СтатусДокумента.Thestatusofadocument AS "Статус документа", 
        Документы.Dateofcompletion AS "Дата завершения",  
        Документы.Acomment AS "Комментарий"
FROM Документы
INNER JOIN Сотрудники ON Документы.IDauthor = Сотрудники.IDemployee
INNER JOIN ТипДокумента ON Документы.IDTypeofDocument = ТипДокумента.IDTypeofDocument
INNER JOIN СтатусДокумента ON Документы.IDdocumentstatus = СтатусДокумента.IDdocumentstatus 
where {val} like {col};""")
    
    
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
        self.appdate.clicked.connect(self.apdate_slot)
        self.open.clicked.connect(self.TD)
        self.otdel.clicked.connect(self.gotootdel)
        self.docs.clicked.connect(self.gotodocs)
        self.sviz.clicked.connect(self.gotosvz)
        self.conn = None

 
    def open_file(self):
        try:
            self.conn = sqlite3.connect('database coursework.db')
            cur = self.conn.cursor()
            data = cur.execute(f"""SELECT Сотрудники.IDemployee , Сотрудники.Fullname AS "ФИО" , Должности.Jobtitle AS "Должность", Отделы.Thenameofthedepartment AS "Отдел", Сотрудники.Thedateofemployment AS "Дата трудоустройства", Сотрудники.Telephone AS "Телефон", Сотрудники.Email AS "Почта"
FROM Сотрудники
INNER JOIN Должности ON Сотрудники.IDposition = Должности.IDposition
INNER JOIN Отделы ON Сотрудники.IDofthedepartment = Отделы.IDofthedepartment; """)
            col_name = [i[0] for i in data.description]
            data_rows = data.fetchall()
        except Exception as e:
            print(f"Проблемы с подключением к БД. {e}")
            return e
        self.twStaffs.setColumnCount(len(col_name))
        self.twStaffs.setHorizontalHeaderLabels(col_name)
        self.twStaffs.setRowCount(0)
        for i, row in enumerate(data_rows):
            self.twStaffs.setRowCount(self.twStaffs.rowCount() + 1)
            for j, elem in enumerate(row):
                self.twStaffs.setItem(i, j, QTableWidgetItem(str(elem)))
        self.twStaffs.resizeColumnsToContents()


    def Fomin(self):
        conn = sqlite3.connect("database coursework.db")

        typdocs = conn.execute("SELECT Jobtitle FROM Должности").fetchall()
        self.dolg.clear()
        self.dolg.addItems([x[0] for x in typdocs])

        statesdocs = conn.execute("SELECT Thenameofthedepartment FROM Отделы").fetchall()
        self.otdels.clear()
        self.otdels.addItems([x[0] for x in statesdocs])

        conn.close()



    def update_twStaffs(self, query=(f"""SELECT Сотрудники.IDemployee , Сотрудники.Fullname AS "ФИО" , Должности.Jobtitle AS "Должность", Отделы.Thenameofthedepartment AS "Отдел", Сотрудники.Thedateofemployment AS "Дата трудоустройства", Сотрудники.Telephone AS "Телефон", Сотрудники.Email AS "Почта"
FROM Сотрудники
INNER JOIN Должности ON Сотрудники.IDposition = Должности.IDposition
INNER JOIN Отделы ON Сотрудники.IDofthedepartment = Отделы.IDofthedepartment; """)):
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
        conn = sqlite3.connect("database coursework.db")

        typdoc = self.dolg.currentText()
        id_dolgnost = conn.execute("SELECT IDposition FROM Должности WHERE Jobtitle = ?", (typdoc,)).fetchone()[0]

        tytstatusdoc = self.otdels.currentText()
        id_otdel = conn.execute("SELECT IDofthedepartment FROM Отделы WHERE Thenameofthedepartment = ?", (tytstatusdoc,)).fetchone()[0]

        try:
            cur = conn.cursor()
            cur.execute("INSERT INTO Сотрудники(Fullname, IDposition, IDofthedepartment, Thedateofemployment, Telephone, Email) VALUES (?, ?, ?, ?, ?, ?)",
                        (self.fio.text(), id_dolgnost, id_otdel, self.datestart.text(), self.phone.text(), self.mail.text()))
            conn.commit()
            cur.close()
        except Exception as e:
            print(f"Исключение1: {e}")
            return e

        self.update_twStaffs()
        conn.close()



    def apdate_slot(self):
        conn = sqlite3.connect('database coursework.db')
        cursor = conn.cursor()

        typdoc = self.dolg.currentText()
        cursor.execute("SELECT IDposition FROM Должности WHERE Jobtitle = ?", (typdoc,))
        id_dolgnost = cursor.fetchone()[0]  # получить id выбранной записи

        tytstatusdoc = self.otdels.currentText()
        cursor.execute("SELECT IDofthedepartment FROM Отделы WHERE Thenameofthedepartment = ?", (tytstatusdoc,))
        id_otdel = cursor.fetchone()[0]  # получить id выбранной записи

        # выполнить обновление данных в таблице Сотрудники, используя id
        cursor.execute("""UPDATE Сотрудники SET Fullname=?, IDposition=?, IDofthedepartment=?, Thedateofemployment=?, Telephone=?, Email=? WHERE IDemployee=?""",
                    (self.fio.text(), id_dolgnost, id_otdel, self.datestart.text(), self.phone.text(), self.mail.text(), self.id.text()))
        conn.commit()
        conn.close()
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


    test = False
    def TD(self):
        
        if Clients.test == False:                                                      
            self.conn = sqlite3.connect('database coursework.db')
            cur = self.conn.cursor()
            data = cur.execute(f"SELECT * FROM Сотрудники;")
            col_name = [i[0] for i in data.description]
            self.typdoc_2.addItems(col_name)
            Clients.test = True


    def find_for_val(self):
        val = self.whattext.text()
        col = self.typdoc_2.itemText(self.typdoc_2.currentIndex())
        self.update_twStaffs(f"select * from Сотрудники where {col} like {val};")


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
        self.what_5.clicked.connect(self.apdate_slot)
        self.open.clicked.connect(self.TD)
        self.client.clicked.connect(self.gotoclient)
        self.docs.clicked.connect(self.gotodocs)
        self.sviz.clicked.connect(self.gotosvz)
        self.conn = None
 
 
    def open_file(self):
        try:
            self.conn = sqlite3.connect('database coursework.db')
            cur = self.conn.cursor()
            data = cur.execute(f"""SELECT Отделы.IDofthedepartment , Отделы.Thenameofthedepartment AS "Название отдела" , Сотрудники.Fullname AS "Руководитель"
FROM Отделы
INNER JOIN Сотрудники ON Отделы.SotrokdnikIDBrutder = Сотрудники.IDemployee; """)
            col_name = [i[0] for i in data.description]
            data_rows = data.fetchall()
        except Exception as e:
            print(f"Проблемы с подключением к БД. {e}")
            return e
        self.twStaffs.setColumnCount(len(col_name))
        self.twStaffs.setHorizontalHeaderLabels(col_name)
        self.twStaffs.setRowCount(0)
        for i, row in enumerate(data_rows):
            self.twStaffs.setRowCount(self.twStaffs.rowCount() + 1)
            for j, elem in enumerate(row):
                self.twStaffs.setItem(i, j, QTableWidgetItem(str(elem)))
        self.twStaffs.resizeColumnsToContents()


    def Fomin(self):
        conn = sqlite3.connect('database coursework.db')
        cursor = conn.cursor()

        typdocs = []
        for row in cursor.execute('SELECT Fullname FROM Сотрудники'):
            typdocs.append(row[0])
        self.king.addItems(typdocs)

        conn.close()


    def update_twStaffs(self, query=(f"""SELECT Отделы.IDofthedepartment , Отделы.Thenameofthedepartment AS "Название отдела" , Сотрудники.Fullname AS "Руководитель"
FROM Отделы
INNER JOIN Сотрудники ON Отделы.SotrokdnikIDBrutder = Сотрудники.IDemployee; """)):
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
        conn = sqlite3.connect("database coursework.db")

        typdoc = self.king.currentText()
        query = conn.execute("SELECT IDemployee FROM Сотрудники WHERE Fullname = ?", (typdoc,))
        id_king = query.fetchone()[0]

        try:
            cur = conn.cursor()
            cur.execute("INSERT INTO Отделы(Thenameofthedepartment, SotrokdnikIDBrutder) VALUES(?, ?)", (self.name.text(), id_king))
            conn.commit()
            cur.close()
        except Exception as e:
            print(f"Исключение1: {e}")
            return e
        finally:
            conn.close()
            
        self.update_twStaffs()



    def apdate_slot(self):
        conn = sqlite3.connect("database coursework.db")

        typdoc = self.king.currentText()
        query = conn.execute("SELECT IDemployee FROM Сотрудники WHERE Fullname = ?", (typdoc,))
        row = query.fetchone()
        if row:
            id_king = row[0]  # получить id выбранной записи
        else:
            print("No results returned")
            conn.close()
            return

        # выполнить обновление данных в таблице Документы, используя id
        try:
            conn.execute("""UPDATE Отделы SET Thenameofthedepartment=?, SotrokdnikIDBrutder=? WHERE IDofthedepartment=?""",
                        (self.name.text(), id_king, self.id.text()))
            conn.commit()
        except Exception as e:
            print(f"Исключение1: {e}")
            conn.rollback()
            conn.close()
            return e

        conn.close()
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


    test = False
    def TD(self):
        
        if Otdel.test == False:                                                      
            self.conn = sqlite3.connect('database coursework.db')
            cur = self.conn.cursor()
            data = cur.execute(f"SELECT * FROM Отделы;")
            col_name = [i[0] for i in data.description]
            self.typdoc_2.addItems(col_name)
            Otdel.test = True


    def find_for_val(self):
        val = self.whattext.text()
        col = self.typdoc_2.itemText(self.typdoc_2.currentIndex())
        self.update_twStaffs(f"""SELECT Отделы.IDofthedepartment, Отделы.Thenameofthedepartment AS "Название отдела", Сотрудники.Fullname AS "Руководитель"
FROM Отделы
INNER JOIN Сотрудники ON Отделы.SotrokdnikIDBrutder = Сотрудники.IDemployee where Отделы.{col} like '{val}';""")


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
        self.open.clicked.connect(self.TD)
        self.what_5.clicked.connect(self.apdate_slot)

        self.apdate_2.clicked.connect(self.insert_staff2)
        self.open_2.clicked.connect(self.open_file2)
        self.dell_2.clicked.connect(self.delete_staff2)
        self.what_2.clicked.connect(self.find_for_val2)
        self.open_2.clicked.connect(self.Fomin2)
        self.open_2.clicked.connect(self.TD2)
        self.what_7.clicked.connect(self.apdate_slot2)


        self.otdel.clicked.connect(self.gotootdel)
        self.docs.clicked.connect(self.gotodocs)
        self.client.clicked.connect(self.gotoclient)
        self.conn = None
 
 
    def open_file(self):
        try:
            self.conn = sqlite3.connect('database coursework.db')
            cur = self.conn.cursor()
            data = cur.execute((f"""SELECT СвязанныеДокументы.IDrelateddocuments, 
       Документы1.DocumentNumber AS "Главный документ", 
       Документы2.DocumentNumber AS "Связанный документ"
FROM СвязанныеДокументы
INNER JOIN Документы Документы1 ON СвязанныеДокументы.IDdocumentSource = Документы1.IDdocument
INNER JOIN Документы Документы2 ON СвязанныеДокументы.IDofthedocumentRelated = Документы2.IDdocument;
 """))

            col_name = [i[0] for i in data.description]
            data_rows = data.fetchall()
        except Exception as e:
            print(f"Проблемы с подключением к БД. {e}")
            return e
        self.twStaffs.setColumnCount(len(col_name))
        self.twStaffs.setHorizontalHeaderLabels(col_name)
        self.twStaffs.setRowCount(0)
        for i, row in enumerate(data_rows):
            self.twStaffs.setRowCount(self.twStaffs.rowCount() + 1)
            for j, elem in enumerate(row):
                self.twStaffs.setItem(i, j, QTableWidgetItem(str(elem)))
        self.twStaffs.resizeColumnsToContents()

    def open_file2(self):
        try:
            self.conn = sqlite3.connect('database coursework.db')
            cur = self.conn.cursor()
            data = cur.execute((f"""SELECT ИсполнителиДокументов.IDexecutorsofdocuments, 
       Документы.DocumentNumber AS "Документ", 
       Сотрудники.Fullname AS "Исполнитель"
FROM ИсполнителиДокументов
INNER JOIN Документы ON ИсполнителиДокументов.IDdocument = Документы.IDdocument
INNER JOIN Сотрудники ON ИсполнителиДокументов.IDemployee = Сотрудники.IDemployee;
 """))

            col_name = [i[0] for i in data.description]
            data_rows = data.fetchall()
        except Exception as e:
            print(f"Проблемы с подключением к БД. {e}")
            return e
        self.twStaffs.setColumnCount(len(col_name))
        self.twStaffs.setHorizontalHeaderLabels(col_name)
        self.twStaffs.setRowCount(0)
        for i, row in enumerate(data_rows):
            self.twStaffs.setRowCount(self.twStaffs.rowCount() + 1)
            for j, elem in enumerate(row):
                self.twStaffs.setItem(i, j, QTableWidgetItem(str(elem)))
        self.twStaffs.resizeColumnsToContents()






    def Fomin(self):
        conn = sqlite3.connect("database coursework.db")

        cur = conn.cursor()
        cur.execute("SELECT DocumentNumber FROM Документы")
        data = cur.fetchall()

        self.docs1.clear()
        self.docs1.addItems([str(row[0]) for row in data])
        self.docs2.clear()
        self.docs2.addItems([str(row[0]) for row in data])

        cur.close()
        conn.close()


    def Fomin2(self):
        conn = sqlite3.connect("database coursework.db")

        cur = conn.cursor()
        cur.execute("SELECT DocumentNumber FROM Документы")
        data = cur.fetchall()

        self.docs3.clear()
        self.docs3.addItems([str(row[0]) for row in data])

        cur.execute("SELECT Fullname FROM Сотрудники")
        data = cur.fetchall()

        self.sotrudnic.clear()
        self.sotrudnic.addItems([str(row[0]) for row in data])

        cur.close()
        conn.close()






    def update_twStaffs(self, query=(f"""SELECT СвязанныеДокументы.IDrelateddocuments, 
       Документы1.DocumentNumber AS "Главный документ", 
       Документы2.DocumentNumber AS "Связанный документ"
FROM СвязанныеДокументы
INNER JOIN Документы Документы1 ON СвязанныеДокументы.IDdocumentSource = Документы1.IDdocument
INNER JOIN Документы Документы2 ON СвязанныеДокументы.IDofthedocumentRelated = Документы2.IDdocument;
 """)):
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


    def update_twStaffs2(self, query="""SELECT ИсполнителиДокументов.IDexecutorsofdocuments, 
       Документы.DocumentNumber AS "Документ", 
       Сотрудники.Fullname AS "Исполнитель"
FROM ИсполнителиДокументов
INNER JOIN Документы ON ИсполнителиДокументов.IDdocument = Документы.IDdocument
INNER JOIN Сотрудники ON ИсполнителиДокументов.IDemployee = Сотрудники.IDemployee;
 """):
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
        conn = sqlite3.connect("database coursework.db")

        typdoc = self.docs1.currentText()
        query = conn.execute("SELECT IDdocument FROM Документы WHERE DocumentNumber = ?", (typdoc,))
        row = query.fetchone()
        if row:
            docs2 = row[0]  # получить id выбранной записи
        else:
            print("No results returned")
            conn.close()
            return

        tytstatusdoc = self.docs2.currentText()
        query = conn.execute("SELECT IDdocument FROM Документы WHERE DocumentNumber = ?", (tytstatusdoc,))
        row = query.fetchone()
        if row:
            docs3 = row[0]  # получить id выбранной записи
        else:
            print("No results returned")
            conn.close()
            return

        # выполнить вставку в другую таблицу, используя id
        try:
            conn.execute("INSERT INTO СвязанныеДокументы(IDdocumentSource, IDofthedocumentRelated) VALUES (?, ?)",
                        (docs2, docs3))
            conn.commit()
        except Exception as e:
            print(f"Исключение1: {e}")
            conn.rollback()
            conn.close()
            return e

        conn.close()
        self.update_twStaffs()


    def insert_staff2(self):
        conn = sqlite3.connect("database coursework.db")

        typdoc = self.docs3.currentText()
        query = conn.execute("SELECT IDdocument FROM Документы WHERE DocumentNumber = ?", (typdoc,))
        row = query.fetchone()
        if row:
            docs2 = row[0]  # получить id выбранной записи
        else:
            print("No results returned")
            conn.close()
            return

        typdoc1 = self.sotrudnic.currentText()
        query = conn.execute("SELECT IDemployee FROM Сотрудники WHERE Fullname = ?", (typdoc1,))
        row = query.fetchone()
        if row:
            sotrudnic = row[0]  # получить id выбранной записи
        else:
            print("No results returned")
            conn.close()
            return

        # выполнить вставку в другую таблицу, используя id
        try:
            conn.execute("INSERT INTO ИсполнителиДокументов(IDdocument, IDemployee) VALUES (?, ?)", (docs2, sotrudnic))
            conn.commit()
        except Exception as e:
            print(f"Исключение1: {e}")
            conn.rollback()
            conn.close()
            return e

        conn.close()
        self.update_twStaffs2()


    def apdate_slot(self):
        conn = sqlite3.connect("database coursework.db")
        c = conn.cursor()

        typdoc = self.docs1.currentText()
        c.execute("SELECT IDdocument FROM Документы WHERE DocumentNumber = ?", (typdoc,))
        docs2 = c.fetchone()[0]  # получить id выбранной записи
    
        tytstatusdoc = self.docs2.currentText()
        c.execute("SELECT IDdocument FROM Документы WHERE DocumentNumber = ?", (tytstatusdoc,))
        docs3 = c.fetchone()[0]  # получить id выбранной записи

        # выполнить обновление данных в таблице Документы, используя id
        c.execute("""UPDATE СвязанныеДокументы SET IDdocumentSource=?, IDofthedocumentRelated=? WHERE IDrelateddocuments=?""", (docs2, docs3, self.id.text()))
        conn.commit()
        conn.close()
        self.update_twStaffs()


    def apdate_slot2(self):
        conn = sqlite3.connect("database coursework.db")
        c = conn.cursor()

        typdoc = self.docs3.currentText()
        c.execute("SELECT IDdocument FROM Документы WHERE DocumentNumber = ?", (typdoc,))
        docs2 = c.fetchone()[0]  # получить id выбранной записи
    
        typdoc1 = self.sotrudnic.currentText()
        c.execute("SELECT IDemployee FROM Сотрудники WHERE Fullname = ?", (typdoc1,))
        sotrudnic = c.fetchone()[0]  # получить id выбранной записи

        # выполнить обновление данных в таблице Документы, используя id
        c.execute("""UPDATE ИсполнителиДокументов SET IDdocument=?, IDemployee=? WHERE IDexecutorsofdocuments=?""", (docs2, sotrudnic, self.id_2.text()))
        conn.commit()
        conn.close()
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


    test = False
    def TD(self):
        
        if Svz.test == False:                                                      
            self.conn = sqlite3.connect('database coursework.db')
            cur = self.conn.cursor()
            data = cur.execute(f"SELECT * FROM СвязанныеДокументы;")
            col_name = [i[0] for i in data.description]
            self.typdoc_2.addItems(col_name)
            Svz.test = True


    def find_for_val(self):
        val = self.whattext.text()
        col = self.typdoc_2.itemText(self.typdoc_2.currentIndex())
        self.update_twStaffs(f"""SELECT СвязанныеДокументы.IDrelateddocuments, 
       Документы1.DocumentNumber AS "Главный документ", 
       Документы2.DocumentNumber AS "Связанный документ"
FROM СвязанныеДокументы
INNER JOIN Документы Документы1 ON СвязанныеДокументы.IDdocumentSource = Документы1.IDdocument
INNER JOIN Документы Документы2 ON СвязанныеДокументы.IDofthedocumentRelated = Документы2.IDdocument where {col} like {val}; """) 

    test2 = False
    def TD2(self):
        
        if Svz.test2 == False:                                                      
            self.conn = sqlite3.connect('database coursework.db')
            cur = self.conn.cursor()
            data = cur.execute(f"SELECT * FROM ИсполнителиДокументов;")
            col_name = [i[0] for i in data.description]
            self.typdoc_3.addItems(col_name)
            Svz.test2 = True

    def find_for_val2(self):
        val = self.whattext_2.text()
        col = self.typdoc_3.itemText(self.typdoc_3.currentIndex())
        self.update_twStaffs2(f"select * from ИсполнителиДокументов where {col} like {val};")

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