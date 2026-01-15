# Databricks notebook source
sale_data = spark.read.csv("/Volumes/workspace/default/data/product_sales_solution - orders.csv", 
                           header=True, 
                           inferSchema=True
                           )

customer = spark.read.csv("/Volumes/workspace/default/data/product_sales_solution - customers.csv", 
                          header = True, 
                          inferSchema=True
                          )

# COMMAND ----------

# Task 1: Convert CSV to Delta format and save as table

from pyspark.sql.functions import col

sale_data_clean = sale_data.withColumnRenamed("price (in INR)", "price_in_INR")

sale_data_clean.write\
    .format("delta")\
    .mode("overwrite")\
    .saveAsTable("workspace.default.sale_data")

# COMMAND ----------

# MAGIC %md
# MAGIC **Create New Schema**

# COMMAND ----------

new_schema = spark.createDataFrame([("abc", "xyz")], ["col1", "col2"])
new_schema.printSchema()

# COMMAND ----------

# Task 2:- Test schema enforcement

try:
    new_schema.write\
        .format("delta")\
        .mode("append")\
        .saveAsTable("workspace.default.sale_data")
except Exception as e:
    print(e)