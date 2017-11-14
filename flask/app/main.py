# coding=utf-8
from flask import Flask
from flask import render_template, redirect, url_for
from flask import request
from block import *      # импортируем наш блокчейн скрипт


import os     #для дебага


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():

    print(os.curdir)

    if request.method == 'POST':
        sender = request.form['sender']
        amount = request.form['amount']
        reciever = request.form['reciever']

        write_block(sender, amount, reciever)
        return redirect(url_for('index'))

    return render_template('index.html')


@app.route('/checking', methods=['GET'])
def check():
    print 'lala'
    # result_arr = check_integrity()
    result_arr = [
      {
        "block": 1,
        "result": "ok"
      },
      {
        "block": 2,
        "result": "ok"
      },
      {
        "block": 2,
        "result": "ok"
      }
    ]
    return render_template('index.html', result_arr=result_arr)


if __name__ == '__main__':
    app.run(debug=True)