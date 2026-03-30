from flask import Flask, render_template, request, jsonify
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

# Initialize Flask app
app = Flask(__name__)

# Basic greeting and exit responses
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey")
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]
EXIT_INPUTS = ("bye", "goodbye", "exit", "quit", "see ya", "later")

def chatbot_response(user_input):
    # Process user input with NLTK
    tokens = word_tokenize(user_input.lower())
    
    # Filter out stopwords and punctuation
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [w for w in tokens if not w in stop_words and w not in string.punctuation]

    # Check for exit words
    for word in tokens:
        if word in EXIT_INPUTS:
            return "Chatbot: Goodbye! Have a great day!"
    
    # Check for greetings
    for word in tokens:
        if word in GREETING_INPUTS:
            import random
            return f"Chatbot: {random.choice(GREETING_RESPONSES)}"
            
    if "year" in tokens:
        return "Chatbot: It is 2026!"
    elif "name" in tokens:
        return "Chatbot: I am your first NLTK-enhanced chatbot running on Flask."
    else:
        return "Chatbot: I don't quite understand that. Can you rephrase? (Using NLTK tokenization!)"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"response": "Error: No message provided."}), 400
    
    response = chatbot_response(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)