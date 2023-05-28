"""abstract.py의 AbstractImagePromptGenerator 클래스 참고"""
from modules.abstract import AbstractImagePromptGenerator
from modules.user_input_getter import UserInputGetterSooni
from modules.ready_made_prompt_getter import ReadyMadePromptGetterSooni

class ImagePromptGeneratorSooni(AbstractImagePromptGenerator):
    """이미지 생성용 프롬프트 제작"""
<<<<<<< HEAD
    def __init__(self, data):
        self.user_input = UserInputGetterSooni(data)
        #self.user_input.get_keyword_input()
=======
    def __init__(self):
        self.user_input = UserInputGetterSooni()
        self.user_input.get_keyword_input()
>>>>>>> 4f6cd6af505c79bf1c92710beea504b55cd0f369

        self.ready_made = ReadyMadePromptGetterSooni(None, None)

        self.final_prompt = ''

    def generate_image_prompt(self):
        self.final_prompt = \
          self.ready_made.image_prompt_before_keyword + \
          self.user_input.keyword_for_image
