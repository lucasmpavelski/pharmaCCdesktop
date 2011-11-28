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

        self.refresh()

    def _make_QTreeWidgetItem (self, s) :
        prods = s.products()
        prod_items = []
        total = 0.0
        for p in prods :
          pitem = QtGui.QTreeWidgetItem([str(p.id), p.name, str(p.price)])
          pitem.sold_product = pharma.SoldProduct.where("id_prod_sold_prod == " + str(p.id) + " and " +
                                                        "id_sell_sold_prod == " + str(s.id))[0]
          prod_items.append(pitem)
          total = total + p.price
        item = QtGui.QTreeWidgetItem([str(s.id), "", str(total)])
        item.addChildren(prod_items)
        item.sell = s
        return item

    def refresh (self) :
        print "yey"
        si = self.ui.sell_index
        for i in range(si.topLevelItemCount()) :
             si.takeTopLevelItem(0)
        #.takeChildren()
        for s in pharma.Sell.get_all() :
            item = self._make_QTreeWidgetItem(s)
            self.ui.sell_index.addTopLevelItem(item)
 
    def _edit_on_form (self, item) :
        pass
	#self.ui.sell_index.setCurrentItem(item)
	#self.ui.sell_form.edit(item)

    def new (self) :
        pass
	#p = pharma.Product("novo produto", 0, 0.00, 0)
	#item = self._make_QTreeWidgetItem(p)

	#self.ui.sell_index.addTopLevelItem(item)

	#self._edit_on_form(item)

    def edit (self) :
        pass
	#item = self.ui.sell_index.currentItem()
	#if not item : return

	#self._edit_on_form(item)

    def remove_item (self, item) :
	self.ui.sell_index.takeTopLevelItem(self.ui.sell_index.indexOfTopLevelItem(item))
    
    def remove (self) :
        item = self.ui.sell_index.currentItem()
        if not item : return

        if item.childCount() > 0 :
          item.sell.remove()
          item.sell.remove_products()        
          self.remove_item(item)
        else :
          item.sold_product.remove()
          itemp = item.parent()
          itemp.takeChild(itemp.indexOfChild(item))
