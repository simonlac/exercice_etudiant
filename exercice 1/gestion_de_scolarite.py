# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gestion_scolaire.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 585)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.afficheeleve = QtWidgets.QTextBrowser(self.centralwidget)
        self.afficheeleve.setGeometry(QtCore.QRect(90, 340, 256, 192))
        self.afficheeleve.setObjectName("afficheeleve")
        self.btvalidation = QtWidgets.QPushButton(self.centralwidget)
        self.btvalidation.setGeometry(QtCore.QRect(90, 242, 131, 61))
        self.btvalidation.setObjectName("btvalidation")
        self.linenom = QtWidgets.QLineEdit(self.centralwidget)
        self.linenom.setGeometry(QtCore.QRect(90, 180, 221, 41))
        self.linenom.setObjectName("linenom")
        self.linenb = QtWidgets.QLineEdit(self.centralwidget)
        self.linenb.setGeometry(QtCore.QRect(90, 80, 221, 41))
        self.linenb.setObjectName("linenb")
        self.lbnom = QtWidgets.QLabel(self.centralwidget)
        self.lbnom.setGeometry(QtCore.QRect(90, 150, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbnom.setFont(font)
        self.lbnom.setObjectName("lbnom")
        self.lbnb = QtWidgets.QLabel(self.centralwidget)
        self.lbnb.setGeometry(QtCore.QRect(90, 40, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbnb.setFont(font)
        self.lbnb.setObjectName("lbnb")
        self.lberreur = QtWidgets.QLabel(self.centralwidget)
        self.lberreur.setGeometry(QtCore.QRect(340, 60, 171, 161))
        self.lberreur.setText("")
        self.lberreur.setObjectName("lberreur")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(260, 240, 131, 51))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btvalidation.setText(_translate("MainWindow", "Ajouter"))
        self.lbnom.setText(_translate("MainWindow", "Nom de l\'étudiant(e)"))
        self.lbnb.setText(_translate("MainWindow", "Numéro de l\'étudiant(e)"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Programmation"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Infrastructure"))
        self.comboBox.setItemText(2, _translate("MainWindow", "outil et carrière"))
