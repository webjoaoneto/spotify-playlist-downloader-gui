# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Iniciar(object):
    def setupUi(self, Iniciar):
        Iniciar.setObjectName("Iniciar")
        Iniciar.resize(802, 487)
        self.centralWidget = QtWidgets.QWidget(Iniciar)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 171, 21))
        self.label.setObjectName("label")
        self.textUrlSpotify = QtWidgets.QLineEdit(self.centralWidget)
        self.textUrlSpotify.setGeometry(QtCore.QRect(180, 10, 401, 21))
        self.textUrlSpotify.setObjectName("textUrlSpotify")
        self.btnBuscar = QtWidgets.QPushButton(self.centralWidget)
        self.btnBuscar.setGeometry(QtCore.QRect(590, 10, 51, 23))
        self.btnBuscar.setObjectName("btnBuscar")
        self.tabelaResultados = QtWidgets.QTableView(self.centralWidget)
        self.tabelaResultados.setGeometry(QtCore.QRect(10, 50, 781, 301))
        self.tabelaResultados.setObjectName("tabelaResultados")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(10, 360, 101, 16))
        self.label_2.setObjectName("label_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 380, 531, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.diretorio = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.diretorio.setObjectName("diretorio")
        self.horizontalLayout.addWidget(self.diretorio)
        self.btnEscolherDiretorio = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnEscolherDiretorio.setObjectName("btnEscolherDiretorio")
        self.horizontalLayout.addWidget(self.btnEscolherDiretorio)
        self.btnProcessar = QtWidgets.QPushButton(self.centralWidget)
        self.btnProcessar.setGeometry(QtCore.QRect(700, 380, 91, 31))
        self.btnProcessar.setObjectName("btnProcessar")
        self.btnLimpar = QtWidgets.QPushButton(self.centralWidget)
        self.btnLimpar.setGeometry(QtCore.QRect(600, 380, 75, 23))
        self.btnLimpar.setObjectName("btnLimpar")
        Iniciar.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(Iniciar)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 802, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuConfigura_es = QtWidgets.QMenu(self.menuBar)
        self.menuConfigura_es.setObjectName("menuConfigura_es")
        Iniciar.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(Iniciar)
        self.mainToolBar.setObjectName("mainToolBar")
        Iniciar.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(Iniciar)
        self.statusBar.setObjectName("statusBar")
        Iniciar.setStatusBar(self.statusBar)
        self.actionClient_IDs_e_API_Keys = QtWidgets.QAction(Iniciar)
        self.actionClient_IDs_e_API_Keys.setObjectName("actionClient_IDs_e_API_Keys")
        self.menuConfigura_es.addAction(self.actionClient_IDs_e_API_Keys)
        self.menuBar.addAction(self.menuConfigura_es.menuAction())

        self.retranslateUi(Iniciar)
        QtCore.QMetaObject.connectSlotsByName(Iniciar)

    def retranslateUi(self, Iniciar):
        _translate = QtCore.QCoreApplication.translate
        Iniciar.setWindowTitle(_translate("Iniciar", "Spotify Youtube Downloader"))
        self.label.setText(_translate("Iniciar", "Informe a URL do Spotify (Playlist)"))
        self.btnBuscar.setText(_translate("Iniciar", "Buscar"))
        self.label_2.setText(_translate("Iniciar", "Salvar no diretório:"))
        self.btnEscolherDiretorio.setText(_translate("Iniciar", "Selecionar"))
        self.btnProcessar.setText(_translate("Iniciar", "Processar fila"))
        self.btnLimpar.setText(_translate("Iniciar", "Limpar"))
        self.menuConfigura_es.setTitle(_translate("Iniciar", "Configurações"))
        self.actionClient_IDs_e_API_Keys.setText(_translate("Iniciar", "Client IDs e API Keys"))

