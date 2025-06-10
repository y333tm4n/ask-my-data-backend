from flask import Blueprint, request, jsonify
from .file_parser import parse_file
from .gemini_chain import ask_gemini

main = Blueprint('main', __name__)

@main.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    text = parse_file(file)
    return jsonify({"parsed_text": text})

@main.route('/ask', methods=['POST'])
def ask():
    question = request.json.get("question")
    response = ask_gemini(question)
    return jsonify({"response": response})
