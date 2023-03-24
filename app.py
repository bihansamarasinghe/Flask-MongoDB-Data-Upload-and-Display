from flask import Flask, render_template
from show_table import show_table
from upload import upload_huawei

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload1', methods=['POST'])
def upload():

    result = upload_huawei()
    return result

@app.route('/table')
def show_table_huawei():

    result = show_table()
    return result


if __name__ == '__main__':
    app.run(debug=True)