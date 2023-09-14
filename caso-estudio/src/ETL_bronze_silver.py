# Databricks notebook source
# MAGIC %md
# MAGIC ## Transformación bronze - silver

# COMMAND ----------

from pyspark.sql import functions as F
from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType, FloatType

# Crear o obtener la Spark Session
spark = SparkSession.builder \
    .appName("Pre-procesamientoDatos") \
    .getOrCreate()


# COMMAND ----------

# MAGIC %md
# MAGIC #### Creación del modelo de datos en la capa silver

# COMMAND ----------

spark.sql("USE CATALOG main")

# spark.sql("DROP SCHEMA IF EXISTS silver")

spark.sql("CREATE SCHEMA IF NOT EXISTS silver")

spark.sql("DROP TABLE IF EXISTS silver.ProductInfo")

# Crear la tabla ProductInfo en la capa Silver
spark.sql("""
CREATE TABLE IF NOT EXISTS silver.ProductInfo (
    product_id STRING,
    product_name STRING,
    category STRING,
    actual_price DOUBLE,
    discounted_price DOUBLE,
    discount_percentage DOUBLE,
    img_link STRING,
    product_link STRING,
    about_product STRING
    )
USING DELTA
PARTITIONED BY (category)
OPTIONS ('path' = 'abfss://adl-silverlayer-test-01@sastoragelayertest02.dfs.core.windows.net/ProductInfo/')
""")

# Crear la tabla ProductReviews en la capa Silver
spark.sql('DROP TABLE IF EXISTS silver.ProductReviews')
spark.sql("""
CREATE TABLE IF NOT EXISTS silver.ProductReviews (
    review_id STRING,
    product_id STRING,
    user_id STRING,
    user_name STRING,
    rating DOUBLE,
    rating_count INT,
    review_title STRING,
    review_content STRING
)
USING DELTA
PARTITIONED BY (product_id)
OPTIONS ('path' = 'abfss://adl-silverlayer-test-01@sastoragelayertest02.dfs.core.windows.net/ProductReviews')
""")

# COMMAND ----------

# MAGIC %md
# MAGIC ### Ejecución de transformaciones

# COMMAND ----------

# MAGIC %md 
# MAGIC ##### Extract

# COMMAND ----------

# Cargar el dataset desde la capa de bronce
bronze_path = "abfss://adl-bronzelayer-test01@sastoragelayertest02.dfs.core.windows.net/amazon_sales.parquet"
df_bronze = spark.read.parquet(bronze_path, header=True, inferSchema=True)

# COMMAND ----------

# MAGIC %md
# MAGIC #####Transform

# COMMAND ----------

# Transformaciones para la tabla "product_info"
df_product_info = df_bronze.select(
    F.col("product_id").cast("string"),
    F.col("product_name").cast("string"),
    F.col("category").cast("string"),
    F.col("discounted_price").cast("double"),
    F.col("actual_price").cast("double"),
    F.col("discount_percentage").cast("string"),
    F.col("about_product").cast("string"),
    F.col("img_link").cast("string"),
    F.col("product_link").cast("string")
)

# Transformaciones para la tabla "product_reviews"
df_product_reviews = df_bronze.select(
    F.col("product_id").cast("string"),
    F.col("user_id").cast("string"),
    F.col("user_name").cast("string"),
    F.col("review_id").cast("string"),
    F.col("rating").cast("double"),
    F.col("rating_count").cast("int"),
    F.col("review_title").cast("string"),
    F.col("review_content").cast("string")
)

# Se crea un indice único para la columna review_id
df_product_reviews = df_product_reviews.withColumn('review_id', F.monotonically_increasing_id())

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Load

# COMMAND ----------

# Guardar los DataFrames transformados como tablas Delta en la capa de plata
df_product_info.write.format("delta").mode("overwrite").insertInto("silver.ProductInfo")

df_product_reviews.write.format("delta").mode("overwrite").insertInto("silver.ProductReviews")

# COMMAND ----------

# MAGIC %md
# MAGIC #### end

# COMMAND ----------

spark.stop()
