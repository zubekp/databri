# Databricks notebook source
from dataclasses import dataclass

# COMMAND ----------

@dataclass
class MyRecord:
    name : str
    age : int
        

# COMMAND ----------

<<<<<<< HEAD
listek = []

# COMMAND ----------

print('no otot')
=======
listek = [MyRecord('Petere',i) for i in range(5)]

# COMMAND ----------

print(listek)

# COMMAND ----------

print(listek[3].age)

# COMMAND ----------

print(listek[3].name, listek[4].age)

# COMMAND ----------


>>>>>>> parent of 7fbdff6 (delete to back)
