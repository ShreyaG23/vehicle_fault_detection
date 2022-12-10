import pymongo
import pandas as pd
import json

# Provide the mongodb localhost url to connect python to mongodb
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

#database name
DATABASE_NAME = "aps"
DATA_FILE_PATH = "/config/workspace/aps_failure_training_set1.csv"
#collection name
COLLECTION_NAME = "sensor"

if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"rows and column : {df.shape}")

#convert dataframe into json so that we can dump these records in mongo DB
df.reset_index(drop= True, inplace=True)

#transpose dataframe and convert to jon format also store each record (row) in list
json_record = list(json.loads(df.T.to_json()).values())
#print(json_record[0])

#insert json_record into mongoDB

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)