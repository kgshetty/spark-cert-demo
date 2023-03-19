# Databricks notebook source
# MAGIC %run ./Includes/Setup

# COMMAND ----------

print(projectName)

# COMMAND ----------

# MAGIC %md
# MAGIC # FS

# COMMAND ----------

# MAGIC %fs 
# MAGIC ls dbfs:/databricks-datasets/COVID/download_daily_covid-19_datasets.sh

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------


