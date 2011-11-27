# Import Qt modules
from PyQt4 import QtCore,QtGui

# Import the compiled UI module
from productFormUi import Ui_Form

class ProductForm (QtGui.QWidget) :
    def __init__(self,parent,task=None):
        QtGui.QWidget.__init__(self,parent)

        self.ui=Ui_Form()
        self.ui.setupUi(self)

    def edit(self,item):
        self.item = item
        self.ui.pidText.setText(str(self.item.product.id))
        self.ui.nameText.setText(self.item.product.name)
        self.ui.providerText.setText(self.item.product.provider)
        self.ui.priceText.setText(str(self.item.product.price))
        self.ui.amountText.setText(str(self.item.product.amount))

        #self.ui.tags.setText(','.join( t.name for t in self.item.task.tags))
        self.show()

    def save (self) :
        #self.item.product.id = int(unicode(self.ui.pidText.text()))
        self.item.product.name = unicode(self.ui.nameText.text())
        self.item.product.provider = unicode(self.ui.providerText.text())
        self.item.product.price = float(unicode(self.ui.priceText.text()))
        self.item.product.amount = int(unicode(self.ui.amountText.text()))

        if self.item.product.new :
            self.item.product.save()
        else :
            self.item.product.update()

        self.reloadRow()
        self.hide()

    def cancel (self) :
        if self.item.product.new :
            self.item
        else :
            self.item.setText(0, str(self.item.product.id))
            self.item.setText(1, self.item.product.name)
            self.item.setText(2, self.item.product.provider)
            self.item.setText(3, str(self.item.product.price))
            self.item.setText(4, str(self.item.product.amount))

        self.hide()

    def reloadRow (self) :
        pid = unicode(self.ui.pidText.text())
        name = unicode(self.ui.nameText.text())
        provider = unicode(self.ui.providerText.text())
        price = unicode(self.ui.priceText.text())
        amount = unicode(self.ui.amountText.text())

        self.item.setText(0, pid)
        self.item.setText(1, name)
        self.item.setText(2, provider)
        self.item.setText(3, price)
        self.item.setText(4, amount)
        
