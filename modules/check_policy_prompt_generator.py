"""abstract.py의 AbstractCheckPolicyPromptGenerator 클래스 참고"""
from modules.abstract import AbstractCheckPolicyPromptGenerator
from modules.prompt_data_getter import PromptDataGetterSooni
from modules.ready_made_prompt_getter import ReadyMadePromptGetterSooni

class CheckPolicyPromptGeneratorSooni(AbstractCheckPolicyPromptGenerator):
    """정책 채점용 프롬프트 제작"""
    def __init__(self, category, topic, original_script):
        self.category = category
        self.topic = topic
        self.original_script = original_script

        self.prompt_data = PromptDataGetterSooni(self.category, self.topic)
        self.prompt_data.get_every_data(\
            guideline_type='order', general_policy_type='detailed', script_policy_type='detailed')

        self.ready_made_prompt = ReadyMadePromptGetterSooni(self.category, self.topic)
        self.ready_made_prompt.generate_prompt_after_script_policy()

        self.check_policy_prompt = ''

    def generate_check_policy_prompt(self):
        self.check_policy_prompt = \
        self.ready_made_prompt.check_prompt_before_original_script + \
        self.original_script + \
        self.ready_made_prompt.check_prompt_before_guideline + \
        self.prompt_data.guideline_data + \
        self.ready_made_prompt.check_prompt_before_general_policy + \
        self.prompt_data.general_policy_data + \
        self.prompt_data.script_policy_data + \
        self.ready_made_prompt.check_prompt_after_script_policy
