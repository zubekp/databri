# Databricks notebook source
class Demo:
    
    def __init__(self,name='Petr',age=47):
        self.name=name
        self.age=age
        
    def display_name(self):
        print(self.name,'-',self.age)
        
    def set_name(self,name):
        self_name=name

# COMMAND ----------

demo = Demo()

# COMMAND ----------

demo.display_name()

# COMMAND ----------


