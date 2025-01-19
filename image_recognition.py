from flask import Flask, request, jsonify, render_template
from chatbot import handle_text_message, handle_image_and_generate_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    message = request.form.get('message')
    image = request.files.get('image')

    if image:
        response = handle_image_and_generate_response(image)
    elif message:
        response = handle_text_message(message)
    else:
        response = "No message or image received."

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)

