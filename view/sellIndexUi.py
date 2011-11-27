# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sellIndex.ui'
#
# Created: Sun Nov 27 17:32:58 2011
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(576, 618)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.botton_new_sell = QtGui.QPushButton(Form)
        self.botton_new_sell.setObjectName("botton_new_sell")
        self.horizontalLayout.addWidget(self.botton_new_sell)
        self.button_edit_sell = QtGui.QPushButton(Form)
        self.button_edit_sell.setObjectName("button_edit_sell")
        self.horizontalLayout.addWidget(self.button_edit_sell)
        self.button_delete_sell = QtGui.QPushButton(Form)
        self.button_delete_sell.setObjectName("button_delete_sell")
        self.horizontalLayout.addWidget(self.button_delete_sell)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.sell_index = QtGui.QTreeWidget(Form)
        self.sell_index.setAnimated(False)
        self.sell_index.setObjectName("sell_index")
        self.verticalLayout.addWidget(self.sell_index)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.botton_new_sell, QtCore.SIGNAL("clicked()"), Form.new)
        QtCore.QObject.connect(self.button_edit_sell, QtCore.SIGNAL("clicked()"), Form.remove)
        QtCore.QObject.connect(self.button_delete_sell, QtCore.SIGNAL("clicked()"), Form.edit)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.botton_new_sell.setText(QtGui.QApplication.translate("Form", "Nova venda", None, QtGui.QApplication.UnicodeUTF8))
        self.button_edit_sell.setText(QtGui.QApplication.translate("Form", "Apagar venda", None, QtGui.QApplication.UnicodeUTF8))
        self.button_delete_sell.setText(QtGui.QApplication.translate("Form", "Editar venda", None, QtGui.QApplication.UnicodeUTF8))
        self.sell_index.setSortingEnabled(False)
        self.sell_index.headerItem().setText(0, QtGui.QApplication.translate("Form", "Codigo", None, QtGui.QApplication.UnicodeUTF8))
        self.sell_index.headerItem().setText(1, QtGui.QApplication.translate("Form", "Nome", None, QtGui.QApplication.UnicodeUTF8))
        self.sell_index.headerItem().setText(2, QtGui.QApplication.translate("Form", "Preco", None, QtGui.QApplication.UnicodeUTF8))

