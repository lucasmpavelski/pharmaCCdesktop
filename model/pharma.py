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

  def saveToTable (self) :
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
      self.who = "product"

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

    def save (self) :
      self.saveToTable()

    def update (self) :
      self.updateThe("id_prod == " + str(self.id))

    def remove (self) :
      self.removeThe("id_prod == " + str(self.id))
      
    

class Provider (object) :
    """
    A provider to the pharma.
    """

    def __init__ (self, pid, name, phone) :
      self.new = True

      self.id = pid
      self.name = name
      self.phone = phone
          
    def __repr__(self):
      return "Provider: " + self.name + ", phone:" + self.phone

    def _get_dict (self) :
      return {"id_prov"    : self.id,
              "name_prov"  : self.name,
              "phone_prov" : self.phone}

    def save (self) :
      self.saveToTable("provider")
      #self.new = False
      #print "save " + self.name
      #values = {"id_prov"    : self.pid,
		#"name_prov"  : self.name,
		#"phone_prov" : self.phone}
      #db.insertInto("provider", values)

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
