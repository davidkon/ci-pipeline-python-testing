from flask import Flask, jsonify, request
"""
app.py

A simple Flask web application that provides a RESTful API for managing a list of items.
The application uses an in-memory data store to keep track of items, each with an 'id' and a 'name'.

Endpoints:
    - GET /: Returns a welcome message.
    - GET /api/items: Returns a list of all items.
    - GET /api/items/<item_id>: Returns a specific item by its ID.
    - POST /api/items: Adds a new item with a specified name.

This app is intended for demonstration and testing purposes only.
"""

app = Flask(__name__)

# Simple in-memory data store
items = [
    {"id": 1, "name": "Item One"},
    {"id": 2, "name": "Item Two"}
]

@app.route('/')
def index():
    return "Welcome to the Dummy App!"

@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({"error": "Item not found"}), 404

@app.route('/api/items', methods=['POST'])
def add_item():
    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"error": "Name is required"}), 400
    new_id = max(item["id"] for item in items) + 1 if items else 1
    new_item = {"id": new_id, "name": data["name"]}
    items.append(new_item)
    return jsonify(new_item), 201

if __name__ == '__main__':
    app.run(debug=True)
