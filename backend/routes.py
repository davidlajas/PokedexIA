from flask import Blueprint, request, jsonify, render_template
from llm import generate_response
from database import save_query, get_history

api = Blueprint("api", __name__)

@api.route("/")
def home():
    return render_template("index.html")

@api.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    if not data or "question" not in data:
        return jsonify({"error": "No question provided"}), 400

    question = data["question"]
    response = generate_response(question)

    save_query(question, response)

    return jsonify({"answer": response})

@api.route("/history")
def history():
    rows = get_history()
    return jsonify(
        [{"term": term, "response": resp} for term, resp in rows]
    )







