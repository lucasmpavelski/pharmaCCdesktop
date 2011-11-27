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

  def update (self) :
    when = self.__class__.id_field + " == " + str(self.id)
    db.update(self.who, when, self._get_dict())
    print "update " + self.who + " " + self.name

  def remove (self) :
    when = self.__class__.id_field + " == " + str(self.id)
    db.deleteFrom(self.who, when)
    print "delete " + self.who + " " + self.name

  def getAll (self) :
    return db.fromTables([self.who]).data

  def lastId (self, id_col) :
    return db.fromTables([self.who]).max_value(id_col)

  @classmethod
  def get_all (cls) :
    allrows =  db.fromTables([cls.who])
    r = []
    for row in allrows.data :
      row.update({'isNew': False})
      r.append(cls(**row))
    return r

  @classmethod
  def find (cls, _id) :
    row = db.fromTables([cls.who]).where(cls.id_field + " == " + str(_id))
    if row.data :
      row[0].update({'isNew': False})
      return cls(**row[0])
    else :
      return None


class Product (Record) :
    """
    A product to the pharma.
    """
    who = "product"
    id_field = "id_prod"

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
      
    
class Provider (Record) :
    """
    A provider to the pharma.
    """
    who = "provider"
    id_field = "id_prov"

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


class SoldProduct (Record) :
    """
    A product that has been sold.
    """
    who = "sold_product"
    id_field = "id_sold_prod"

    def __init__ (self, id_prod_sold_prod, id_sell_sold_prod, id_sold_prod = None, isNew = True) :
      self.new = isNew
      self.who = SoldProduct.who

      if sold_prod_id == None :
        self.id = self.lastId("sold_product") + 1
      else :
        self.id = sold_prod_id

      self.prod = id_prod_sold_prod
      self.sell = id_prod_sold_prod

    def _get_dict (self) :
      return {"id_sold_prod"      : self.id,
              "id_prod_sold_prod" : self.id_prod,
              "id_sell_sold_prod" : self.id_sell}
      
      
class Sell (Record) :
    """
    A sell full of products.
    """
    who = "sell"
    id_field = "id_sell"

    def __init__ (self, id_sell = None, isNew = True) :
      self.new = isNew
      self.who = Sell.who

      if id_sell == None :
        self.id = self.lastId("sell") + 1
      else :
        self.id = id_sell

      self.id = id_sell

    def _get_dict (self) :
      return {"id_sell" : self.id}
      
    def products (self) :
      r = []
      rows = db.fromTables(["sold_product"]).where("id_sell_sold_prod == " + str(self.id)).select(['id_prod_sold_prod'])
      for row in rows :
        r.append(Product.find(row['id_prod_sold_prod']))
      return r
        
def main() :
  print Provider.get_all()

if __name__ == "__main__":
    main()
