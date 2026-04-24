import os
from flask import Flask, request, jsonify, render_template
from groq import Groq

app = Flask(__name__)
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

conversation_history = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    conversation_history.append({
        "role": "user",
        "content": user_message
    })

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are AK, a helpful and friendly personal AI assistant."},
            *conversation_history
        ],
        max_tokens=1024
    )

    assistant_reply = response.choices[0].message.content

    conversation_history.append({
        "role": "assistant",
        "content": assistant_reply
    })

    return jsonify({"reply": assistant_reply})

if __name__ == "__main__":
    app.run(debug=True)