"""abstract.py의 AbstractRegenerationPromptGenerator 클래스 참고"""
from modules.abstract import AbstractRegenerationPromptGenerator
from modules.user_input_getter import UserInputGetterSooni
from modules.ready_made_prompt_getter import ReadyMadePromptGetterSooni

class RegenerationPromptGeneratorSooni(AbstractRegenerationPromptGenerator):
<<<<<<< HEAD
    def __init__(self, original_prompt, original_script, data):
        self.original_prompt = original_prompt
        self.original_script = original_script

        self.user_input = UserInputGetterSooni(data)
        #self.user_input.get_feedback_input()
=======
    def __init__(self, original_prompt, original_script):
        self.original_prompt = original_prompt
        self.original_script = original_script

        self.user_input = UserInputGetterSooni()
        self.user_input.get_feedback_input()
>>>>>>> 4f6cd6af505c79bf1c92710beea504b55cd0f369

        self.ready_made_prompt = ReadyMadePromptGetterSooni(None, None)

        self.final_regeneration_prompt = ''

    def generate_regeneration_prompt(self):
        self.final_regeneration_prompt = \
        self.ready_made_prompt.regeneration_prompt_before_original_script + \
        self.original_script + \
        self.ready_made_prompt.regeneration_prompt_before_original_prompt + \
        self.original_prompt + \
        self.ready_made_prompt.regeneration_prompt_before_feedback_score + \
        self.user_input.feedback_score + \
        self.ready_made_prompt.regeneration_prompt_before_feedback_text + \
        self.user_input.feedback_text + \
        self.ready_made_prompt.regeneration_prompt_after_feedback_text
