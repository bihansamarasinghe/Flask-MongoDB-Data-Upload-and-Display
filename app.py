from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # get the uploaded file
    file = request.files['file']

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


    # convert the dataframe to an html table
    table = df.to_html(classes='table table-striped table-bordered table-hover')

    # render the table in the table.html template
    return render_template('table.html', table=table)

if __name__ == '__main__':
    app.run(debug=True)
