"""abstract.py의 AbstractReadyMadePromptGetter 클래스 참고"""
from textwrap import dedent
from modules.abstract import AbstractReadyMadePromptGetter

class ReadyMadePromptGetterSooni(AbstractReadyMadePromptGetter):
    """기본적으로 항상 동일하게 사용하는 프롬프트 저장"""
    def __init__(self, category, topic):
        self.category = category
        self.topic = topic

        self.prompt_before_general_policy = 'Imagine: \n'
        self.prompt_before_script_policy = 'When writing a script, follow the policy below: \n'
        self.prompt_after_script_policy = ''
        self.prompt_before_example_script = 'Here is an example script you can use as reference: \n'
        self.prompt_before_guideline = '\n\nHere is an guideline you should follow: \n'
        self.prompt_after_guideline = dedent("""
            \nNow, write a script that follows the policy and guideline using example script I gave you.
            Do not forget to insert <END> in the end of your script.
            <RUN>
            """)

        self.check_prompt_before_original_script = 'this is the script I have. \n'
        self.check_prompt_before_guideline = 'this is the guideline for the script. \n'
        self.check_prompt_before_general_policy = 'this is the policy for the script. \n'
        self.check_prompt_after_script_policy = \
          'Correct the script so that it can follow guideline and policy properly.'

    def generate_prompt_after_script_policy(self):
        self.prompt_after_script_policy = \
          dedent(f"""Now, I'll give you a guideline & example script for given category & topic.
          
          Here is the information for script you'll write today.

          Category: {self.category}
          Topic: {self.topic}

          """)
