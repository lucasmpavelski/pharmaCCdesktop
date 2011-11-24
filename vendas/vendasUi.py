# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vendas.ui'
#
# Created: Thu Nov 24 14:58:46 2011
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 496)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_new_sell = QtGui.QPushButton(self.centralwidget)
        self.button_new_sell.setGeometry(QtCore.QRect(10, 10, 93, 27))
        self.button_new_sell.setObjectName("button_new_sell")
        self.button_edit_sell = QtGui.QPushButton(self.centralwidget)
        self.button_edit_sell.setGeometry(QtCore.QRect(220, 10, 93, 27))
        self.button_edit_sell.setObjectName("button_edit_sell")
        self.button_delete_sell = QtGui.QPushButton(self.centralwidget)
        self.button_delete_sell.setGeometry(QtCore.QRect(110, 10, 101, 27))
        self.button_delete_sell.setObjectName("button_delete_sell")
        self.grid_sells = QtGui.QTreeWidget(self.centralwidget)
        self.grid_sells.setGeometry(QtCore.QRect(10, 50, 301, 341))
        self.grid_sells.setObjectName("grid_sells")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 23))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea(QtCore.Qt.TopToolBarArea), self.toolBar)
        self.actionNova_Venda = QtGui.QAction(MainWindow)
        self.actionNova_Venda.setObjectName("actionNova_Venda")
        self.actionExcluir_Venda = QtGui.QAction(MainWindow)
        self.actionExcluir_Venda.setObjectName("actionExcluir_Venda")
        self.actionEditar_Venda = QtGui.QAction(MainWindow)
        self.actionEditar_Venda.setObjectName("actionEditar_Venda")
        self.menuMenu.addAction(self.actionNova_Venda)
        self.menuMenu.addAction(self.actionExcluir_Venda)
        self.menuMenu.addAction(self.actionEditar_Venda)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.button_new_sell.setText(QtGui.QApplication.translate("MainWindow", "Nova Venda", None, QtGui.QApplication.UnicodeUTF8))
        self.button_edit_sell.setText(QtGui.QApplication.translate("MainWindow", "Editar Venda", None, QtGui.QApplication.UnicodeUTF8))
        self.button_delete_sell.setText(QtGui.QApplication.translate("MainWindow", "Excluir Venda", None, QtGui.QApplication.UnicodeUTF8))
        self.grid_sells.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "ID", None, QtGui.QApplication.UnicodeUTF8))
        self.grid_sells.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "Numero de produtos", None, QtGui.QApplication.UnicodeUTF8))
        self.grid_sells.headerItem().setText(2, QtGui.QApplication.translate("MainWindow", "Total", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMenu.setTitle(QtGui.QApplication.translate("MainWindow", "menu", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNova_Venda.setText(QtGui.QApplication.translate("MainWindow", "Nova Venda", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExcluir_Venda.setText(QtGui.QApplication.translate("MainWindow", "Excluir Venda", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEditar_Venda.setText(QtGui.QApplication.translate("MainWindow", "Editar Venda", None, QtGui.QApplication.UnicodeUTF8))

