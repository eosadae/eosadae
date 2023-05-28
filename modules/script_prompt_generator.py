"""abstract.py의 AbstractScriptPromptGenerator 클래스 참고"""
from modules.abstract import AbstractScriptPromptGenerator
from modules.user_input_getter import UserInputGetterSooni
from modules.prompt_data_getter import PromptDataGetterSooni
from modules.ready_made_prompt_getter import ReadyMadePromptGetterSooni

class ScriptPromptGeneratorSooni(AbstractScriptPromptGenerator):
    """대본 생성용 프롬프트 제작"""
<<<<<<< HEAD
    def __init__(self,data):
        self.user_input = UserInputGetterSooni(data)
        #self.user_input.get_basic_input()
=======
    def __init__(self):
        self.user_input = UserInputGetterSooni()
        self.user_input.get_basic_input()
>>>>>>> 4f6cd6af505c79bf1c92710beea504b55cd0f369

        self.prompt_data = PromptDataGetterSooni(self.user_input.category, self.user_input.topic)
        self.prompt_data.get_every_data(\
            guideline_type='order', general_policy_type='detailed', script_policy_type='detailed')

        self.ready_made_prompt = \
          ReadyMadePromptGetterSooni(self.user_input.category, self.user_input.topic)
        self.ready_made_prompt.generate_prompt_after_script_policy()

        self.final_prompt = ''

    def generate_script_prompt(self):
        self.final_prompt = \
        self.ready_made_prompt.prompt_before_general_policy + \
        self.prompt_data.general_policy_data + \
        self.ready_made_prompt.prompt_before_script_policy + \
        self.prompt_data.script_policy_data + \
        self.ready_made_prompt.prompt_after_script_policy + \
        self.ready_made_prompt.prompt_before_example_script + \
        self.prompt_data.example_script_data + \
        self.ready_made_prompt.prompt_before_guideline + \
        self.prompt_data.guideline_data + \
        self.ready_made_prompt.prompt_after_guideline
