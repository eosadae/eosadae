from abc import *

class AbstractUserInputGetter(metaclass=ABCMeta):
    """웹에서 어떻게 입력받는지에 따라 다르게 구현됨"""
    category = '입력받은 카테고리'
    topic = '입력받은 주제'
    additional_request = '입력받은 추가지시'

    feedback_score = '입력받은 별점'
    feedback_text = '입력받은 사유'

    keyword_for_image = '입력받은 이미지 생성용 키워드'

    @abstractmethod
    def get_basic_input(self):
        """
        값을 입력받아 다음 속성을 재정의함.
        - category
        - topic
        - additional_request
        """
        pass

    @abstractmethod
    def get_feedback_input(self):
        """
        값을 입력받아 다음 속성을 재정의함.
        - feedback_score
        - feedback_text
        """
        pass

    @abstractmethod
    def get_keyword_input(self):
        """
        값을 입력받아 다음 속성을 재정의함.
        - keyword_for_image
        """
        pass

    @abstractmethod
    def set_example_attribute(self):
        """
        웹에서 입력을 받는 부분이 구현되기 전까지 개발을 중단하고 있을 수 없으므로,
        우선 임의 값으로 본 클래스 전체 속성을 재정의하는 메소드
        """
        pass

class AbstractDataAddressGetter(metaclass=ABCMeta):
    category = '입력받은 카테고리'  # __init__(category, topic)으로 받음
    topic = '입력받은 주제' # __init__(category, topic)으로 받음

    example_script_folder_address = 'example_script 폴더까지 상대 경로'
    guideline_folder_address = 'guideline 폴더까지 상대 경로'
    policy_folder_address = 'policy 폴더까지 상대 경로'

    example_script_text_address = '특정 주제의 예시대본 데이터까지 상대 경로'

    guideline_by_line_text_address = '특정 주제의 줄별-가이드라인 데이터까지 상대 경로'
    guideline_by_order_text_address = '특정 주제의 순서별-가이드라인 데이터까지 상대 경로'
    guideline_by_trait_text_address = '특정 주제의 특징별-가이드라인 데이터까지 상대 경로'
    
    brief_general_policy_address = '간단한-일반-정책 데이터까지 상대 경로'
    detailed_general_policy_address = '상세한-일반-정책 데이터까지 상대 경로'

    brief_script_policy_address = '간단한-대본-정책 데이터까지 상대 경로'
    detailed_script_policy_address = '상세한-대본-정책 데이터까지 상대 경로'

    @abstractmethod
    def get_example_script_address(self, category, topic):
        """
        주어진 주제에 맞는 예시 대본의 상대 경로로 다음 속성을 재정의함.
        - example_script_text_address
        """
        pass

    @abstractmethod
    def get_guideline_address(self, category, topic):
        """
        주어진 주제에 맞는 가이드라인의 상대 경로로 다음 속성을 재정의함.
        - guideline_by_line_text_address
        - guideline_by_order_text_address
        - guideline_by_trait_text_address
        """
        pass

    @abstractmethod
    def get_every_data_address(self, category, topic):
        """
        다음 메소드를 모두 실행하여,
        - get_example_script_address(topic)
        - get_guideline_address(topic)

        아래 속성을 모두 재정의함.
        - example_script_text_address
        - guideline_by_line_text_address
        - guideline_by_order_text_address
        - guideline_by_trait_text_address
        """
        pass

class AbstractPromptDataGetter(metaclass=ABCMeta):
    category = '입력받은 카테고리'  # __init__(category, topic)으로 받음
    topic = '입력받은 주제' # __init__(category, topic)으로 받음

    data_address = 'DataAddressKeeper 호출해서 경로 가져오기'
    # data_address.get_every_data_address(category, topic)
    example_script_data = '예시대본 텍스트 데이터'
    guideline_data = '가이드라인 텍스트 데이터'
    general_policy_data = '일반-정책 텍스트 데이터'
    script_policy_data = '대본-정책 텍스트 데이터'

    @abstractmethod
    def get_example_script_data(self):
        """
        data_address.example_script_text_address 경로에서,
        해당 파일의 텍스트를 읽고 아래 속성을 재정의함.
        - example_script_data
        """
        pass

    @abstractmethod
    def get_guideline_data(self, type='order'):
        """
        data_address.guideline_by_{type}_text_address 경로에서,
        해당 파일의 텍스트를 읽고 아래 속성을 재정의함.
        - guideline_data
        """
        pass

    @abstractmethod
    def get_general_policy_data(self, type='detailed'):
        """
        data_address.{type}_general_policy_address 경로에서,
        해당 파일의 텍스트를 읽고 아래 속성을 재정의함.
        - general_policy_data
        """
        pass

    @abstractmethod
    def get_script_policy_data(self, type='detailed'):
        """
        data_address.{type}_script_policy_address 경로에서,
        해당 파일의 텍스트를 읽고 아래 속성을 재정의함.
        - script_policy_data
        """
        pass

    @abstractmethod
    def get_every_data(self, guideline_type, general_policy_type, script_policy_type):
        """
        다음 메소드를 모두 실행하여,
        - get_example_script_data()
        - get_guideline_data(guideline_type)
        - get_general_policy_data(general_policy_type)
        - get_script_policy_data(script_policy_type)

        아래 속성을 모두 재정의함.
        - example_script_data
        - guideline_data
        - general_policy_data
        - script_policy_data
        """
        pass

class AbstractScriptPromptGenerator(metaclass=ABCMeta):
    user_input = 'InputGetter 호출해서 데이터 가져오기'
    # user_input.get_basic_input()
    prompt_data = 'DataGetter 호출해서 데이터 가져오기'
    # prompt_data.get_every_data(user_input.category, user_input.topic)

    final_prompt = '최종 프롬프트'
    
    pass

class AbstractScriptPromptReGenerator(metaclass=ABCMeta):
    original_prompt = '원래 작성한 프롬프트'    # __init__(original_prompt, original_script)로 받음
    original_script = '원래 생성된 프롬프트'    # __init__(original_prompt, original_script)로 받음

    user_input = 'InputGetter 호출해서 데이터 가져오기'
    # user_input.get_feedback_input()

    final_regeneration_prompt = '최종 프롬프트'

    pass

class AbstractImagePromptGenerator(metaclass=ABCMeta):
    user_input = 'InputGetter 호출해서 데이터 가져오기'
    # user_input.get_keyword_input()

    final_prompt = '최종적으로 완성된 프롬프트'

    @abstractmethod
    def generate_image_prompt(self):
        """
        user_input.keyword_for_image 값을 활용하여 아래 속성을 재정의
        - final_prompt
        """
        pass

