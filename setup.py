# -*- coding: utf-8 -*-

"""A simple backend for a Pharma app"""

import os
import sys
sys.path.append("../RelaXML/src")
from DBMS import DBMS

dbms = DBMS("database", ".")

db_name = "pharmaCC"
if db_name not in dbms.databases.keys() :
    dbms.createDatabase("pharmaCC")

db = dbms.useDatabase("pharmaCC")

if not db.hasTable("provider") :
  providerColumns = {"id_prov" : "int",
                     "name_prov" : "unicode",
                     "phone_prov": "unicode"}
  db.createTable("provider", providerColumns)

  prov1 = {"id_prov" : 0, "name_prov" : u"ex provider 11", "phone_prov" : u"6548-7877"}
  db.insertInto("provider", prov1)                     
  prov2 = {"id_prov" : 1, "name_prov" : u"ex provider 22", "phone_prov" : u"6848-7877"}
  db.insertInto("provider", prov2)                     
  prov3 = {"id_prov" : 2, "name_prov" : u"ex provider 33", "phone_prov" : u"6948-7117"}
  db.insertInto("provider", prov3)                     
  prov4 = {"id_prov" : 3, "name_prov" : u"ex provider 44", "phone_prov" : u"6048-7987"}
  db.insertInto("provider", prov4)

if not db.hasTable("product") :
    productColumns = {"id_prod": "int",
                      "name_prod": "unicode",
                      "prov_prod": "int",
                      "price_prod": "float",
                      "amount_prod": "int"}
    db.createTable("product", productColumns)

    prod1 = {"id_prod"    : 0         ,
             "name_prod"  : u"dipirona",
             "prov_prod"  : 0 ,
             "price_prod" : 2.98      ,
             "amount_prod": 30        }
    db.insertInto("product", prod1)
    prod2 = {"id_prod"    : 1         ,
             "name_prod"  : u"anador" ,
             "prov_prod"  : 1 ,
             "price_prod" : 9.98      ,
             "amount_prod": 90        }
    db.insertInto("product", prod2)
    prod3 = {"id_prod"    : 2         ,
             "name_prod"  : u"doril" ,
             "prov_prod"  : 3 ,
             "price_prod" : 9.98      ,
             "amount_prod": 30        }
    db.insertInto("product", prod3)

if not db.hasTable("sold_product") :
    sold_prodColumns = {"id_sold_prod": "int",
                        "id_sell_sold_prod": "int",
                        "id_prod_sold_prod": "int"}
    db.createTable("sold_product", sold_prodColumns)

    db.insertInto("sold_product", {"id_sold_prod" :0 , "id_sell_sold_prod" : 0, "id_prod_sold_prod" : 0})
    db.insertInto("sold_product", {"id_sold_prod" :1 , "id_sell_sold_prod" : 0, "id_prod_sold_prod" : 0})
    db.insertInto("sold_product", {"id_sold_prod" :2 , "id_sell_sold_prod" : 1, "id_prod_sold_prod" : 1})
    db.insertInto("sold_product", {"id_sold_prod" :3 , "id_sell_sold_prod" : 1, "id_prod_sold_prod" : 1})
    db.insertInto("sold_product", {"id_sold_prod" :4 , "id_sell_sold_prod" : 2, "id_prod_sold_prod" : 2})
    db.insertInto("sold_product", {"id_sold_prod" :5 , "id_sell_sold_prod" : 2, "id_prod_sold_prod" : 1})
    db.insertInto("sold_product", {"id_sold_prod" :6 , "id_sell_sold_prod" : 2, "id_prod_sold_prod" : 0})

if not db.hasTable("sell") :
    sellColumns = {"id_sell": "int"}
    db.createTable("sell", sellColumns)

    db.insertInto("sell", {"id_sell" :0})
    db.insertInto("sell", {"id_sell" :1})
    db.insertInto("sell", {"id_sell" :2})
    
