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
printops = True


class Record (object) :

  def save (self) :
    self.new = False
    print "save " + self.who + " " + self.name
    values = self._get_dict()
    db.insertInto(self.who, values)

  def updateThe (self, when) :
    db.update(self.who, when, self._get_dict())
    print "update " + self.who + " " + self.name

  def removeThe (self, when) :
    db.deleteFrom("product", when)
    print "delete " + self.who + " " + self.name

  def getAll (self) :
    return db.fromTables([self.who]).data

  def lastId (self, id_col) :
    return db.fromTables([self.who]).max_value(id_col)

  @classmethod
  def get_all (cls) :
    print cls.who
    allrows =  db.fromTables([cls.who])
    r = []
    for row in allrows.data :
      row.update({'isNew': False})
      r.append(cls(**row))
    return r


class Product (Record) :
    """
    A product to the pharma.
    """
    who = "product"

    def __init__ (self, name_prod, prov_prod, price_prod, amount_prod, id_prod = None, isNew = True) :
      self.new = isNew
      self.who = Product.who

      if id_prod == None :
        self.id = self.lastId("id_prod") + 1
      else :
        self.id = id_prod

      self.name = name_prod
      self.provider = prov_prod
      self.price = price_prod
      self.amount = amount_prod
          
    def __repr__(self):
      return "Product: " + self.name

    def _get_dict (self) :
      return {"id_prod"    : self.id,
              "name_prod"  : self.name,
              "prov_prod"  : self.provider,
              "price_prod" : self.price,
              "amount_prod": self.amount}

    def update (self) :
      self.updateThe("id_prod == " + str(self.id))

    def remove (self) :
      self.removeThe("id_prod == " + str(self.id))
      
    
class Provider (Record) :
    """
    A provider to the pharma.
    """
    who = "provider"

    def __init__ (self, name_prov, phone_prov, id_prov = None, isNew = True) :
      self.new = isNew
      self.who = Provider.who

      if id_prov == None :
        self.id = self.lastId("id_prov") + 1
      else :
        self.id = id_prov

      self.name = name_prov
      self.phone = phone_prov
          
    def __repr__(self):
      return "Provider: " + self.name + ", phone:" + self.phone

    def _get_dict (self) :
      return {"id_prov"    : self.id,
              "name_prov"  : self.name,
              "phone_prov" : self.phone}

    def update (self) :
      self.updateThe("id_prov == " + str(self.id))

    def delete (self) :
      self.removeThe("id_prov == " + str(self.id))
      
    
class User (Record) :
    """
    A provider to the pharma.
    """
    who = "provider"

    def __init__ (self, name_prov, phone_prov, id_prov = None, isNew = True) :
      self.new = isNew
      self.who = Provider.who

      if id_prov == None :
        self.id = self.lastId("id_prov") + 1
      else :
        self.id = id_prov

      self.name = name_prov
      self.phone = phone_prov
          
    def __repr__(self):
      return "Provider: " + self.name + ", phone:" + self.phone

    def _get_dict (self) :
      return {"id_prov"    : self.id,
              "name_prov"  : self.name,
              "phone_prov" : self.phone}

    def update (self) :
      self.updateThe("id_prov == " + str(self.id))

    def delete (self) :
      self.removeThe("id_prov == " + str(self.id))


def main() :
  print Provider.get_all()

if __name__ == "__main__":
    main()
