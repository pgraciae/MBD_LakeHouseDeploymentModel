# Databricks notebook source
# MAGIC %md
# MAGIC #### Analisis datos capa gold
# MAGIC
# MAGIC En este apartado nos centramos en analizar las tablas de la capa gold

# COMMAND ----------

from pyspark.sql import functions as F
from pyspark.sql import SparkSession
from pyspark.sql import DataFrame
import matplotlib.pyplot as plt

# Crear o obtener la Spark Session
spark = SparkSession.builder \
    .appName("data analysis") \
    .getOrCreate()

# COMMAND ----------

spark.sql('USE CATALOG main')

# COMMAND ----------

# MAGIC %md
# MAGIC #### Leer datos gold

# COMMAND ----------

df_product_summary = spark.read.table("gold.ProductSummary")
df_user_activity = spark.read.table("gold.UserActivity")

# COMMAND ----------

# MAGIC %md
# MAGIC #### Análisis 1:
# MAGIC Top 10 productos con más ratio promedio

# COMMAND ----------

top_10_products = df_product_summary.orderBy(F.desc("average_rating")).limit(10)
top_10_products.display()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Análisis 2:
# MAGIC Top 5 usuarios más activos

# COMMAND ----------

top_5_users = df_user_activity.orderBy(F.desc("total_reviews_written")).limit(5)
top_5_users.display()

# COMMAND ----------

#visualización
pdf = top_5_users.toPandas()
plt.barh(pdf['user_name'], pdf['total_reviews_written'])
plt.xlabel('Total Reviews Written')
plt.ylabel('User Name')
plt.title('Top 5 Most Active Users')
plt.show()
