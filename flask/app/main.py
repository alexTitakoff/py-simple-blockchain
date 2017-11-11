# coding=utf-8
from flask import Flask
from flask import render_template
from flask import request
from block import *      # импортируем наш блокчейн скрипт

import os     #для дебага

app = Flask(__name__)


@app.route('/', methods=['POST', 'GEt'])
def index():

    print(os.curdir)

    if request.method == 'POST':
        sender = request.form['sender']
        amount = request.form['amount']
        reciever = request.form['reciever']

        write_block(sender,amount,reciever)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)