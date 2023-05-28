"""abstract.py의 AbstractDataAddressGetter 클래스 참고"""
from modules.abstract import AbstractDataAddressGetter

class DataAddressGetterSooni(AbstractDataAddressGetter):
    """각 데이터 경로를 탐색/저장"""
    def __init__(self, category, topic):
        self.category = category
        self.topic = topic

        self.example_script_folder_address = 'data/example_script/'
        self.guideline_folder_address = 'data/guideline/'
        self.policy_folder_address = 'data/policy/'

        self.example_script_text_address = ''

        self.guideline_by_line_text_address = ''
        self.guideline_by_order_text_address = ''
        self.guideline_by_trait_text_address = ''

        self.brief_general_policy_address = 'data/policy/brief_general_policy.txt'
        self.detailed_general_policy_address = 'data/policy/detailed_general_policy.txt'
        self.brief_script_policy_address = 'data/policy/brief_script_policy.txt'
        self.detailed_script_policy_address = 'data/policy/detailed_script_policy.txt'

    def get_example_script_address(self):
        sub_address_example_script = f'{self.category}/{self.topic}_example_script.txt'
        self.example_script_text_address = self.example_script_folder_address + \
            sub_address_example_script

    def get_guideline_address(self):
        sub_address_guideline_by_line = f'{self.category}/{self.topic}_guideline_by_line.txt'
        sub_address_guideline_by_order = f'{self.category}/{self.topic}_guideline_by_order.txt'
        sub_address_guideline_by_trait = f'{self.category}/{self.topic}_guideline_by_trait.txt'

        self.guideline_by_line_text_address = self.guideline_folder_address + \
            sub_address_guideline_by_line
        self.guideline_by_order_text_address = self.guideline_folder_address + \
            sub_address_guideline_by_order
        self.guideline_by_trait_text_address = self.guideline_folder_address + \
            sub_address_guideline_by_trait

    def get_every_data_address(self):
        self.get_example_script_address()
        self.get_guideline_address()
