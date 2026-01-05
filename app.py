from flask import Flask, render_template, request, jsonify
from project import get_answer

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("chat.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    user_question = data.get("question", "")
    answer = get_answer(user_question)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
