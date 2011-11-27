"""The user interface for our app"""

import os,sys
from PyQt4 import QtCore,QtGui

import pharma
from productIndexUi import Ui_Form

class ProductIndex (QtGui.QWidget) :
    def __init__(self,parent,task=None):
        QtGui.QWidget.__init__(self,parent)

        self.ui=Ui_Form()
        self.ui.setupUi(self)

	self.ui.product_form.hide()

        for p in pharma.Product.get_all() :
            item = self._make_QTreeWidgetItem(p)
            self.ui.product_index.addTopLevelItem(item)

    def _make_QTreeWidgetItem (self, p) :
        pr = pharma.Provider.find(p.provider)
        item = QtGui.QTreeWidgetItem([str(p.id), p.name, pr['name_prov'], str(p.price), str(p.amount)])
        item.product = p
        return item
 
    def _edit_on_form (self, item) :
	self.ui.product_index.setCurrentItem(item)
	self.ui.product_form.edit(item)

    def new (self) :
	p = pharma.Product("novo produto", 0, 0.00, 0)
	item = self._make_QTreeWidgetItem(p)

	self.ui.product_index.addTopLevelItem(item)

	self._edit_on_form(item)

    def edit (self) :
	item = self.ui.product_index.currentItem()
	if not item : return

	self._edit_on_form(item)

    def remove_item (self, item) :
	self.ui.product_index.takeTopLevelItem(self.ui.product_index.indexOfTopLevelItem(item))
    
    def remove (self) :
        item = self.ui.product_index.currentItem()
        if not item : return
        item.product.remove()
        
        self.remove_item(item)
