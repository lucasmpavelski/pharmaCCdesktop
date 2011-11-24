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

allproviders = []

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
