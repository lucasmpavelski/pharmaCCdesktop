# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'productForm.ui'
#
# Created: Sat Nov 26 20:03:33 2011
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(583, 259)
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 561, 224))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtGui.QFormLayout(self.layoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.pidLabel = QtGui.QLabel(self.layoutWidget)
        self.pidLabel.setObjectName("pidLabel")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.pidLabel)
        self.nameLabel = QtGui.QLabel(self.layoutWidget)
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.nameLabel)
        self.fornLabel = QtGui.QLabel(self.layoutWidget)
        self.fornLabel.setObjectName("fornLabel")
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.fornLabel)
        self.priceLabel = QtGui.QLabel(self.layoutWidget)
        self.priceLabel.setObjectName("priceLabel")
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.priceLabel)
        self.amountLabel = QtGui.QLabel(self.layoutWidget)
        self.amountLabel.setObjectName("amountLabel")
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.amountLabel)
        self.pidText = QtGui.QLineEdit(self.layoutWidget)
        self.pidText.setObjectName("pidText")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.pidText)
        self.nameText = QtGui.QLineEdit(self.layoutWidget)
        self.nameText.setObjectName("nameText")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.nameText)
        self.providerText = QtGui.QLineEdit(self.layoutWidget)
        self.providerText.setObjectName("providerText")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.providerText)
        self.priceText = QtGui.QLineEdit(self.layoutWidget)
        self.priceText.setObjectName("priceText")
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.priceText)
        self.amountText = QtGui.QLineEdit(self.layoutWidget)
        self.amountText.setObjectName("amountText")
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.amountText)
        self.buttonBox = QtGui.QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(10, QtGui.QFormLayout.FieldRole, self.buttonBox)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Form.cancel)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Form.save)
        QtCore.QObject.connect(self.pidText, QtCore.SIGNAL("textChanged(QString)"), Form.reloadRow)
        QtCore.QObject.connect(self.nameText, QtCore.SIGNAL("textChanged(QString)"), Form.reloadRow)
        QtCore.QObject.connect(self.providerText, QtCore.SIGNAL("textChanged(QString)"), Form.reloadRow)
        QtCore.QObject.connect(self.priceText, QtCore.SIGNAL("textChanged(QString)"), Form.reloadRow)
        QtCore.QObject.connect(self.amountText, QtCore.SIGNAL("textChanged(QString)"), Form.reloadRow)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.pidLabel.setText(QtGui.QApplication.translate("Form", "Codigo:", None, QtGui.QApplication.UnicodeUTF8))
        self.nameLabel.setText(QtGui.QApplication.translate("Form", "Nome:", None, QtGui.QApplication.UnicodeUTF8))
        self.fornLabel.setText(QtGui.QApplication.translate("Form", "Fornecedor:", None, QtGui.QApplication.UnicodeUTF8))
        self.priceLabel.setText(QtGui.QApplication.translate("Form", "Preco:", None, QtGui.QApplication.UnicodeUTF8))
        self.amountLabel.setText(QtGui.QApplication.translate("Form", "Quantidade:", None, QtGui.QApplication.UnicodeUTF8))

