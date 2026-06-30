from flask import Flask, render_template, request, jsonify

print("SCRIPT STARTED")

app = Flask(__name__)

# Simple keyword-based intent matching (our "NLP" logic for v1)
intents = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! What can I do for you?",
    "hours": "We are open from 9 AM to 6 PM, Monday to Saturday.",
    "price": "Our pricing depends on the service. Could you tell me which product you're asking about?",
    "contact": "You can reach us at support@example.com or call +91-XXXXXXXXXX.",
    "bye": "Goodbye! Have a great day!",
    "thanks": "You're welcome! Let me know if you need anything else.",
}

def get_response(user_message):
    user_message = user_message.lower()
    for keyword, response in intents.items():
        if keyword in user_message:
            return response
    return "I'm not sure I understand. Could you rephrase that, or ask about hours, pricing, or contact info?"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    bot_response = get_response(user_message)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)