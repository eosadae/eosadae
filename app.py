# -*coding: utf-8 -*
# app.py

from flask import Flask, request, render_template, jsonify
from modules.user_input_getter import UserInputGetterSooni
from generate_script import generate_script
from regenerate_script import regenerate_script
from generate_image import generate_image
from generate_title_and_description import get_title_and_description

app = Flask(__name__)
 
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/user_input', methods=['POST'])
def get_user_input():
    data = request.get_json()
    user_input = {
        'category': data.get('category', ''),
        'topic': data.get('topic', ''),
        'additional_request': data.get('additional_request', ''),
        'feedback_score': data.get('feedback_score', ''),
        'feedback_text': data.get('feedback_text', '')
    }

    initial_prompt, final_script = generate_script(user_input)  # generate_script 함수 호출
    title, description = get_title_and_description(final_script)

    print("Initial Prompt:", initial_prompt)
    print("Final Script:", final_script)
    print("Title:", title)
    print("Description:", description)

    return jsonify({'script': final_script, 'title': title, 'description': description}), 200

@app.route('/image_input', methods=['POST'])
def get_image_input():
    data = request.get_json()
    user_input = {
        'image_keyword': data.get('image_keyword', ''),
    }

    final_image = generate_image(user_input)  # regenerate_script 함수 호출

    print("Final Image URL:", final_image)
    return jsonify({'script': final_image}), 200

@app.route('/regenerate_input', methods=['POST'])
def get_regeneration_input():
    data = request.get_json()
    user_input = {
        'category': data.get('category', ''),
        'topic': data.get('topic', ''),
        'additional_request': data.get('additional_request', ''),
        'feedback_score': data.get('feedback_score', ''),
        'feedback_text': data.get('feedback_text', '')
    }

    refinal_script = regenerate_script(user_input)  # regenerate_script 함수 호출

    print("Refinal Script:", refinal_script)

    return jsonify({'script': refinal_script}), 200

if __name__ == "__main__":
    app.run(debug=True)
