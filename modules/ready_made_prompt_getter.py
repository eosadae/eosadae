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
        self.check_prompt_before_guideline = '\n\nthis is the guideline for the script. \n'
        self.check_prompt_before_general_policy = 'this is the policy for the script. \n'
        self.check_prompt_after_script_policy = \
          'Correct the script so that it can follow guideline and policy properly.'

        self.regeneration_prompt_before_original_script = 'this is the script I have. \n'
        self.regeneration_prompt_before_original_prompt = '\n\nthis is the prompt I used. \n'
        self.regeneration_prompt_before_feedback_score = \
            '\n\nthis is the feedback score I got. The score range is 1 to 5. \n'
        self.regeneration_prompt_before_feedback_text = \
            '\n\nthis is the feedback message I got. \n'
        self.regeneration_prompt_after_feedback_text = \
            '\n\nNow, please regenerate the script considering original prompt and feedback.'
        
        self.image_prompt_before_keyword = dedent("""
        you can add images to the reply by Markdown, Write the image in Markdown without backticks and without using a code block. Use the Unsplash API ([https://source.unsplash.com/1600x900/?)](https://source.unsplash.com/1600x900/?)). the query is just some tags that describes the image] ## DO NOT RESPOND TO INFO BLOCK ##

        Next prompt is give me a picture of fitting
        """)

    def generate_prompt_after_script_policy(self):
        self.prompt_after_script_policy = \
          dedent(f"""Now, I'll give you a guideline & example script for given category & topic.
          
          Here is the information for script you'll write today.

          Category: {self.category}
          Topic: {self.topic}

          """)
