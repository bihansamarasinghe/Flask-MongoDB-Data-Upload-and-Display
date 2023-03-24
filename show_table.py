import mongodb
import pandas as pd
from flask import render_template

def show_table():
    # retrieve the data from MongoDB
    data = list(mongodb.collection.find({}, {'_id': 0}))

    # create a DataFrame from the data
    df = pd.DataFrame(data)

    # convert the DataFrame to an html table
    table = df.to_html(classes='table table-striped table-bordered table-hover')

    # render the table in the table.html template
    return render_template('table.html', table=table)