# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'providerIndex.ui'
#
# Created: Sun Nov 27 17:32:57 2011
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(587, 694)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.splitter = QtGui.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.provider_index = QtGui.QTreeWidget(self.splitter)
        self.provider_index.setTabKeyNavigation(True)
        self.provider_index.setAlternatingRowColors(True)
        self.provider_index.setItemsExpandable(False)
        self.provider_index.setExpandsOnDoubleClick(False)
        self.provider_index.setObjectName("provider_index")
        self.provider_form = ProviderForm(self.splitter)
        self.provider_form.setObjectName("provider_form")
        self.verticalLayout.addWidget(self.splitter)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL("clicked()"), Form.new)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"), Form.remove)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), Form.edit)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("Form", "Novo Fornecedor", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Form", "Apagar Fornecedor", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "Editar Fornecedor", None, QtGui.QApplication.UnicodeUTF8))
        self.provider_index.setSortingEnabled(True)
        self.provider_index.headerItem().setText(0, QtGui.QApplication.translate("Form", "Codigo", None, QtGui.QApplication.UnicodeUTF8))
        self.provider_index.headerItem().setText(1, QtGui.QApplication.translate("Form", "Nome", None, QtGui.QApplication.UnicodeUTF8))
        self.provider_index.headerItem().setText(2, QtGui.QApplication.translate("Form", "Telefone", None, QtGui.QApplication.UnicodeUTF8))

from providerForm import ProviderForm
