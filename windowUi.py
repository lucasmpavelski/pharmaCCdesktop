# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created: Thu Nov 17 20:52:39 2011
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(402, 496)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.list = QtGui.QTreeWidget(self.splitter)
        self.list.setTabKeyNavigation(True)
        self.list.setAlternatingRowColors(True)
        self.list.setItemsExpandable(False)
        self.list.setExpandsOnDoubleClick(False)
        self.list.setObjectName("list")
        self.editor = editor(self.splitter)
        self.editor.setObjectName("editor")
        self.verticalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 402, 25))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea(QtCore.Qt.TopToolBarArea), self.toolBar)
        self.actionDelete_Provider = QtGui.QAction(MainWindow)
        self.actionDelete_Provider.setObjectName("actionDelete_Provider")
        self.actionNew_Provider = QtGui.QAction(MainWindow)
        self.actionNew_Provider.setObjectName("actionNew_Provider")
        self.actionEdit_Provider = QtGui.QAction(MainWindow)
        self.actionEdit_Provider.setObjectName("actionEdit_Provider")
        self.menuMenu.addAction(self.actionNew_Provider)
        self.menuMenu.addAction(self.actionDelete_Provider)
        self.menuMenu.addAction(self.actionEdit_Provider)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.toolBar.addAction(self.actionNew_Provider)
        self.toolBar.addAction(self.actionDelete_Provider)
        self.toolBar.addAction(self.actionEdit_Provider)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.list, QtCore.SIGNAL("itemSelectionChanged()"), self.editor.hide)
        QtCore.QObject.connect(self.list, QtCore.SIGNAL("itemDoubleClicked(QTreeWidgetItem*,int)"), self.editor.edit)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "PharmaCC", None, QtGui.QApplication.UnicodeUTF8))
        self.list.setSortingEnabled(True)
        self.list.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Id", None, QtGui.QApplication.UnicodeUTF8))
        self.list.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "Nome", None, QtGui.QApplication.UnicodeUTF8))
        self.list.headerItem().setText(2, QtGui.QApplication.translate("MainWindow", "Telefone", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMenu.setTitle(QtGui.QApplication.translate("MainWindow", "menu", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete_Provider.setText(QtGui.QApplication.translate("MainWindow", "Apagar fornecedor", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete_Provider.setToolTip(QtGui.QApplication.translate("MainWindow", "Apaga o fornecedor selecionado", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete_Provider.setShortcut(QtGui.QApplication.translate("MainWindow", "Del", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Provider.setText(QtGui.QApplication.translate("MainWindow", "Novo fornecedor", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Provider.setToolTip(QtGui.QApplication.translate("MainWindow", "Cadastrar novo fornecedor", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Provider.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEdit_Provider.setText(QtGui.QApplication.translate("MainWindow", "Editar fornecedor", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEdit_Provider.setToolTip(QtGui.QApplication.translate("MainWindow", "Editar fornecedor selecionado", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEdit_Provider.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+E", None, QtGui.QApplication.UnicodeUTF8))

from editor import editor
