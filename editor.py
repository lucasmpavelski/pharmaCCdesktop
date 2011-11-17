"""A custom widget that edits a task's properties"""

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
        self.ui.pid.setText(str(self.item.pid))
        self.ui.name.setText(self.item.name)
        self.ui.phone.setText(self.item.phone)

        #self.ui.tags.setText(','.join( t.name for t in self.item.task.tags))
        self.show()

