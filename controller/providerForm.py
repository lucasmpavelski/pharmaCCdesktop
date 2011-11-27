# Import Qt modules
from PyQt4 import QtCore,QtGui

# Import the compiled UI module
from providerFormUi import Ui_Form

class ProviderForm (QtGui.QWidget) :
    def __init__(self,parent,task=None):
        QtGui.QWidget.__init__(self,parent)

        self.ui=Ui_Form()
        self.ui.setupUi(self)

    def edit(self,item):
        self.item = item
        self.ui.id.setText(str(self.item.provider.id))
        self.ui.name.setText(self.item.provider.name)
        self.ui.phone.setText(self.item.provider.phone)

        #self.ui.tags.setText(','.join( t.name for t in self.item.task.tags))
        self.show()

    def save (self) :
        #self.item.provider.id = int(unicode(self.ui.id.text()))
        self.item.provider.name = unicode(self.ui.name.text())
        self.item.provider.phone = unicode(self.ui.phone.text())

        if self.item.provider.new :
            self.item.provider.save()
        else :
            self.item.provider.update()

        self.reloadRow()
        self.hide()

    def cancel (self) :
        self.item.setText(0, str(self.item.provider.id))
        self.item.setText(1, self.item.provider.name)
        self.item.setText(2, self.item.provider.phone)

        self.hide()

    def reloadRow (self) :
        pid = unicode(self.ui.id.text())
        name = unicode(self.ui.name.text())
        phone = unicode(self.ui.phone.text())

        self.item.setText(0, pid)
        self.item.setText(1, name)
        self.item.setText(2, phone)
        
