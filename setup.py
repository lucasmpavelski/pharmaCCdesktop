# -*- coding: utf-8 -*-

"""A simple backend for a Pharma app"""

import os
import sys
sys.path.append("../RelaXML/src")
from DBMS import DBMS

dbdir=os.path.join(".", "database")

dbms = DBMS(dbdir)

dbms.createDatabase("pharmaCC")

db = dbms.useDatabase("pharmaCC")

#providerColumns = {"id_prov" : "int",
#		   "name_prov" : "str",
#		   "phone_prov": "str"}
#db.createTable("provider", providerColumns)
#
#prov1 = {"id_prov" : 0, "name_prov" : "ex provider 11", "phone_prov" : "6548-7877"}
#db.insertInto("provider", prov1)                     
#prov2 = {"id_prov" : 1, "name_prov" : "ex provider 22", "phone_prov" : "6848-7877"}
#db.insertInto("provider", prov2)                     
#prov3 = {"id_prov" : 2, "name_prov" : "ex provider 33", "phone_prov" : "6948-7117"}
#db.insertInto("provider", prov3)                     
#prov4 = {"id_prov" : 3, "name_prov" : "ex provider 44", "phone_prov" : "6048-7987"}
#db.insertInto("provider", prov4)

productColumns = {"id_prod": "int",
		  "name_prod": "str",
		  "prov_prod": "str",
		  "price_prod": "float",
		  "amount_prod": "int"}
db.createTable("product", productColumns)

prod1 = {"id_prod"    : 0         ,
         "name_prod"  : "dipirona",
         "prov_prod"  : "farmax"  ,
         "price_prod" : 2.98      ,
         "amount_prod": 30        }
db.insertInto("product", prod1)
prod2 = {"id_prod"    : 1         ,
         "name_prod"  : "anador"  ,
         "prov_prod"  : "farmex"  ,
         "price_prod" : 9.98      ,
         "amount_prod": 90        }
db.insertInto("product", prod2)
