# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'providerForm.ui'
#
# Created: Sat Nov 26 21:58:31 2011
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(570, 154)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.phone = QtGui.QLineEdit(Form)
        self.phone.setObjectName("phone")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.phone)
        self.name = QtGui.QLineEdit(Form)
        self.name.setObjectName("name")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.name)
        self.id = QtGui.QLineEdit(Form)
        self.id.setObjectName("id")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.id)
        self.buttonBox = QtGui.QDialogButtonBox(Form)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.buttonBox)
        self.verticalLayout.addLayout(self.formLayout)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.id, QtCore.SIGNAL("textChanged(QString)"), Form.reloadRow)
        QtCore.QObject.connect(self.name, QtCore.SIGNAL("textChanged(QString)"), Form.reloadRow)
        QtCore.QObject.connect(self.phone, QtCore.SIGNAL("textChanged(QString)"), Form.reloadRow)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Form.save)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Form.cancel)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Codigo", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Nome", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Telefone", None, QtGui.QApplication.UnicodeUTF8))

