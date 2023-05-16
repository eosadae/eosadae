"""abstract.py의 AbstractApiImageReceiver 클래스 참고"""
from modules.abstract import AbstractApiImageReceiver

class ApiImageReceiverSooni(AbstractApiImageReceiver):
    """GPT API에서 받은 답변에서 이미지를 추출함"""
    def __init__(self, response):
        self.response = response
        self.content = self.response['choices'][0]['message']['content']

        self.start = self.content.find('http')
        self.end = self.content.find(')', self.start)

        self.image_url = self.content[self.start:self.end]
