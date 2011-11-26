# -*- coding: utf-8 -*-

"""A simple backend for a Pharma app"""

import os
import sys
sys.path.append("../RelaXML/src")
from DBMS import DBMS

dbms_name = "database"
dbms_path = "."
dbms = DBMS(dbms_name, dbms_path)

db = dbms.useDatabase("pharmaCC")



class Product (object) :
    """
    A product to the pharma.
    """

    def __init__ (self, pid, name, provider, price, amount, isNew = True) :
      self.new = isNew

      self.id = pid
      self.name = name
      self.provider = provider
      self.price = price
      self.amount = amount
          
    def __repr__(self):
      return "Product: " + self.name

    def _get_dict (self) :
      return {"id_prod"    : self.id,
              "name_prod"  : self.name,
              "prov_prod"  : self.provider,
              "price_prod" : self.price,
              "amount_prod": self.amount}

    def save (self) :
      self.new = False
      print "save product " + self.name
      values = self._get_dict()
      db.insertInto("product", values)

    def update (self) :
      db.update("product", "id_prod == " + str(self.id), self._get_dict())
      print "update " + self.name

    def remove (self) :
      db.deleteFrom("product", "id_prod == " + str(self.id))
      print "delete product " + self.name

    @staticmethod
    def query (qry) :
      prods = db.fromTables(["product"])
      r = []
      for prod in prods.data :
          r.append(Product( prod["id_prod"    ],
                            prod["name_prod"  ], 
                            prod["prov_prod"  ], 
                            prod["price_prod" ], 
                            prod["amount_prod"],
                            False))
      return r

class Provider (object) :
    """
    A provider to the pharma.
    """

    def __init__ (self, pid, name, phone) :
      self.new = True

      self.pid = pid
      self.name = name
      self.phone = phone
          
    def __repr__(self):
      return "Provider: " + self.name + ", phone:" + self.phone

    def save (self) :
      self.new = False
      print "save " + self.name
      values = {"id_prov"    : self.pid,
		"name_prov"  : self.name,
		"phone_prov" : self.phone}
      db.insertInto("provider", values)

    def update (self) :
      print "update " + self.name
      #allproviders.append(self)

    def delete (self) :
      print "delete " + self.name
      #allproviders.remove(self)

    @staticmethod
    def query (qry) :
      provs = db.fromTables(["provider"])
      r = []
      for prov in provs.data :
          r.append(Provider(prov['id_prov'], prov['name_prov'], prov['phone_prov']))
      return r

def initDB() :
    allproviders.extend([Provider(0, "nha", "54654"),
          	       Provider(1, "nha1", "65654"),
          	       Provider(2, "nha2", "54622"),
          	       Provider(3, "nha3", "34654")])
    for p in allproviders : p.new = False

def main() :
  initDB()
  print Provider.query("all")
  allproviders[2].delete()
  print Provider.query("all")
  p = Provider(10, "yey", "4654")
  p.save()
  print Provider.query("all")

if __name__ == "__main__":
    main()
