from flask import Flask, request, render_template, jsonify
import json

app = Flask(__name__)

with open("dictionary.json", "r") as file:
    data = json.load(file)

def translate(word):
    if word not in data:
        return {"error": "No such word! Please try again."}
    else:
        return {"translation": data[word]}

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/translate")
def translate_route():
    word = request.args.get('word')
    if not word:
        return jsonify({"error": "No word provided"}), 400
    # Check if the input contains multiple words
    if len(word.split()) > 1:
        return jsonify({"error": "Please enter a single word"}), 400
    result = translate(word)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
