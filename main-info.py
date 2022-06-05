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

@app.route('/info', methods = ['GET'])
def info():
    return "<h2>Nombre: Pablo Daniel Rivas Marroquin</h2> \n <h3>Carne: 201901510</h3>"

# STARTING THE SERVER
if (__name__ == '__main__'):
    app.run(host='0.0.0.0', port = 4000, debug = True)