# Databricks notebook source
from dataclasses import dataclass

# COMMAND ----------

@dataclass
class MyRecord:
    name : str
    age : int
        

# COMMAND ----------

listek = [MyRecord('Petere',i) for i in range(5)]

# COMMAND ----------

print(listek)

# COMMAND ----------

print(listek[3].age)

# COMMAND ----------

print(listek[3].name, listek[4].age)

# COMMAND ----------


