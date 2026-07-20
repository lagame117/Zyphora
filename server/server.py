import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite conexiones desde la app cliente

# Almacenamiento temporal en memoria
mensajes_db = []

@app.route('/')
def home():
    return jsonify({
        "status": "Zyphora Server Online 🚀",
        "encryption": "End-to-End (E2EE) Active",
        "total_messages": len(mensajes_db)
    })

@app.route('/send', methods=['POST'])
def send_message():
    data = request.get_json() or {}
    
    sender = data.get("sender")
    recipient = data.get("recipient")
    encrypted_content = data.get("encrypted_content")
    
    if not sender or not recipient or not encrypted_content:
        return jsonify({"error": "Faltan datos obligatorios"}), 400
        
    nuevo_mensaje = {
        "id": len(mensajes_db) + 1,
        "sender": sender,
        "recipient": recipient,
        "encrypted_content": encrypted_content
    }
    
    mensajes_db.append(nuevo_mensaje)
    return jsonify({
        "status": "ok", 
        "msg": "Mensaje encriptado recibido", 
        "id": nuevo_mensaje["id"]
    }), 201

@app.route('/get_messages/<username>', methods=['GET'])
def get_messages(username):
    user_messages = [
        msg for msg in mensajes_db 
        if msg["recipient"] == username or msg["sender"] == username
    ]
    return jsonify({"messages": user_messages}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
