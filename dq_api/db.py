from pymongo import MongoClient
import os

uri = os.getenv("COSMOS_DB_URI")  # store this in .env
client = MongoClient(uri)

db = client["dq_tool"]  # or your actual DB name
files_col = db["files"]
rules_col = db["rules"]
results_col = db["results"]
