from flask import Flask, render_template, request, jsonify
import markdown
from gemini_client import get_ai_reply  # Custom response function

app = Flask(__name__)  # Moved here before route definitions

# Initalize Gemini Call

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data["message"]
    conversation = data.get("conversation", [])
    
    reply, updated_convo = get_ai_reply(user_message, conversation)
    reply_html = markdown.markdown(reply)  # Convert markdown to HTML

    return jsonify({"reply": reply_html, "conversation": updated_convo})

if __name__ == "__main__":
    app.run(debug=True)