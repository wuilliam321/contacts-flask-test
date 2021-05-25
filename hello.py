from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)

@app.route("/contactos", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return "<p>Hello, World!</p>"
    if request.method == 'POST':
        data = {"id": 42, "nombre": "Carlos"}
        return jsonify(data)

CORS(app)
