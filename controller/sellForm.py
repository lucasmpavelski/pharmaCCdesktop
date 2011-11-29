from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import SIGNAL

from sellFormUi import Ui_Form

import pharma

class SellForm (QtGui.QWidget) :
    def __init__(self,parent,task=None):
        QtGui.QWidget.__init__(self,parent)

        self.ui=Ui_Form()
        self.ui.setupUi(self)

        for p in pharma.Product.get_all() :
          self.ui.store_products.addTopLevelItem(self._make_QTreeStoreProduct(p))

	self.sell = pharma.Sell()
        self.sell.nproducts = 0

    def _make_QTreeStoreProduct (self, p) :
	item = QtGui.QTreeWidgetItem([str(p.id), p.name,str(p.price), str(p.amount)])
	item.product = p
	return item

    def _make_QTreeSellProduct (self, p) :
	item = QtGui.QTreeWidgetItem([str(p.id), p.name, str(p.price)])
	sp = pharma.SoldProduct(p.id, self.sell.id)
        sp.id = sp.id + self.sell.nproducts
	item.sold_product = sp
        print "item " + str(sp.id) + " " + str(sp.prod)+ " "  + str(sp.sell)
	return item

    def sell_changed(self) :
	print "sell changed!"
	self.emit(SIGNAL("sell_changed()"))

    def save (self) :
	sp = self.ui.sell_products
	if (sp.topLevelItemCount() <= 0) : return

	self.sell.save()
	for i in range(sp.topLevelItemCount()) :
	    it = sp.topLevelItem(i)
	    sold_prod = it.sold_product
	    sold_prod.save()
	
	self.sell = pharma.Sell()
	self.sell_changed()

    def add (self) :
        item = self.ui.store_products.currentItem()
        if not item : return

        prod = item.product
        self.ui.sell_products.addTopLevelItem(self._make_QTreeSellProduct(prod))
        self.sell.nproducts = self.sell.nproducts + 1

    def remove (self) :
        item = self.ui.sell_products.currentItem()
        if not item : return

	self.ui.sell_products.takeTopLevelItem(self.ui.sell_products.indexOfTopLevelItem(item))
