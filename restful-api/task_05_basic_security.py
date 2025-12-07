#!/usr/bin/python3
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
    get_jwt
)

app = Flask(__name__)

# ==============================
# JWT Konfiqurasiyası
# ==============================
app.config["JWT_SECRET_KEY"] = "super-secret-key-change-me"  # normalda env-dən gəlməlidir
jwt = JWTManager(app)

# ==============================
# Basic Auth Konfiqurasiyası
# ==============================
auth = HTTPBasicAuth()

# ==============================
# İstifadəçi məlumatları (yaddaşda)
# ==============================
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user",
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin",
    },
}


# ==============================
# BASIC AUTH – istifadəçi yoxlama
# ==============================
@auth.verify_password
def verify_password(username, password):
    """
    Basic Auth üçün istifadəçi adı və şifrəni yoxlayır.
    Doğrudursa, username return olunur, yoxsa None.
    """
    user = users.get(username)
    if not user:
        return None
    if not check_password_hash(user["password"], password):
        return None
    return username  # bu dəyəri auth.current_user() ilə oxumaq olur


@auth.error_handler
def basic_auth_error():
    """
    Basic Auth uğursuz olanda cavab.
    """
    return jsonify({"error": "Invalid basic authentication credentials"}), 401


# ==============================
# JWT ERROR HANDLER-lər (hamısı 401 qaytarır)
# ==============================
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401


# ==============================
# BASIC AUTH ilə qorunan endpoint
# ==============================
@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


# ==============================
# JWT LOGIN – token almaq
# ==============================
@app.route("/login", methods=["POST"])
def login():
    """
    Body JSON formatında olmalıdır:
    {
        "username": "user1",
        "password": "password"
    }
    """
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    user = users.get(username)
    if user is None or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Rol-u tokenin içində saxlayırıq
    additional_claims = {"role": user["role"]}
    access_token = create_access_token(identity=username, additional_claims=additional_claims)

    return jsonify({"access_token": access_token}), 200


# ==============================
# JWT ilə qorunan endpoint
# ==============================
@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


# ==============================
# ADMIN ONLY endpoint (rol yoxlamalı)
# ==============================
@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """
    Tokenin içindən rol-u oxuyuruq.
    Əgər admin deyilsə → 403
    """
    claims = get_jwt()
    role = claims.get("role")

    if role != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run()

