"""abstract.py의 AbstractUserInputGetter 클래스 참고"""
from modules.abstract import AbstractUserInputGetter

class UserInputGetterSooni(AbstractUserInputGetter):
    """사용자의 입력을 받음. 웹 구현까지 우선 set_example_attribute() 활용"""
<<<<<<< HEAD
    def __init__(self,data):
        self.category = data.get('category', '')
        self.topic = data.get('topic', '')
        self.additional_request = data.get('additional_request', '')

        self.feedback_score = data.get('feedback_score', '')
        self.feedback_text = data.get('feedback_text', '')

        self.keyword_for_image = '꽃'
=======
    def __init__(self):
        self.category = ''
        self.topic = ''
        self.additional_request = ''

        self.feedback_score = 0
        self.feedback_text = ''

        self.keyword_for_image = ''

    def get_basic_input(self):
        self.set_example_attribute()

    def get_feedback_input(self):
        # 피드백 점수 int 아니고 str 되도록 신경쓰기
        self.set_example_attribute()

    def get_keyword_input(self):
        self.set_example_attribute()

    def set_example_attribute(self):
        self.category = '힐링'
        self.topic = '꽃말_수업'
        self.additional_request = '꽃 중에 장미꽃은 제외해줘.'

        self.feedback_score = '4'
        self.feedback_text = '지금 다 좋은데, 표현이 중복되는게 많아서 조금 더 다채롭게 말해봐.'

        self.keyword_for_image = '꽃'
