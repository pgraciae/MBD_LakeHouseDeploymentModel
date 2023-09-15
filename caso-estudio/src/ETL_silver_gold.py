# Databricks notebook source
# MAGIC %md
# MAGIC ## Transformación bronze - silver

# COMMAND ----------

from pyspark.sql import functions as F
from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType, FloatType

# Crear o obtener la Spark Session
spark = SparkSession.builder \
    .appName("Silver-Gold") \
    .getOrCreate()


# COMMAND ----------

# MAGIC %md
# MAGIC #### Creación del modelo de datos en la capa silver

# COMMAND ----------

# En este caso, para ejemplificar otro metodo operandi, la tabla se crea en la inserción de los datos
spark.sql("USE CATALOG main")

# COMMAND ----------

# MAGIC %md
# MAGIC ### Ejecución de transformaciones

# COMMAND ----------

# MAGIC %md 
# MAGIC ##### Extract

# COMMAND ----------

# Cargar las tablas desde la capa de silver
df_product_info = spark.read.table("silver.ProductInfo")
df_product_reviews = spark.read.table("silver.ProductReviews")

# COMMAND ----------

# MAGIC %md
# MAGIC #####Transform

# COMMAND ----------

# Transformaciones para la tabla ProductSummary en la capa Gold
df_product_summary = df_product_info.join(
    df_product_reviews, "product_id", "inner"
).groupBy(
    "product_id", "product_name"
).agg(
    F.avg("rating").alias("average_rating"),
    F.count("review_id").alias("total_reviews"),
    F.sum("rating_count").alias("total_rating_count")
    )


# Transformaciones para la tabla UserActivity en la capa Gold
df_user_activity = df_product_reviews.groupBy(
    "user_id", "user_name"
).agg(
    F.count("review_id").alias("total_reviews_written"),
    F.avg("rating").alias("average_rating_given")
)

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Load

# COMMAND ----------

spark.sql("CREATE SCHEMA IF NOT EXISTS main.gold")

# COMMAND ----------

# Escribir la tabla ProductSummary en la capa Gold
df_product_summary.write \
    .format("delta") \
    .mode("overwrite") \
    .option("path", "abfss://adl-goldlayer-test-01@sastoragelayertest02.dfs.core.windows.net/ProductSummary") \
    .saveAsTable("gold.ProductSummary")

# Escribir la tabla UserActivity en la capa Gold
df_user_activity.write \
    .format("delta") \
    .mode("overwrite") \
    .option("path", "abfss://adl-goldlayer-test-01@sastoragelayertest02.dfs.core.windows.net/UserActivity") \
    .saveAsTable("gold.UserActivity")

# COMMAND ----------

# MAGIC %md
# MAGIC #### end

# COMMAND ----------

spark.stop()
