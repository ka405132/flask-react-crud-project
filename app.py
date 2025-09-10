from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

DB_FILE = './data/database.db'

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/items', methods=['GET'])
def get_items():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM items')
    items = cursor.fetchall()
    conn.close()
    return jsonify([{'id': i[0], 'name': i[1], 'quantity': i[2]} for i in items])

@app.route('/items', methods=['POST'])
def add_item():
    data = request.json
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO items (name, quantity) VALUES (?, ?)', (data['name'], data['quantity']))
    conn.commit()
    conn.close()
    return jsonify({'status':'ok'}), 201

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.json
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('UPDATE items SET name=?, quantity=? WHERE id=?', (data['name'], data['quantity'], item_id))
    conn.commit()
    conn.close()
    return jsonify({'status':'ok'})

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM items WHERE id=?', (item_id,))
    conn.commit()
    conn.close()
    return jsonify({'status':'ok'})

@app.route('/health', methods=['GET'])
def health():
    return {'status': 'ok'}, 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
