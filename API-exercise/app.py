from flask import Flask, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return 'This is a sample template created for this workshop'

# create a post request that takes in 2 numbers and add them together
@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return str(num1 + num2)

# create a post request that takes in 2 numbers and subtracts them
@app.route('/subtract/<int:num1>/<int:num2>')
def subtract(num1, num2):
    return str(num1 - num2)

# create a post request that takes in 2 numbers and add them but this time in the body
@app.route('/addBody', methods=['POST'])
def add2():
    data = request.json  # Assuming the request body contains JSON data
    print(data)
    num1 = data.get('num1')
    num2 = data.get('num2')

    if num1 is not None and num2 is not None:
        result = num1 + num2
        return str(result)
    else:
        return "Invalid input data"

if __name__ == '__main__':
    app.run(debug=True, port=8080)
