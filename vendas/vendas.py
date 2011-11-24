"""A custom widget that edits a task's properties"""

import sys

# Import Qt modules
from PyQt4 import QtCore,QtGui

# Import the compiled UI module
from vendasUi import Ui_MainWindow

class Main(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

    def edit(self,item):
        self.item = item
        self.ui.pid.setText(str(self.item.prov.pid))
        self.ui.product.setText(self.item.prov.product)
        self.ui.total.setText(self.item.prov.total)

        #self.ui.tags.setText(','.join( t.name for t in self.item.task.tags))
        self.show()

    def save (self) :
        self.item.prov.pid = int(unicode(self.ui.pid.text()))
        self.item.prov.product = unicode(self.ui.product.text())
        self.item.prov.total = unicode(self.ui.total.text())

        if self.item.prov.new :
            self.item.prov.save()
        else :
            self.item.prov.update()

        self.reloadRow()
        self.hide()

    def cancel (self) :
        self.item.setText(0, str(self.item.prov.pid))
        self.item.setText(1, self.item.prov.product)
        self.item.setText(2, self.item.prov.total)

        self.hide()

    def reloadRow (self) :
        pid = unicode(self.ui.pid.text())
        name = unicode(self.ui.product.text())
        phone = unicode(self.ui.total.text())

        self.item.setText(0, pid)
        self.item.setText(1, product)
        self.item.setText(2, total)

def main():
    app = QtGui.QApplication(sys.argv)
    window=Main()
    window.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
   main()
        
