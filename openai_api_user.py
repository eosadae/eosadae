import os
import openai

from dotenv import load_dotenv


class ApiUserSooni:
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

    def create_response(self, prompt):
        self.get_api_key()
        self.get_prompt(prompt)

        self.final_response = openai.Completion.create(
            model='gpt-3.5-turbo',
            prompt=self.prompt,
            temperature=0,
            max_tokens=2048,
        )
