#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return f'{parameter}'

@app.route('/count/<int:number>')
def count(number):
    for x in range(number):
        return f'{x}\n'

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    return f'{num1} {operation} {num2}'