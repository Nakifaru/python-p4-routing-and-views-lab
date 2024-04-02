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
    numbers = ''
    for x in range(number):
        numbers += str(x) + '\n'
    return numbers

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    # if operation == 'div':
    #     return str(num1 / num2)
    # answer = eval(str(num1) + str(operation) + str(num2))
    # return answer
    if operation == '+':
        return str(num1 + num2)
    elif operation == '-':
        return str(num1 - num2)
    elif operation == 'div':
        return str(num1 / num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == '%':
        return str(num1 % num2)
