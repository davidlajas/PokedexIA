from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

from database import init_db, save_query
from llm import generate_response

app = Flask(__name__, static_folder="../frontend", static_url_path="")
CORS(app)


init_db()


@app.route("/")
def home():
    return send_from_directory(app.static_folder, "index.html")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    term = data.get("message", "").strip()

    if not term:
        return jsonify({"error": "Mensaje vacío"}), 400

    response = generate_response(term)


    save_query(term, response)

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)









