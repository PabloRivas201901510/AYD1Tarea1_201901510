from flask import Flask
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# FIRST ROUTE TO THE SERVER
@app.route('/')
def initServer(): 
    return {
        'response':'Servidor corriendo'
    }

@app.route('/suma', methods = ['POST'])
def suma():
    num1 = int(request.json['num1'])
    num2 = int(request.json['num2'])
    return str(num1+num2)

# STARTING THE SERVER
if (__name__ == '__main__'):
    app.run(host='0.0.0.0', port = 3000, debug = True)