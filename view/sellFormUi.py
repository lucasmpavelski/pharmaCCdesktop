#!/usr/bin/env python
# coding=UTF-8
#
# Generated by pykdeuic4 from sellForm.ui on Mon Nov 28 15:44:58 2011
#
# WARNING! All changes to this file will be lost.
from PyKDE4 import kdecore
from PyKDE4 import kdeui
from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(669, 721)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.store_products = QtGui.QTreeWidget(Form)
        self.store_products.setObjectName("store_products")
        self.verticalLayout.addWidget(self.store_products)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_5 = QtGui.QPushButton(Form)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_4 = QtGui.QPushButton(Form)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.sell_products = QtGui.QTreeWidget(Form)
        self.sell_products.setObjectName("sell_products")
        self.verticalLayout.addWidget(self.sell_products)
        self.pushButton_6 = QtGui.QPushButton(Form)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL("clicked()"), Form.add)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL("clicked()"), Form.remove)
        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL("clicked()"), Form.save)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(kdecore.i18n("Form"))
        self.store_products.headerItem().setText(0, kdecore.i18n("Codigo"))
        self.store_products.headerItem().setText(1, kdecore.i18n("Nome"))
        self.store_products.headerItem().setText(2, kdecore.i18n("Preco"))
        self.store_products.headerItem().setText(3, kdecore.i18n("Quantidade"))
        self.pushButton_5.setText(kdecore.i18n("Adicionar Produto"))
        self.pushButton_4.setText(kdecore.i18n("Remover Produto"))
        self.sell_products.headerItem().setText(0, kdecore.i18n("Codigo"))
        self.sell_products.headerItem().setText(1, kdecore.i18n("Nome"))
        self.sell_products.headerItem().setText(2, kdecore.i18n("Preco"))
        self.pushButton_6.setText(kdecore.i18n("Concluir Venda"))

