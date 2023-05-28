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
