"""The user interface for our app"""

import os,sys
from PyQt4 import QtCore,QtGui

import pharma
from sellIndexUi import Ui_Form

class SellIndex (QtGui.QWidget) :
    def __init__(self,parent,task=None):
        QtGui.QWidget.__init__(self,parent)

        self.ui=Ui_Form()
        self.ui.setupUi(self)

        for s in pharma.Sell.get_all() :
            item = self._make_QTreeWidgetItem(s)
            self.ui.sell_index.addTopLevelItem(item)

    def _make_QTreeWidgetItem (self, s) :
        products = s.products()
        prod_items = []
        total = 0.0
        for p in products :
          prod_items.append(QtGui.QTreeWidgetItem([str(p.id), p.name, str(p.price)]))
          total = total + p.price
        item = QtGui.QTreeWidgetItem([str(s.id), "", str(total)])
        item.addChildren(prod_items)
        item.sell = s
        return item
 
    def _edit_on_form (self, item) :
        pass
	#self.ui.product_index.setCurrentItem(item)
	#self.ui.product_form.edit(item)

    def new (self) :
        pass
	#p = pharma.Product("novo produto", 0, 0.00, 0)
	#item = self._make_QTreeWidgetItem(p)

	#self.ui.product_index.addTopLevelItem(item)

	#self._edit_on_form(item)

    def edit (self) :
        pass
	#item = self.ui.product_index.currentItem()
	#if not item : return

	#self._edit_on_form(item)

    def remove_item (self, item) :
        pass
	#self.ui.product_index.takeTopLevelItem(self.ui.product_index.indexOfTopLevelItem(item))
    
    def remove (self) :
        pass
        #item = self.ui.product_index.currentItem()
        #if not item : return
        #item.product.remove()
        
        #self.remove_item(item)
