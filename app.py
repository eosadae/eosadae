
# -*coding: utf-8 -*
# app.py

from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)

openai.api_key = ''

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data['prompt']

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )

    return jsonify({
        'response': response.choices[0]['message']['content']
    })

if __name__ == '__main__':
    app.run(port=5000, debug=True)