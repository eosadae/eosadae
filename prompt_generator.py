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
        file_name_brief_general_policy = 'prompt/policy/brief_general_policy.txt'
        file_name_detailed_general_policy = 'prompt/policy/detailed_general_policy.txt'
        file_name_brief_script_policy = 'prompt/policy/brief_script_policy.txt'
        file_name_detailed_script_policy = 'prompt/policy/detailed_script_policy.txt'

        prompt_before_general_policy = 'Imagine: \n'
        prompt_before_script_policy = 'When writing a script, follow the policy below: \n'

        with open(file_name_brief_general_policy, 'r', encoding='UTF8') as f:
            brief_general_policy = f.read()

        with open(file_name_detailed_general_policy, 'r', encoding='UTF8') as f:
            detailed_general_policy = f.read()

        with open(file_name_brief_script_policy, 'r', encoding='UTF8') as f:
            brief_script_policy = f.read()

        with open(file_name_detailed_script_policy, 'r', encoding='UTF8') as f:
            detailed_script_policy = f.read()

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

    def get_example_script(self):
        file_name_example_script = f'prompt/example_script/{self.category}/{self.topic}_example_script.txt'

        prompt_before_example_script = 'Here is an example script you can use as reference: \n'

        with open(file_name_example_script, 'r', encoding='UTF8') as f:
            example_script = f.read()

        self.prompt_example_script = prompt_before_example_script + example_script

    def get_guideline(self):
        file_name_guideline_by_line = f'prompt/guideline/{self.category}/{self.topic}_guideline_by_line.txt'
        file_name_guideline_by_order = f'prompt/guideline/{self.category}/{self.topic}_guideline_by_order.txt'
        file_name_guideline_by_trait = f'prompt/guideline/{self.category}/{self.topic}_guideline_by_trait.txt'

        prompt_before_guideline = 'Here is an guideline you should follow: \n'

        with open(file_name_guideline_by_line, 'r', encoding='UTF8') as f:
            guideline_by_line = f.read()

        with open(file_name_guideline_by_order, 'r', encoding='UTF8') as f:
            guideline_by_order = f.read()

        with open(file_name_guideline_by_trait, 'r', encoding='UTF8') as f:
            guideline_by_trait = f.read()

        self.prompt_guideline_by_line = prompt_before_guideline + guideline_by_line
        self.prompt_guideline_by_order = prompt_before_guideline + guideline_by_order
        self.prompt_guideline_by_trait = prompt_before_guideline + guideline_by_trait

    def set_prompt_generate(self, example_script_exists=True):
        if example_script_exists:
            self.prompt_generate = dedent(f"""
            Now, write a script that follows the policy and guideline using example script I gave you.
            Do not forget to insert <끝> in the end of your script.
            <RUN>
            """)
        else:
            self.prompt_generate = dedent(f"""
            Now, write a script that follows the policy and guideline I gave you.
            Do not forget to insert <끝> in the end of your script.
            <RUN>
            """)

    def set_check_policy(self):
        self.prompt_check_policy = dedent(f"""
        this is the script I have.

        {self.final_script}

        this is the guideline for the script.

        {self.prompt_detiled_general_policy}

        {self.prompt_detailed_script_policy}

        Correct the script so that it can follow policy properly.
        """)

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