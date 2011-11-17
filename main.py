# -*- coding: utf-8 -*-

"""The user interface for our app"""

import os,sys

# Import Qt modules
from PyQt4 import QtCore,QtGui

# Import the compiled UI module
from windowUi import Ui_MainWindow

# Import our backend
import pharma

# Create a class for our main window
class Main(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.editor.hide()

        for p in pharma.Provider.query('all') :
            item = QtGui.QTreeWidgetItem([str(p.pid), p.name, p.phone])
            item.prov = p
            #if task.done:
                #item.setCheckState(0,QtCore.Qt.Checked)
            #else:
                #item.setCheckState(0,QtCore.Qt.Unchecked)
            self.ui.list.addTopLevelItem(item)

    def on_list_itemChanged(self,item,column):
        if item.checkState(0):
            item.prov.done = True
        else:
            item.prov.done = False
        item.prov.save()

    def on_actionDelete_Provider_triggered(self,checked=None):
        if checked is None: return
        item = self.ui.list.currentItem()
        if not item: return

        item.prov.delete()
        #todo.saveData()
        
        self.ui.list.takeTopLevelItem(self.ui.list.indexOfTopLevelItem(item))

    def on_actionNew_Provider_triggered(self,checked=None):
       if checked is None: return
       p = pharma.Provider(0, "Nome", "Telefone")

       item = QtGui.QTreeWidgetItem([str(p.pid), p.name, p.phone])
       item.prov = p

       self.ui.list.addTopLevelItem(item)
       self.ui.list.setCurrentItem(item)
       #p.save()
       self.ui.editor.edit(item)


    def on_actionEdit_Provider_triggered(self,checked=None):
        if checked is None: return

        item = self.ui.list.currentItem()
        if not item : 
            return
        
        self.ui.editor.edit(item)


def main():
    pharma.initDB()
    
    app = QtGui.QApplication(sys.argv)
    window=Main()
    window.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
    
