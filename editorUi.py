# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editor.ui'
#
# Created: Thu Nov 24 13:39:24 2011
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(401, 209)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pidLabel = QtGui.QLabel(Form)
        self.pidLabel.setObjectName("pidLabel")
        self.verticalLayout.addWidget(self.pidLabel)
        self.pid = QtGui.QLineEdit(Form)
        self.pid.setObjectName("pid")
        self.verticalLayout.addWidget(self.pid)
        self.nameLabel = QtGui.QLabel(Form)
        self.nameLabel.setObjectName("nameLabel")
        self.verticalLayout.addWidget(self.nameLabel)
        self.name = QtGui.QLineEdit(Form)
        self.name.setObjectName("name")
        self.verticalLayout.addWidget(self.name)
        self.phoneLabel = QtGui.QLabel(Form)
        self.phoneLabel.setObjectName("phoneLabel")
        self.verticalLayout.addWidget(self.phoneLabel)
        self.phone = QtGui.QLineEdit(Form)
        self.phone.setObjectName("phone")
        self.verticalLayout.addWidget(self.phone)
        self.buttonBox = QtGui.QDialogButtonBox(Form)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.actionEdit_provider = QtGui.QAction(Form)
        self.actionEdit_provider.setObjectName("actionEdit_provider")

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Form.save)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Form.cancel)
        QtCore.QObject.connect(self.pid, QtCore.SIGNAL("textChanged(QString)"), Form.reloadRow)
        QtCore.QObject.connect(self.name, QtCore.SIGNAL("textChanged(QString)"), Form.reloadRow)
        QtCore.QObject.connect(self.phone, QtCore.SIGNAL("textChanged(QString)"), Form.reloadRow)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.pidLabel.setText(QtGui.QApplication.translate("Form", "ID:", None, QtGui.QApplication.UnicodeUTF8))
        self.nameLabel.setText(QtGui.QApplication.translate("Form", "Nome:", None, QtGui.QApplication.UnicodeUTF8))
        self.phoneLabel.setText(QtGui.QApplication.translate("Form", "Telefone:", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEdit_provider.setText(QtGui.QApplication.translate("Form", "Edit_provider", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEdit_provider.setToolTip(QtGui.QApplication.translate("Form", "Editar fornecedor", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEdit_provider.setShortcut(QtGui.QApplication.translate("Form", "Ctrl+E", None, QtGui.QApplication.UnicodeUTF8))

