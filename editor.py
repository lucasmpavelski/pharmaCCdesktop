"""A custom widget that edits a task's properties"""

import pharma

# Import Qt modules
from PyQt4 import QtCore,QtGui

# Import the compiled UI module
from editorUi import Ui_Form

class editor(QtGui.QWidget):
    def __init__(self,parent,task=None):
        QtGui.QWidget.__init__(self,parent)

        self.ui=Ui_Form()
        self.ui.setupUi(self)

    def edit(self,item):
        self.item = item
        self.ui.pid.setText(str(self.item.prov.pid))
        self.ui.name.setText(self.item.prov.name)
        self.ui.phone.setText(self.item.prov.phone)

        #self.ui.tags.setText(','.join( t.name for t in self.item.task.tags))
        self.show()

    def save (self) :
        self.item.prov.pid = unicode(self.ui.pid.text())
        self.item.prov.name = unicode(self.ui.name.text())
        self.item.prov.phone = unicode(self.ui.phone.text())

        self.item.prov.save()

        self.item.setText(0, self.item.prov.pid)
        self.item.setText(1, self.item.prov.name)
        self.item.setText(2, self.item.prov.phone)
        
