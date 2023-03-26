from flask import Flask, render_template
from show_table import table_show
from upload import upload_huawei, upload_ftg, upload_stg
import mongodb

app = Flask(__name__, static_url_path='/static')

#Call index.html template for root
@app.route('/')
def home():
    return render_template('index.html')

#Call huawei file upload function as /uploadhuawei domain
@app.route('/uploadhuawei', methods=['POST'])
def uploadhuawei():

    result = upload_huawei()
    return result

#Call ftg file upload function as /uploadftg domain
@app.route('/uploadftg', methods=['POST'])
def uploadftg():

    result = upload_ftg()
    return result

#Call ftg file upload function as /uploadftg domain
@app.route('/uploadstg', methods=['POST'])
def uploadstg():

    result = upload_stg()
    return result

#Show huawei uploaded table as /tablehua domain
@app.route('/tablehua')
def show_table_huawei():

    result = table_show('huawei_table.html',mongodb.collection_hua)
    return result

#Show FTG uploaded table as /tableftg domain
@app.route('/tableftg')
def show_table_ftg():

    result = table_show('table_ftg.html',mongodb.collection_ftg)
    return result

#Show STG uploaded table as /tablestg domain
@app.route('/tablestg')
def show_table_stg():

    result = table_show('table_stg.html',mongodb.collection_stg)
    return result

if __name__ == '__main__':
    app.run(debug=True)