# Databricks notebook source
BLOB_CONTAINER = 'dev'
BLOB_ACCOUNT = 'dltp8tdylpblob'
ACCOUNT_KEY = dbutils.secrets.get(scope='akv-secrets', key='storage-account-key1')

# COMMAND ----------

DIRECTORY = "/"
MOUNT_PATH = "/mnt/dev"

try:
  dbutils.fs.mount(
    source = f"wasbs://{BLOB_CONTAINER}@{BLOB_ACCOUNT}.blob.core.windows.net",
    mount_point = MOUNT_PATH,
    extra_configs = {
      f"fs.azure.account.key.{BLOB_ACCOUNT}.blob.core.windows.net":ACCOUNT_KEY
    }
  )
except Exception as e:
  print(f"Already mounted on {MOUNT_PATH}. Unmount first if needed")

# COMMAND ----------

# MAGIC %fs ls /mnt

# COMMAND ----------

