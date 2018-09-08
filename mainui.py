# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(656, 380)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(240, 110, 160, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(260, 10, 141, 21))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 656, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuConfigura_es = QtWidgets.QMenu(self.menuBar)
        self.menuConfigura_es.setObjectName("menuConfigura_es")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionClient_IDs_e_API_Keys = QtWidgets.QAction(MainWindow)
        self.actionClient_IDs_e_API_Keys.setObjectName("actionClient_IDs_e_API_Keys")
        self.menuConfigura_es.addAction(self.actionClient_IDs_e_API_Keys)
        self.menuBar.addAction(self.menuConfigura_es.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Spotify Youtube Downloader!"))
        self.menuConfigura_es.setTitle(_translate("MainWindow", "Configurações"))
        self.actionClient_IDs_e_API_Keys.setText(_translate("MainWindow", "Client IDs e API Keys"))

