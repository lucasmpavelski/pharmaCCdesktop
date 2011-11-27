# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sellsIndex.ui'
#
# Created: Sun Nov 27 15:43:43 2011
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(634, 564)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.sells_index = QtGui.QTreeWidget(Form)
        self.sells_index.setAnimated(False)
        self.sells_index.setObjectName("sells_index")
        self.verticalLayout.addWidget(self.sells_index)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.sells_index.setSortingEnabled(False)
        self.sells_index.headerItem().setText(0, QtGui.QApplication.translate("Form", "Codigo", None, QtGui.QApplication.UnicodeUTF8))
        self.sells_index.headerItem().setText(1, QtGui.QApplication.translate("Form", "Quantidade", None, QtGui.QApplication.UnicodeUTF8))
        self.sells_index.headerItem().setText(2, QtGui.QApplication.translate("Form", "Total", None, QtGui.QApplication.UnicodeUTF8))

