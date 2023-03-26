from flask import request, redirect
import pandas as pd
import json
import mongodb
from dataclean import clean

def upload_huawei():
    
    # get the uploaded file
    df_id = request.files['file1']
    clean(df_id)

    # Return a JSON response indicating that the upload was successful
    return redirect('/tablehua')

def upload_ftg():
    
    # get the uploaded file
    file = request.files['file2']

   # read the file using pandas
    df = pd.read_excel(file)

    # convert the dataframe to a JSON string
    json_data = df.to_json(orient='records')

    # delete all documents in the collection
    mongodb.collection_ftg.delete_many({})

    # insert the JSON data into MongoDB
    mongodb.collection_ftg.insert_many(json.loads(json_data))

    # print the JSON string to the console in debug mode
    #if app.debug:
        #print(json.dumps(json_data, indent=4))
        #print(type(json_data))

    # Return a JSON response indicating that the upload was successful
    return redirect('/tableftg')

def upload_stg():
    
    # get the uploaded file
    file = request.files['file3']

   # read the file using pandas
    df = pd.read_excel(file)

    # convert the dataframe to a JSON string
    json_data = df.to_json(orient='records')

    # delete all documents in the collection
    mongodb.collection_stg.delete_many({})

    # insert the JSON data into MongoDB
    mongodb.collection_stg.insert_many(json.loads(json_data))

    # print the JSON string to the console in debug mode
    #if app.debug:
        #print(json.dumps(json_data, indent=4))
        #print(type(json_data))

    # Return a JSON response indicating that the upload was successful
    return redirect('/tablestg')

