#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<par>')
def print_string(par):
     print(par)
     return par

@app.route('/count/<int:parameter>')
def count(parameter):
    for num in range(parameter):
      result = ""
      for num in range(parameter):
        result += str(num) + '\n'
      return result
    
@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation,num2):
    if operation == '+':
       result = num1+num2
    elif operation == '-':
        result = num1-num2
    elif operation == '*':
        result = num1*num2
    elif operation == 'div':
        result = num1/num2
    elif operation == '%':
        result = num1%num2
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
