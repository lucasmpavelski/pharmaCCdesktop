"""The user interface for our app"""

import os,sys
from PyQt4 import QtCore,QtGui

import pharma
from providerIndexUi import Ui_Form

class ProviderIndex (QtGui.QWidget) :
    def __init__(self,parent,task=None):
        QtGui.QWidget.__init__(self,parent)

        self.ui=Ui_Form()
        self.ui.setupUi(self)

    self.ui.provider_form.hide()

        for p in pharma.Provider.all() :
            item = self._make_QTreeWidgetItem(p)
            self.ui.provider_index.addTopLevelItem(item)

    def _make_QTreeWidgetItem (self, p) :
        item = QtGui.QTreeWidgetItem([str(p.id), p.name, p.provider, str(p.price), str(p.amount)])
        item.provider = p
        return item
 
    def _edit_on_form (self, item) :
        self.ui.provider_index.setCurrentItem(item)
        self.ui.provider_form.edit(item)

    def new (self) :
        p = pharma.Provider(0, "novo produto", "fornecedor", 0.00, 0)
        item = self._make_QTreeWidgetItem(p)

        self.ui.provider_index.addTopLevelItem(item)

        self._edit_on_form(item)

    def edit (self) :
        item = self.ui.provider_index.currentItem()
        if not item : return

        self._edit_on_form(item)

    def remove_item (self, item) :
        self.ui.provider_index.takeTopLevelItem(self.ui.provider_index.indexOfTopLevelItem(item))
        
    def remove (self) :
        item = self.ui.provider_index.currentItem()
        if not item : return
        item.provider.remove()

        self.remove_item(item)
