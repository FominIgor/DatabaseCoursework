# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/fomin/Рабочий стол/Курсовая работа /documents.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(767, 602)
        Dialog.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(283, 7, 244, 50))
        self.label_3.setStyleSheet(" font-size:28pt; color:rgb(243, 202, 32);")
        self.label_3.setObjectName("label_3")
        self.typdoc_2 = QtWidgets.QComboBox(Dialog)
        self.typdoc_2.setGeometry(QtCore.QRect(513, 216, 210, 32))
        self.typdoc_2.setStyleSheet("font-size:15pt; \n"
"background-color: rgb(34, 34, 34);\n"
"color:rgb(243, 202, 32);")
        self.typdoc_2.setObjectName("typdoc_2")
        self.whattext = QtWidgets.QLineEdit(Dialog)
        self.whattext.setGeometry(QtCore.QRect(512, 255, 210, 32))
        self.whattext.setStyleSheet("font-size:15pt; \n"
"background-color: rgb(34, 34, 34);\n"
"color:rgb(243, 202, 32);")
        self.whattext.setText("")
        self.whattext.setObjectName("whattext")
        self.what = QtWidgets.QPushButton(Dialog)
        self.what.setGeometry(QtCore.QRect(591, 297, 72, 31))
        self.what.setStyleSheet("background-color: rgb(34, 34, 34);\n"
"font-size:14pt; color:rgb(243, 202, 32);")
        self.what.setObjectName("what")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(590, 174, 68, 32))
        self.label_9.setStyleSheet("font-size:15pt; \n"
"color:rgb(243, 202, 32);")
        self.label_9.setObjectName("label_9")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(465, 71, 20, 257))
        self.line.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(459, 71, 24, 259))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(21, 66, 487, 262))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setStyleSheet("font-size:15pt; \n"
"color:rgb(243, 202, 32);")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setStyleSheet("font-size:15pt; \n"
"color:rgb(243, 202, 32);")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.datestart = QtWidgets.QDateEdit(self.layoutWidget)
        self.datestart.setStyleSheet("font-size:15pt; \n"
"background-color: rgb(34, 34, 34);\n"
"color:rgb(243, 202, 32);")
        self.datestart.setObjectName("datestart")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.datestart)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setStyleSheet("font-size:15pt; \n"
"color:rgb(243, 202, 32);")
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.author = QtWidgets.QLineEdit(self.layoutWidget)
        self.author.setStyleSheet("font-size:15pt; \n"
"background-color: rgb(34, 34, 34);\n"
"color:rgb(243, 202, 32);")
        self.author.setText("")
        self.author.setObjectName("author")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.author)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setStyleSheet("font-size:15pt; \n"
"color:rgb(243, 202, 32);")
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.typdoc = QtWidgets.QComboBox(self.layoutWidget)
        self.typdoc.setStyleSheet("font-size:15pt; \n"
"background-color: rgb(34, 34, 34);\n"
"color:rgb(243, 202, 32);")
        self.typdoc.setObjectName("typdoc")
        self.typdoc.addItem("")
        self.typdoc.addItem("")
        self.typdoc.addItem("")
        self.typdoc.addItem("")
        self.typdoc.addItem("")
        self.typdoc.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.typdoc)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setStyleSheet("font-size:15pt; \n"
"color:rgb(243, 202, 32);")
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.statusdoc = QtWidgets.QComboBox(self.layoutWidget)
        self.statusdoc.setStyleSheet("font-size:15pt; \n"
"color:rgb(243, 202, 32);\n"
"background-color: rgb(34, 34, 34);")
        self.statusdoc.setObjectName("statusdoc")
        self.statusdoc.addItem("")
        self.statusdoc.addItem("")
        self.statusdoc.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.statusdoc)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setStyleSheet("font-size:15pt; \n"
"color:rgb(243, 202, 32);")
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.datefinish = QtWidgets.QDateEdit(self.layoutWidget)
        self.datefinish.setStyleSheet("font-size:15pt; \n"
"color:rgb(243, 202, 32);\n"
"background-color: rgb(34, 34, 34);")
        self.datefinish.setObjectName("datefinish")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.datefinish)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setStyleSheet("font-size:15pt; \n"
"color:rgb(243, 202, 32);")
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.comm = QtWidgets.QLineEdit(self.layoutWidget)
        self.comm.setStyleSheet("font-size:15pt; \n"
"color:rgb(243, 202, 32);\n"
"background-color: rgb(34, 34, 34);")
        self.comm.setObjectName("comm")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.comm)
        self.namber = QtWidgets.QLineEdit(self.layoutWidget)
        self.namber.setStyleSheet("font-size:15pt; \n"
"background-color: rgb(34, 34, 34);\n"
"color:rgb(243, 202, 32);")
        self.namber.setText("")
        self.namber.setObjectName("namber")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.namber)
        self.twStaffs = QtWidgets.QTableWidget(Dialog)
        self.twStaffs.setGeometry(QtCore.QRect(25, 331, 726, 273))
        self.twStaffs.setStyleSheet("font-size:15pt; \n"
"color:rgb(243, 202, 32);\n"
"background-color: rgb(34, 34, 34);")
        self.twStaffs.setObjectName("twStaffs")
        self.twStaffs.setColumnCount(0)
        self.twStaffs.setRowCount(0)
        self.apdate = QtWidgets.QPushButton(Dialog)
        self.apdate.setGeometry(QtCore.QRect(626, 76, 104, 31))
        self.apdate.setStyleSheet("background-color: rgb(34, 34, 34);\n"
"font-size:14pt; color:rgb(243, 202, 32);")
        self.apdate.setObjectName("apdate")
        self.open = QtWidgets.QPushButton(Dialog)
        self.open.setGeometry(QtCore.QRect(525, 76, 95, 31))
        self.open.setStyleSheet("background-color: rgb(34, 34, 34);\n"
"font-size:14pt; color:rgb(243, 202, 32);")
        self.open.setObjectName("open")
        self.dell = QtWidgets.QPushButton(Dialog)
        self.dell.setGeometry(QtCore.QRect(525, 113, 94, 31))
        self.dell.setStyleSheet("background-color: rgb(34, 34, 34);\n"
"font-size:14pt; color:rgb(243, 202, 32);")
        self.dell.setObjectName("dell")
        self.what_5 = QtWidgets.QPushButton(Dialog)
        self.what_5.setGeometry(QtCore.QRect(626, 113, 106, 31))
        self.what_5.setStyleSheet("background-color: rgb(34, 34, 34);\n"
"font-size:14pt; color:rgb(243, 202, 32);")
        self.what_5.setObjectName("what_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Документы</span></p></body></html>"))
        self.what.setText(_translate("Dialog", "Найти"))
        self.label_9.setText(_translate("Dialog", "Поиск"))
        self.label.setText(_translate("Dialog", "Номер документа"))
        self.label_2.setText(_translate("Dialog", "Дата создания"))
        self.label_4.setText(_translate("Dialog", "Автор"))
        self.label_5.setText(_translate("Dialog", "Тип документа"))
        self.typdoc.setItemText(0, _translate("Dialog", "Договор"))
        self.typdoc.setItemText(1, _translate("Dialog", "Акт выполненных работ"))
        self.typdoc.setItemText(2, _translate("Dialog", "Резюме"))
        self.typdoc.setItemText(3, _translate("Dialog", "Трудовой договор"))
        self.typdoc.setItemText(4, _translate("Dialog", "Приказ"))
        self.typdoc.setItemText(5, _translate("Dialog", "Служебная записка"))
        self.label_6.setText(_translate("Dialog", "Статус документа"))
        self.statusdoc.setItemText(0, _translate("Dialog", "В работе"))
        self.statusdoc.setItemText(1, _translate("Dialog", "В ожидании"))
        self.statusdoc.setItemText(2, _translate("Dialog", "Завершен"))
        self.label_7.setText(_translate("Dialog", "Дата выполнения"))
        self.label_8.setText(_translate("Dialog", "Комментарий"))
        self.apdate.setText(_translate("Dialog", "Добавить"))
        self.open.setText(_translate("Dialog", "Открыть"))
        self.dell.setText(_translate("Dialog", "Удалить"))
        self.what_5.setText(_translate("Dialog", "Изменить"))
