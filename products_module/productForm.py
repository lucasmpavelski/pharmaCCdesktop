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
        self.ui.pidText.setText(str(self.item.produto.pid))
        self.ui.nameText.setText(self.item.produto.name)
        self.ui.fornecedorText.setText(self.item.produto.fornecedor)
        self.ui.priceText.setText(self.item.produto.price)
        self.ui.amountText.setText(self.item.produto.amount)

        #self.ui.tags.setText(','.join( t.name for t in self.item.task.tags))
        self.show()

    def save (self) :
        self.item.produto.pid = int(unicode(self.ui.pidText.text()))
        self.item.produto.name = unicode(self.ui.nameText.text())
        self.item.produto.fornecedor = unicode(self.ui.fornecedorText.text())
        self.item.produto.price = float(unicode(self.ui.priceText.text()))
        self.item.produto.amount = int(unicode(self.ui.amountText.text()))

        if self.item.produto.new :
            self.item.produto.save()
        else :
            self.item.produto.update()

        self.reloadRow()
        self.hide()

    def cancel (self) :
        self.item.setText(0, str(self.item.produto.pid))
        self.item.setText(1, self.item.produto.name)
        self.item.setText(2, self.item.produto.fornecedor)
        self.item.setText(3, self.item.produto.price)
        self.item.setText(4, self.item.produto.amount)

        self.hide()

    def reloadRow (self) :
        pid = unicode(self.ui.pidText.text())
        name = unicode(self.ui.nameText.text())
        fornecedor = unicode(self.ui.fornecedorText.text())
        price = unicode(self.ui.priceText.text())
        amount = unicode(self.ui.amountText.text())

        self.item.setText(0, pid)
        self.item.setText(1, name)
        self.item.setText(2, fornecedor)
        self.item.setText(3, price)
        self.item.setText(4, amount)
        
