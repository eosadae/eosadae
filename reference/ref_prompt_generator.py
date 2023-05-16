from textwrap import dedent


class PromptWriterSooni:
    def __init__(self):
        self.category = ''
        self.topic = ''
        self.additional_request = ''

        self.feedback_score = 3  # given score (stars) in range of (1, 5)
        self.feedback_text = ''

        self.created_script_idx = 1

        self.prompt_brief_general_policy = ''
        self.prompt_detiled_general_policy = ''

        self.prompt_brief_script_policy = ''
        self.prompt_detailed_script_policy = ''

        self.prompt_after_policy = ''

        self.prompt_example_script = ''

        self.prompt_guideline_by_line = ''
        self.prompt_guideline_by_order = ''
        self.prompt_guideline_by_trait = ''

        self.prompt_generate = ''

        self.prompt_check_policy = ''

        self.script_list = []
        self.ongoing_script = ''
        self.final_script = ''

        self.prompt_continue_writing = ''

        self.prompt_for_image = ''

    def get_user_input(self, category, topic, additional_request):
        self.category = category
        self.topic = topic
        self.additional_request = additional_request

    def get_feedback(self, feedback_score, feedback_text):
        self.feedback_score = feedback_score
        self.feedback_text = feedback_text

    def get_policy(self):

        self.prompt_brief_general_policy = prompt_before_general_policy + brief_general_policy
        self.prompt_detailed_general_policy = prompt_before_general_policy + detailed_general_policy
        self.prompt_brief_script_policy = prompt_before_script_policy + brief_script_policy
        self.prompt_detailed_script_policy = prompt_before_script_policy + detailed_script_policy

    def set_prompt_after_policy(self, example_script_exists=True):
        prompt_with_example_script = "Now, I'll give you a guideline & example script for given category & topic."
        prompt_without_example_script = "Now, I'll give you a guideline for given category & topic."

        if example_script_exists:
            self.prompt_after_policy = dedent(f"""
            Here is the information for script you'll write today.

            Category: {self.category}
            Topic: {self.topic}

            {prompt_with_example_script}
            """)

        else:
            self.prompt_after_policy = dedent(f"""
            Here is the information for script you'll write today.

            Category: {self.category}
            Topic: {self.topic}

            {prompt_without_example_script}
            """)

    def get_guideline(self):
        file_name_guideline_by_line = f'prompt/guideline/{self.category}/{self.topic}_guideline_by_line.txt'
        file_name_guideline_by_order = f'prompt/guideline/{self.category}/{self.topic}_guideline_by_order.txt'
        file_name_guideline_by_trait = f'prompt/guideline/{self.category}/{self.topic}_guideline_by_trait.txt'

    def continue_writing(self):
        if self.script_list[-1][-3:] == '<끝>':
            self.ongoing_script += self.script_list[-1][:-3]
            self.final_script = self.ongoing_script

        else:
            self.ongoing_script += self.script_list[-1]

            self.prompt_continue_writing = dedent(f"""
            this is what you have written so far:

            {self.ongoing_script}

            continue writing the script.
            """)

    def create_prompt_for_model_2(self, category, topic, additional_request):
        self.get_user_input(category, topic, additional_request)
        self.get_policy()
        self.set_prompt_after_policy()
        self.get_example_script()
        self.get_guideline()
        self.set_prompt_generate()

        final_prompt = dedent(f"""{self.prompt_detailed_general_policy}

        {self.prompt_detailed_script_policy}

        {self.prompt_after_policy}

        {self.prompt_example_script}

        {self.prompt_guideline_by_order}

        {self.prompt_generate}""")

    def create_prompt_for_image(self, keyword):
        pass