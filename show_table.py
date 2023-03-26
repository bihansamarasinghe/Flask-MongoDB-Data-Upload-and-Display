import pandas as pd
from flask import render_template

def table_show(table,collection):
    # retrieve the data from MongoDB
    data = list(collection.find({}, {'_id': 0}))

    # create a DataFrame from the data
    df = pd.DataFrame(data)

    # convert the DataFrame to an html table
    data_dict = df.to_dict('records')

    # render the table in the table.html template
    return render_template(table, data=data_dict)