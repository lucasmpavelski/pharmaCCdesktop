"""The user interface for our app"""

import os,sys

from PyQt4 import QtCore,QtGui

from productIndexUi import Ui_Form

class ProductIndex (QtGui.QWidget) :
    def __init__(self,parent,task=None):
        QtGui.QWidget.__init__(self,parent)

        self.ui=Ui_Form()
        self.ui.setupUi(self)
