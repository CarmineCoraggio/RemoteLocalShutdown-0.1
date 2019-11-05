# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RemoteLR.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys, os , threading
from SocketService import SocketService
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(546, 154)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(546, 154))
        MainWindow.setMaximumSize(QtCore.QSize(546, 154))
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(350, 30))
        self.label.setScaledContents(False)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(84, 26))
        self.pushButton.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 546, 21))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuManuale = QtWidgets.QMenu(self.menuHelp)
        self.menuManuale.setObjectName("menuManuale")
        self.menuAbout = QtWidgets.QMenu(self.menuHelp)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionEsci = QtWidgets.QAction(MainWindow)
        self.actionEsci.setObjectName("actionEsci")
        self.actionGuida = QtWidgets.QAction(MainWindow)
        self.actionGuida.setObjectName("actionGuida")
        self.actionPython_Version = QtWidgets.QAction(MainWindow)
        self.actionPython_Version.setObjectName("actionPython_Version")
        self.actionPyQT_Version = QtWidgets.QAction(MainWindow)
        self.actionPyQT_Version.setObjectName("actionPyQT_Version")
        self.actionLicense = QtWidgets.QAction(MainWindow)
        self.actionLicense.setObjectName("actionLicense")
        self.menuManuale.addAction(self.actionGuida)
        self.menuAbout.addAction(self.actionPython_Version)
        self.menuAbout.addAction(self.actionPyQT_Version)
        self.menuAbout.addAction(self.actionLicense)
        self.menuHelp.addAction(self.menuManuale.menuAction())
        self.menuHelp.addAction(self.menuAbout.menuAction())
        self.menuHelp.addAction(self.actionEsci)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.tray_icon = QtWidgets.QSystemTrayIcon(MainWindow)
        self.tray_icon.setIcon(QtGui.QIcon("myicon.ico"))

        self.show_action = QtWidgets.QAction("Mostra Applicazione",MainWindow)
        self.quit_action = QtWidgets.QAction("Esci", MainWindow)
        self.hide_action = QtWidgets.QAction("Minimizza Nella Tray Icon", MainWindow)

        self.show_action.triggered.connect(MainWindow.show)
        self.hide_action.triggered.connect(MainWindow.hide)
        self.quit_action.triggered.connect(self.killshellpython)

        self.tray_menu = QtWidgets.QMenu()
        self.tray_menu.addAction(self.show_action)
        self.tray_menu.addAction(self.hide_action)
        self.tray_menu.addAction(self.quit_action)

        self.tray_icon.setContextMenu(self.tray_menu)
        self.tray_icon.show()
        

        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RemoteLocalShutdown Service..."))
        self.label.setText(_translate("MainWindow", " Serivizio per recezione Comando remoto per Reti LAN  Attiva"))
        self.label_2.setText(_translate("MainWindow", " L'indirizzi IP del Computer  '"  + str(serversocket.namehost) + 
                                                                " ' è :    " + str(serversocket.host)))
        self.pushButton.setText(_translate("MainWindow", "Riduci a Icona"))
        self.pushButton_2.setText(_translate("MainWindow", "Opzioni"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuManuale.setTitle(_translate("MainWindow", "Info"))
        self.menuAbout.setTitle(_translate("MainWindow", "About "))
        self.actionEsci.setText(_translate("MainWindow", "Esci"))
        self.actionGuida.setText(_translate("MainWindow", "Guida"))
        self.actionPython_Version.setText(_translate("MainWindow", "Python Version"))
        self.actionPyQT_Version.setText(_translate("MainWindow", "PyQT Version"))
        self.actionLicense.setText(_translate("MainWindow", "License"))

    

    def killshellpython(self):
        ### Provvisorio
        os.system('taskkill /f /im pyw.exe')

    
        
class Window(QtWidgets.QMainWindow):
    def  __init__(self, parent=None):
        super(Window, self).__init__(parent=parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.startServerSocket()


    def closeEvent(self, event):
        self.ui.tray_icon.setToolTip("Servizio RemoteShutdown Avviato")
        self.ui.tray_icon.showMessage("Servizio in esecuzione", "RemoteShutdown", QtGui.QIcon("myicon.ico"), 2000)
        event.ignore()
        self.hide()

    def startServerSocket(self):
        self.t1 = threading.Thread(target=serversocket.startsocket)
        self.t1.start()    

   

if __name__ == "__main__":
    serversocket = SocketService()
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('myicon.ico'))

    thiswindow = Window()
    thiswindow.setWindowIcon(QtGui.QIcon('myicon.ico'))
    thiswindow.show()

    sys.exit(app.exec_())

    
   
    