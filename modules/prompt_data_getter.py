"""abstract.py의 AbstractUserInputGetter 클래스 참고"""
from modules.abstract import AbstractPromptDataGetter
from modules.data_address_getter import DataAddressGetterSooni

class PromptDataGetterSooni(AbstractPromptDataGetter):
    """데이터 경로를 활용해 데이터 읽기/저장"""
    def __init__(self, category, topic):
        self.category = category
        self.topic = topic

        self.data_address = DataAddressGetterSooni(self.category, self.topic)
        self.data_address.get_every_data_address()

        self.example_script_data = ''
        self.guideline_data = ''
        self.general_policy_data = ''
        self.script_policy_data = ''

    def get_example_script_data(self):
        file_address = self.data_address.example_script_text_address
        with open(file_address, 'r', encoding='UTF8') as example_script_file:
            self.example_script_data = example_script_file.read()

    def get_guideline_data(self, data_type='order'):
        if data_type == 'order':
            file_address = self.data_address.guideline_by_order_text_address
        elif data_type == 'line':
            file_address = self.data_address.guideline_by_line_text_address
        elif data_type == 'trait':
            file_address = self.data_address.guideline_by_trait_text_address

        with open(file_address, 'r', encoding='UTF8') as guideline_file:
            self.guideline_data = guideline_file.read()

    def get_general_policy_data(self, data_type='detailed'):
        if data_type == 'detailed':
            file_address = self.data_address.detailed_general_policy_address
        elif data_type == 'brief':
            file_address = self.data_address.brief_general_policy_address

        with open(file_address, 'r', encoding='UTF8') as general_policy_file:
            self.general_policy_data = general_policy_file.read()

    def get_script_policy_data(self, data_type='detailed'):
        if data_type == 'detailed':
            file_address = self.data_address.detailed_script_policy_address
        elif data_type == 'brief':
            file_address = self.data_address.brief_script_policy_address

        with open(file_address, 'r', encoding='UTF8') as script_policy_file:
            self.script_policy_data = script_policy_file.read()

    def get_every_data(self, guideline_type, general_policy_type, script_policy_type):
        self.get_example_script_data()
        self.get_guideline_data(guideline_type)
        self.get_general_policy_data(general_policy_type)
        self.get_script_policy_data(script_policy_type)
