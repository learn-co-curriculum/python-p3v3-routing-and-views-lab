#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/greet/<string:name>')
def greet(name):
    return f'<p>Welcome {name}!</p>'

@app.route('/count/<int:number>')
def count(number):
    response = '<ul>'
    for n in range(number):
        response += f'<li>{n}</li>'
    response += '</ul>'
    return response

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, num2, operation):
    result = 0
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result =num1 % num2
    else:
        return '<p>Operation not recognized.</p>'
    return f'<h2>{num1}{operation}{num2}={result}</h2>'
    
if __name__ == '__main__':
    app.run(port=5555, debug=True)