"""abstract.py의 AbstractApiPromptSender 클래스 참고"""
import os
import openai
from dotenv import load_dotenv

from modules.abstract import AbstractApiPromptSender

class ApiPromptSenderSooni(AbstractApiPromptSender):
    """GPT API에 프롬프트 전송"""
    def __init__(self):
        self.api_key = ''
        self.prompt = ''
        self.response = ''
        self.image_response = ''
        self.title_response = ''
        self.description_response = ''

    def get_api_key(self):
        load_dotenv()
        self.api_key = os.getenv('OPENAI_API_KEY')
        openai.api_key = self.api_key

    def get_prompt(self, prompt):
        self.prompt = prompt

    def generate_response(self, prompt):
        self.get_api_key()
        self.get_prompt(prompt)

        self.response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[{"role": "user", "content": self.prompt}],
            temperature=0,
            max_tokens=2048,
        )

    def generate_image_response(self, prompt):
        self.get_api_key()
        self.get_prompt(prompt)

        self.image_response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[{"role": "user", "content": self.prompt}],
            temperature=0,
            max_tokens=2048,
        )

    def generate_title_response(self, prompt):
        self.get_api_key()
        self.get_prompt(prompt)

        self.title_response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[{"role": "user", "content": self.prompt}],
            temperature=0,
            max_tokens=2048,
        )

    def generate_description_response(self, prompt):
        self.get_api_key()
        self.get_prompt(prompt)

        self.description_response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[{"role": "user", "content": self.prompt}],
            temperature=0,
            max_tokens=2048,
        )

    def get_result_script(self, category, topic):
        BASE_ADDRESS = 'C:\\Users\\JongbeenSong\\Desktop\\23-1\\캡스톤 설계 및 실습\\eosadae-main\\data\\result_script'
        FILE_ADDRESS = BASE_ADDRESS + f'\\{category}\\{topic}\\{topic}_result_script.txt'
        with open(FILE_ADDRESS, 'r', encoding='utf-8') as f:
            self.response = f.read()
        print(self.response)

    def get_result_remake_script(self, category, topic):
        BASE_ADDRESS = 'C:\\Users\\JongbeenSong\\Desktop\\23-1\\캡스톤 설계 및 실습\\eosadae-main\\data\\result_script'
        FILE_ADDRESS = BASE_ADDRESS + f'\\{category}\\{topic}\\{topic}_result_remake_script.txt'
        with open(FILE_ADDRESS, 'r', encoding='utf-8') as f:
            self.response = f.read()
        print(self.response)
