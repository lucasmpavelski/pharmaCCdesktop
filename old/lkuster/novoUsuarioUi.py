# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'novoUsuario.ui'
#
# Created by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(267, 444)
        self.lNome = QtGui.QLabel(Form)
        self.lNome.setGeometry(QtCore.QRect(10, 0, 55, 16))
        self.lNome.setObjectName("lNome")
        self.lRG = QtGui.QLabel(Form)
        self.lRG.setGeometry(QtCore.QRect(10, 50, 55, 16))
        self.lRG.setObjectName("lRG")
        self.lCPF = QtGui.QLabel(Form)
        self.lCPF.setGeometry(QtCore.QRect(10, 100, 55, 16))
        self.lCPF.setObjectName("lCPF")
        self.lTelefone = QtGui.QLabel(Form)
        self.lTelefone.setGeometry(QtCore.QRect(10, 150, 55, 16))
        self.lTelefone.setObjectName("lTelefone")
        self.lPrivilegio = QtGui.QLabel(Form)
        self.lPrivilegio.setGeometry(QtCore.QRect(10, 200, 55, 16))
        self.lPrivilegio.setObjectName("lPrivilegio")
        self.lUsuario = QtGui.QLabel(Form)
        self.lUsuario.setGeometry(QtCore.QRect(10, 250, 55, 16))
        self.lUsuario.setObjectName("lUsuario")
        self.lSenha = QtGui.QLabel(Form)
        self.lSenha.setGeometry(QtCore.QRect(10, 300, 55, 16))
        self.lSenha.setObjectName("lSenha")
        self.lConfirmar = QtGui.QLabel(Form)
        self.lConfirmar.setGeometry(QtCore.QRect(10, 350, 55, 16))
        self.lConfirmar.setObjectName("lConfirmar")
        self.leNome = QtGui.QLineEdit(Form)
        self.leNome.setGeometry(QtCore.QRect(10, 20, 241, 26))
        self.leNome.setObjectName("leNome")
        self.leRG = QtGui.QLineEdit(Form)
        self.leRG.setGeometry(QtCore.QRect(10, 70, 241, 26))
        self.leRG.setObjectName("leRG")
        self.leCPF = QtGui.QLineEdit(Form)
        self.leCPF.setGeometry(QtCore.QRect(10, 120, 241, 26))
        self.leCPF.setObjectName("leCPF")
        self.leTelefone = QtGui.QLineEdit(Form)
        self.leTelefone.setGeometry(QtCore.QRect(10, 170, 241, 26))
        self.leTelefone.setObjectName("leTelefone")
        self.ptePrivilegio = QtGui.QPlainTextEdit(Form)
        self.ptePrivilegio.setGeometry(QtCore.QRect(10, 220, 111, 21))
        self.ptePrivilegio.setObjectName("ptePrivilegio")
        self.leUsuario = QtGui.QLineEdit(Form)
        self.leUsuario.setGeometry(QtCore.QRect(10, 270, 241, 26))
        self.leUsuario.setObjectName("leUsuario")
        self.leSenha = QtGui.QLineEdit(Form)
        self.leSenha.setGeometry(QtCore.QRect(10, 320, 241, 26))
        self.leSenha.setObjectName("leSenha")
        self.leConfirmar = QtGui.QLineEdit(Form)
        self.leConfirmar.setGeometry(QtCore.QRect(10, 370, 241, 26))
        self.leConfirmar.setObjectName("leConfirmar")
        self.bbCancelarOK = QtGui.QDialogButtonBox(Form)
        self.bbCancelarOK.setGeometry(QtCore.QRect(70, 410, 176, 27))
        self.bbCancelarOK.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.bbCancelarOK.setObjectName("bbCancelarOK")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.lNome.setText(QtGui.QApplication.translate("Form", "Nome", None, QtGui.QApplication.UnicodeUTF8))
        self.lRG.setText(QtGui.QApplication.translate("Form", "RG", None, QtGui.QApplication.UnicodeUTF8))
        self.lCPF.setText(QtGui.QApplication.translate("Form", "CPF", None, QtGui.QApplication.UnicodeUTF8))
        self.lTelefone.setText(QtGui.QApplication.translate("Form", "Telefone", None, QtGui.QApplication.UnicodeUTF8))
        self.lPrivilegio.setText(QtGui.QApplication.translate("Form", "Privilégio", None, QtGui.QApplication.UnicodeUTF8))
        self.lUsuario.setText(QtGui.QApplication.translate("Form", "Usuário", None, QtGui.QApplication.UnicodeUTF8))
        self.lSenha.setText(QtGui.QApplication.translate("Form", "Senha", None, QtGui.QApplication.UnicodeUTF8))
        self.lConfirmar.setText(QtGui.QApplication.translate("Form", "Confirmar senha", None, QtGui.QApplication.UnicodeUTF8))
        self.ptePrivilegio.setPlainText(QtGui.QApplication.translate("Form", "Administrador\n"
"Atendente", None, QtGui.QApplication.UnicodeUTF8))

