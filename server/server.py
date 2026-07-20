import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"status": "Zyphora Server Online"})

if __name__ == '__main__':
    # Railway requiere que el puerto se tome de las variables de entorno
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
