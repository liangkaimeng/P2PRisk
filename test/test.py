# -*- coding: utf-8 -*-
# Author: 梁开孟
# date: 2023/9/1 20:55

from aquadb.query import read_table

user = "scott"
query = "SELECT * FROM PPD_LOAN_CHARACTERISTICS;"
data = read_table(user, query=query)
print(data.head())
