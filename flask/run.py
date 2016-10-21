# __*__coding:utf-8__*__
from flask import Flask, render_template, request
from pymongo import MongoClient
import time

app = Flask(__name__)
client = MongoClient("192.168.1.145", 27017)
db = client.hlssysalert


@app.route('/')
def hello_world():
    return 'Hello Worlds!'


@app.route('/http_code/query', methods=['POST', 'GET'])
def querry():
    now_time = time.strftime('%Y%m%d')
    col_name = 'http_stat' + now_time
    data = []
    if request.method == 'POST':
        time_arg = request.form['time']
        time_select = time_arg.replace('-', '')
        if len(time_select) == 0:
            col = db.get_collection(col_name)
            res = col.find()
            for i in res:
                data.append(i)
            return render_template("http_stat.html", info=data)
        else:
            col_name = 'http_stat' + time_select
            col = db.get_collection(col_name)
            res = col.find()
            for i in res:
                data.append(i)
            return render_template("http_stat.html", info=data)
    else:
        col = db.get_collection(col_name)
        res = col.find()
        for i in res:
            data.append(i)
        return render_template("http_stat.html", info=data)


app.run(host='0.0.0.0', port=9090, debug=True)
