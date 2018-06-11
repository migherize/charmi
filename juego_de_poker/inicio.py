# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inicio.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PokerCharmi(object):
    def setupUi(self, PokerCharmi):
        PokerCharmi.setObjectName("PokerCharmi")
        PokerCharmi.resize(1078, 718)
        PokerCharmi.setStyleSheet("background-color: rgb(76, 76, 113);")
        self.centralwidget = QtWidgets.QWidget(PokerCharmi)
        self.centralwidget.setObjectName("centralwidget")
        self.fondo = QtWidgets.QLabel(self.centralwidget)
        self.fondo.setGeometry(QtCore.QRect(90, 0, 1171, 681))
        self.fondo.setStyleSheet("border-image: url(:/fondo/fondo.jpg);")
        self.fondo.setObjectName("fondo")
        self.titulo = QtWidgets.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(340, 0, 591, 41))
        self.titulo.setObjectName("titulo")
        self.btn_jugar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_jugar.setGeometry(QtCore.QRect(520, 150, 121, 41))
        self.btn_jugar.setStyleSheet("background-color: rgb(149, 0, 0);")
        self.btn_jugar.setObjectName("btn_jugar")
        self.btn_salir = QtWidgets.QPushButton(self.centralwidget)
        self.btn_salir.setGeometry(QtCore.QRect(690, 150, 121, 41))
        self.btn_salir.setStyleSheet("background-color: rgb(149, 0, 0);")
        self.btn_salir.setObjectName("btn_salir")
        self.usuario = QtWidgets.QLineEdit(self.centralwidget)
        self.usuario.setGeometry(QtCore.QRect(680, 90, 141, 31))
        self.usuario.setObjectName("usuario")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(510, 90, 141, 31))
        self.label.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.label.setObjectName("label")
        PokerCharmi.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PokerCharmi)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1078, 27))
        self.menubar.setObjectName("menubar")
        PokerCharmi.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PokerCharmi)
        self.statusbar.setObjectName("statusbar")
        PokerCharmi.setStatusBar(self.statusbar)

        self.retranslateUi(PokerCharmi)
        QtCore.QMetaObject.connectSlotsByName(PokerCharmi)

    def retranslateUi(self, PokerCharmi):
        _translate = QtCore.QCoreApplication.translate
        PokerCharmi.setWindowTitle(_translate("PokerCharmi", "MainWindow"))
        self.fondo.setText(_translate("PokerCharmi", "TextLabel"))
        self.titulo.setText(_translate("PokerCharmi", "<html><head/><body><p><span style=\" font-size:24pt; color:#ff5500;\">VAMOS A JUGAR POKER CON CHARMI</span></p><p><br/></p></body></html>"))
        self.btn_jugar.setText(_translate("PokerCharmi", "JUGAR"))
        self.btn_salir.setText(_translate("PokerCharmi", "SALIR"))
        self.label.setText(_translate("PokerCharmi", "<html><head/><body><p><span style=\" font-size:12pt;\">Escribe tu nombre</span></p></body></html>"))

import fondo_portada_rc
