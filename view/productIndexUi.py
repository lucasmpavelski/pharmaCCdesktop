# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'productIndex.ui'
#
# Created: Sat Nov 26 20:03:32 2011
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(596, 683)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.botton_new = QtGui.QPushButton(Form)
        self.botton_new.setObjectName("botton_new")
        self.horizontalLayout.addWidget(self.botton_new)
        self.button_edit = QtGui.QPushButton(Form)
        self.button_edit.setObjectName("button_edit")
        self.horizontalLayout.addWidget(self.button_edit)
        self.button_delete = QtGui.QPushButton(Form)
        self.button_delete.setObjectName("button_delete")
        self.horizontalLayout.addWidget(self.button_delete)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.splitter = QtGui.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.product_index = QtGui.QTreeWidget(self.splitter)
        self.product_index.setTabKeyNavigation(True)
        self.product_index.setAlternatingRowColors(True)
        self.product_index.setItemsExpandable(False)
        self.product_index.setExpandsOnDoubleClick(False)
        self.product_index.setObjectName("product_index")
        self.product_form = ProductForm(self.splitter)
        self.product_form.setObjectName("product_form")
        self.verticalLayout.addWidget(self.splitter)
        self.actionNew_Product = QtGui.QAction(Form)
        self.actionNew_Product.setObjectName("actionNew_Product")

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.botton_new, QtCore.SIGNAL("clicked()"), Form.new)
        QtCore.QObject.connect(self.button_edit, QtCore.SIGNAL("clicked()"), Form.remove)
        QtCore.QObject.connect(self.button_delete, QtCore.SIGNAL("clicked()"), Form.edit)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.botton_new.setText(QtGui.QApplication.translate("Form", "Novo Produto", None, QtGui.QApplication.UnicodeUTF8))
        self.button_edit.setText(QtGui.QApplication.translate("Form", "Apagar Produto", None, QtGui.QApplication.UnicodeUTF8))
        self.button_delete.setText(QtGui.QApplication.translate("Form", "Editar Produto", None, QtGui.QApplication.UnicodeUTF8))
        self.product_index.setSortingEnabled(True)
        self.product_index.headerItem().setText(0, QtGui.QApplication.translate("Form", "Codigo", None, QtGui.QApplication.UnicodeUTF8))
        self.product_index.headerItem().setText(1, QtGui.QApplication.translate("Form", "Nome", None, QtGui.QApplication.UnicodeUTF8))
        self.product_index.headerItem().setText(2, QtGui.QApplication.translate("Form", "Forncedor", None, QtGui.QApplication.UnicodeUTF8))
        self.product_index.headerItem().setText(3, QtGui.QApplication.translate("Form", "Preco", None, QtGui.QApplication.UnicodeUTF8))
        self.product_index.headerItem().setText(4, QtGui.QApplication.translate("Form", "Quantidade", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Product.setText(QtGui.QApplication.translate("Form", "Novo produto", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Product.setShortcut(QtGui.QApplication.translate("Form", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))

from productForm import ProductForm
