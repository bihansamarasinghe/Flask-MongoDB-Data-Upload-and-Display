from flask import Flask, render_template
from show_table import show_hua_table,show_ftg_table
from upload import upload_huawei,upload_ftg,merge

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/uploadhuawei', methods=['POST'])
def uploadhuawei():

    result = upload_huawei()
    return result

@app.route('/uploadftg', methods=['POST'])
def uploadftg():

    result = upload_ftg()
    return result

@app.route('/tablehua')
def show_table_huawei():

    result = show_hua_table()
    return result

@app.route('/tableftg')
def show_table_ftg():

    result = show_ftg_table()
    return result

@app.route('/tablemerge')
def show_table_merge():

    result = merge()
    return result

if __name__ == '__main__':
    app.run(debug=True)