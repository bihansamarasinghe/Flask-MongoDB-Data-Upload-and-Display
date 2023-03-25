from flask import request, redirect , render_template
import pandas as pd
import json
from datetime import datetime
import mongodb

def upload_huawei():
    
    # get the uploaded file
    file = request.files['file1']

   # read the file using pandas
    df = pd.read_csv(file, skiprows=7, usecols=['Occurred On (NT)', 'Cleared On (NT)', 'MO Name', 'Name'])
    df.loc[df['MO Name'].str.startswith('NodeB Name='), 'MO Name'] = \
    df.loc[df['MO Name'].str.startswith('NodeB Name='), 'MO Name'].str.split(',', n=1).str[0].str.replace('NodeB Name=', '')

    # extract first 2 characters of MO Name column and add to Region ID column
    df['Region ID'] = df['MO Name'].apply(lambda x: x[-2:])

    # extract first 6 characters of MO Name column and add to Site ID column
    df['Site ID'] = df['MO Name'].apply(lambda x: x[:6])

    # check if 'NOA' is in MO Name, then set Region ID to 'NOA'
    df.loc[df['MO Name'].str.contains('NOA'), 'Region ID'] = 'NOA'

    # move Site ID column to before MO Name column
    cols = list(df.columns)
    cols = cols[:2] + ['Site ID'] + cols[2:4] + ['Region ID'] + cols[4:-2]
    df = df[cols]

    # add 'Site Type' column to df
    def get_site_type(site_id):
        if site_id[0] == 'Q':
            return 'Small Cell'
        elif site_id[0] == 'L':
            return 'Lamp Pole'
        else:
            return 'Macro'

    df['Site Type'] = df['Site ID'].apply(get_site_type)

    def get_band(name):
        if name == 'NodeB Unavailable':
            return '3G'
        elif name in ['CSL Fault', 'OML Fault']:
            return '2G'
        elif name == 'NE Is Disconnected':
            return '4G'
        else:
            return ''

    df['Band'] = df['Name'].apply(get_band)

    # Add Duration column
    #occurred = pd.to_datetime(df['Occurred On (NT)'], format='%Y-%m-%d %H:%M:%S')
    #cleared = pd.to_datetime(df['Cleared On (NT)'], format='%Y-%m-%d %H:%M:%S', errors='coerce')
    #df['Duration'] = (cleared - occurred).dt.total_seconds().div(60).fillna('')

    # Round up Duration values
    #df.loc[df['Duration'] != '', 'Duration'] = df.loc[df['Duration'] != '', 'Duration'].astype(float).round(decimals=0)

    # Add Duration column
    occurred = pd.to_datetime(df['Occurred On (NT)'], format='%Y-%m-%d %H:%M:%S')

    # fill 'Cleared On (NT)' column with current date and time
    cleared = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # replace '-' with current date and time in 'Cleared On (NT)' column
    df.loc[df['Cleared On (NT)'] == '\t\t-', 'Cleared On (NT)'] = cleared

    df['Duration'] = (pd.to_datetime(df['Cleared On (NT)'], format='%Y-%m-%d %H:%M:%S') - occurred).dt.total_seconds().div(60).fillna('')

    # Round up Duration values
    df.loc[df['Duration'] != '', 'Duration'] = df.loc[df['Duration'] != '', 'Duration'].astype(float).round(decimals=0).astype(int)

    # Rename the column
    df = df.rename(columns={'Duration': 'Duration (BTSmin)'})

    # convert the dataframe to a JSON string
    json_data = df.to_json(orient='records')

    # delete all documents in the collection
    mongodb.collection_hua.delete_many({})

    # insert the JSON data into MongoDB
    mongodb.collection_hua.insert_many(json.loads(json_data))

    # print the JSON string to the console in debug mode
    #if app.debug:
        #print(json.dumps(json_data, indent=4))
        #print(type(json_data))

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

def merge():

    # create df1
    data1 = list(mongodb.collection_hua.find({}, {'_id': 0}))
    df1 = pd.DataFrame(data1)

    # create df2
    data2 = list(mongodb.collection_ftg.find({}, {'_id': 0}))
    df2 = pd.DataFrame(data2)

    # perform vlookup
    df_merged = pd.merge(df1, df2, on='Site ID', how='left')

    # create 'FTG Status' column and set values based on condition
    df_merged['FTG Status'] = ''
    df_merged.loc[df_merged['Site ID'].isin(df2['Site ID']), 'FTG Status'] = 'FTG'


    # convert the DataFrame to an html table
    data_dict = df_merged.to_dict('records')

    #print(df_merged)

    # render the table in the table.html template
    return render_template('merge_table.html', data=data_dict)

