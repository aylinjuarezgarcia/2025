from flask import Flask, jsonify, request

app = Flask(__name__)

# Base de datos simulada
users_db = [
    {"id": 1, "name": "John Doe", "email": "john@example.com"}
]

# Obtener todos los usuarios
@app.route("/users", methods=["GET"])
def get_users():
    print('get users')
    return jsonify(users_db)

# Obtener un usuario por ID
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    for user in users_db:
        if user["id"] == user_id:
            return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# Crear un usuario
@app.route("/users", methods=["POST"])
def create_user():
    user = request.get_json()
    users_db.append(user)
    return jsonify(user), 201

# Actualizar un usuario
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    updated_user = request.get_json()
    for index, user in enumerate(users_db):
        if user["id"] == user_id:
            users_db[index] = updated_user
            return jsonify(updated_user)
    return jsonify({"error": "User not found"}), 404

# Eliminar un usuario
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    for index, user in enumerate(users_db):
        if user["id"] == user_id:
            del users_db[index]
            return jsonify({"message": "User deleted successfully"})
    return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
