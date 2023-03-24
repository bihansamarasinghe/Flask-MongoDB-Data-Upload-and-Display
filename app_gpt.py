from flask import Flask, request, render_template, redirect
import pandas as pd
import json
import mongodb

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # get the uploaded file
    file = request.files['file1']

   # read the file using pandas
    df = pd.read_csv(file, skiprows=7, usecols=['Occurred On (NT)', 'Cleared On (NT)', 'MO Name', 'Name'])

    # convert the dataframe to a JSON string
    json_data = df.to_json(orient='records')

    # delete all documents in the collection
    mongodb.collection.delete_many({})

    # insert the JSON data into MongoDB
    mongodb.collection.insert_many(json.loads(json_data))

    # print the JSON string to the console in debug mode
    #if app.debug:
        #print(json.dumps(json_data, indent=4))
        #print(type(json_data))

    # Return a JSON response indicating that the upload was successful
    return redirect('/table')

@app.route('/table')
def show_table():
    # retrieve the data from MongoDB
    data = list(mongodb.collection.find({}, {'_id': 0}))

    # create a DataFrame from the data
    df = pd.DataFrame(data)

    # convert the DataFrame to an html table
    table = df.to_html(classes='table table-striped table-bordered table-hover')

    # render the table in the table.html template
    return render_template('table.html', table=table)


if __name__ == '__main__':
    app.run(debug=True)