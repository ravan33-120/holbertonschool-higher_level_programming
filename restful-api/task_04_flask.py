#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

# Empty dictionary as required (NO testing data!)
users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/status")
def status():
    return "OK"

@app.route("/data")
def get_usernames():
    # Return list of usernames
    return jsonify(list(users.keys()))

@app.route("/users/<username>")
def get_user(username):
    # Check if user exists
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    # Return full user object including username
    user_data = users[username].copy()
    user_data["username"] = username
    return jsonify(user_data)

@app.route("/add_user", methods=["POST"])
def add_user():
    # Attempt to parse JSON
    try:
        data = request.get_json()
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    # If JSON is None → invalid or missing JSON
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    # Check for username
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Check for duplicate username
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Save user data (except username itself)
    users[username] = {
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    # Return confirmation
    return jsonify({
        "message": "User added",
        "user": {
            "username": username,
            "name": data.get("name"),
            "age": data.get("age"),
            "city": data.get("city")
        }
    }), 201


if __name__ == "__main__":
    app.run()

