# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sellsForm.ui'
#
# Created: Sun Nov 27 15:43:43 2011
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(669, 721)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.sells_form_top = QtGui.QTreeWidget(Form)
        self.sells_form_top.setObjectName("sells_form_top")
        self.verticalLayout.addWidget(self.sells_form_top)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_5 = QtGui.QPushButton(Form)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_4 = QtGui.QPushButton(Form)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.sells_form_button = QtGui.QTreeWidget(Form)
        self.sells_form_button.setObjectName("sells_form_button")
        self.verticalLayout.addWidget(self.sells_form_button)
        self.pushButton_6 = QtGui.QPushButton(Form)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL("clicked()"), Form.add)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL("clicked()"), Form.remove)
        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL("clicked()"), Form.save)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.sells_form_top.headerItem().setText(0, QtGui.QApplication.translate("Form", "Codigo", None, QtGui.QApplication.UnicodeUTF8))
        self.sells_form_top.headerItem().setText(1, QtGui.QApplication.translate("Form", "Nome", None, QtGui.QApplication.UnicodeUTF8))
        self.sells_form_top.headerItem().setText(2, QtGui.QApplication.translate("Form", "Preco", None, QtGui.QApplication.UnicodeUTF8))
        self.sells_form_top.headerItem().setText(3, QtGui.QApplication.translate("Form", "Quantidade", None, QtGui.QApplication.UnicodeUTF8))
        self.sells_form_top.headerItem().setText(4, QtGui.QApplication.translate("Form", "Total", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("Form", "Adicionar Produto", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("Form", "Remover Produto", None, QtGui.QApplication.UnicodeUTF8))
        self.sells_form_button.headerItem().setText(0, QtGui.QApplication.translate("Form", "Codigo", None, QtGui.QApplication.UnicodeUTF8))
        self.sells_form_button.headerItem().setText(1, QtGui.QApplication.translate("Form", "Nome", None, QtGui.QApplication.UnicodeUTF8))
        self.sells_form_button.headerItem().setText(2, QtGui.QApplication.translate("Form", "Preco", None, QtGui.QApplication.UnicodeUTF8))
        self.sells_form_button.headerItem().setText(3, QtGui.QApplication.translate("Form", "Quantidade", None, QtGui.QApplication.UnicodeUTF8))
        self.sells_form_button.headerItem().setText(4, QtGui.QApplication.translate("Form", "Total", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_6.setText(QtGui.QApplication.translate("Form", "Concluir Venda", None, QtGui.QApplication.UnicodeUTF8))

