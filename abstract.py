from abc import ABCMeta, abstractmethod

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

    @abstractmethod
    def get_feedback_input(self):
        """
        값을 입력받아 다음 속성을 재정의함.
        - feedback_score
        - feedback_text
        """

    @abstractmethod
    def get_keyword_input(self):
        """
        값을 입력받아 다음 속성을 재정의함.
        - keyword_for_image
        """

    @abstractmethod
    def set_example_attribute(self):
        """
        웹에서 입력을 받는 부분이 구현되기 전까지 개발을 중단하고 있을 수 없으므로,
        우선 임의 값으로 본 클래스 전체 속성을 재정의하는 메소드
        """

class AbstractDataAddressGetter(metaclass=ABCMeta):
    """각 데이터 경로를 탐색/저장"""
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

    @abstractmethod
    def get_guideline_address(self, category, topic):
        """
        주어진 주제에 맞는 가이드라인의 상대 경로로 다음 속성을 재정의함.
        - guideline_by_line_text_address
        - guideline_by_order_text_address
        - guideline_by_trait_text_address
        """

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

class AbstractPromptDataGetter(metaclass=ABCMeta):
    """데이터 경로를 활용해 데이터 읽기/저장"""
    # 아래 속성에 대해 default값 있어야함
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

    @abstractmethod
    def get_guideline_data(self, type='order'):
        """
        data_address.guideline_by_{type}_text_address 경로에서,
        해당 파일의 텍스트를 읽고 아래 속성을 재정의함.
        - guideline_data
        """

    @abstractmethod
    def get_general_policy_data(self, type='detailed'):
        """
        data_address.{type}_general_policy_address 경로에서,
        해당 파일의 텍스트를 읽고 아래 속성을 재정의함.
        - general_policy_data
        """

    @abstractmethod
    def get_script_policy_data(self, type='detailed'):
        """
        data_address.{type}_script_policy_address 경로에서,
        해당 파일의 텍스트를 읽고 아래 속성을 재정의함.
        - script_policy_data
        """

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

class AbstractReadyMadePromptGetter(metaclass=ABCMeta):
    """기본적으로 항상 동일하게 사용하는 프롬프트 저장"""
    category = '입력받은 카테고리'  # __init__(category, topic)으로 받음
    topic = '입력받은 주제' # __init__(category, topic)으로 받음

    prompt_before_general_policy = '일반-정책 전에 넣을 프롬프트'
    prompt_before_script_policy = '대본-정책 전에 넣을 프롬프트'
    prompt_after_script_policy = '대본-정책 이후에 넣을 프롬프트'
    prompt_before_example_script = '예시 대본 전에 넣을 프롬프트'
    prompt_before_guideline = '가이드라인 전에 넣을 프롬프트'
    prompt_after_guideline = '가이드라인 이후에 넣을 프롬프트'

    check_prompt_before_original_script = '(채점용) 원래 생성된 대본 전에 넣을 프롬프트'
    check_prompt_before_guideline = '(채점용) 가이드라인 전에 넣을 프롬프트'
    check_prompt_before_general_policy = '(채점용) 일반-정책 전에 넣을 프롬프트'
    check_prompt_after_script_policy = '(채점용) 대본-정책 이후에 넣을 프롬프트'

    @abstractmethod
    def generate_prompt_after_script_policy(self):
        """
        기존 코드의 set_prompt_after_policy() 참고
        기존 코드의 prompt_with_example_script + prompt_after_policy

        다음 데이터를 활용하여,
        - category
        - topic

        다음 속성을 재정의함.
        - prompt_after_script_policy
        """

    @abstractmethod
    def generate_check_prompt_after_script_policy(self):
        """
        다음 데이터를 활용하여,
        - category
        - topic

        다음 속성을 재정의함.
        - check_prompt_after_script_policy
        """

class AbstractScriptPromptGenerator(metaclass=ABCMeta):
    """대본 생성용 프롬프트 제작"""
    user_input = 'InputGetter 호출해서 데이터 가져오기'
    # user_input.get_basic_input()
    prompt_data = 'PromptDataGetter 호출해서 데이터 가져오기'
    # PromptDataGetter(user_input.category, user_input.topic)
    # prompt_data.get_every_data(guideline_type, general_policy_type, script_policy_type)
    ready_made_prompt = 'ReadyMadePromptGetter 호출해서 데이터 가져오기'
    # ReadyMadePromptGetter(user_input.category, user_input.topic)
    # ready_made_prompt.generate_prompt_after_script_policy()

    final_prompt = '최종 프롬프트'

    @abstractmethod
    def generate_script_prompt(self):
        """
        다음 데이터를 활용하여,
        - ready_made_prompt.prompt_before_general_policy
        - prompt_data.general_policy_data
        - ready_made_prompt.prompt_before_script_policy
        - prompt_data.script_policy_data
        - ready_made_prompt.prompt_after_script_policy
        - ready_made_prompt.prompt_before_example_script
        - prompt_data.example_script_data
        - ready_made_prompt.prompt_before_guideline
        - prompt_data.guideline_data
        - ready_made_prompt.prompt_after_guideline

        다음 속성을 재정의함.
        - final_prompt
        """

class AbstractCheckPolicyPromptGenerator(metaclass=ABCMeta):
    """정책 채점용 프롬프트 제작"""
    category = '입력받은 카테고리'  # __init__(category, topic)으로 받음
    topic = '입력받은 주제' # __init__(category, topic)으로 받음

    original_script = '원래 생성된 대본'    # __init__(original_script)로 받음
    prompt_data = 'PromptDataGetter 호출해서 데이터 가져오기'
    # PromptDataGetter(category, topic)
    # prompt_data.get_every_data(guideline_type, general_policy_type, script_policy_type)
    ready_made_prompt = 'ReadyMadePromptGetter 호출해서 데이터 가져오기'
    # ReadyMadePromptGetter(category, topic)
    # ready_made_prompt.generate_prompt_after_script_policy()

    check_policy_prompt = '정책 채점 프롬프트'

    @abstractmethod
    def generate_check_policy_prompt(self):
        """
        다음 데이터를 활용하여,
        - ready_made_prompt.check_prompt_before_original_script
        - original_script
        - ready_made_prompt.check_prompt_before_guideline
        - prompt_data.guideline_data
        - ready_made_prompt.check_prompt_before_general_policy
        - prompt_data.general_policy_data
        - prompt_data.script_policy_data
        - ready_made_prompt.check_prompt_after_script_policy

        다음 속성을 재정의함.      
        - check_policy_prompt
        """

class AbstractRegenerationPromptGenerator(metaclass=ABCMeta):
    """대본 재생성용 프롬프트 제작"""
    original_prompt = '원래 작성한 프롬프트'    # __init__(original_prompt, original_script)로 받음
    original_script = '원래 생성된 대본'    # __init__(original_prompt, original_script)로 받음

    user_input = 'InputGetter 호출해서 데이터 가져오기'
    # user_input.get_feedback_input()

    final_regeneration_prompt = '최종 프롬프트'

    @abstractmethod
    def generate_regeneration_prompt(self):
        """
        다음 데이터를 활용하여,
        - original_prompt
        - original_script
        - user_input.feedback_score
        - user_input.feedback_text

        다음 속성을 재정의함.
        - final_regeneration_prompt
        """

class AbstractImagePromptGenerator(metaclass=ABCMeta):
    """이미지 생성용 프롬프트 제작"""
    user_input = 'InputGetter 호출해서 데이터 가져오기'
    # user_input.get_keyword_input()

    final_prompt = '최종적으로 완성된 프롬프트'

    @abstractmethod
    def generate_image_prompt(self):
        """
        다음 데이터를 활용하여,
        - user_input.keyword_for_image

        아래 속성을 재정의
        - final_prompt
        """

class AbstractContinuePromptGenerator(metaclass=ABCMeta):
    """끊긴 답변을 이어나가도록 하는 프롬프트 제작"""

class AbstractPromptDivider(metaclass=ABCMeta):
    """프롬프트를 길이에 맞춰 분할"""

class AbstractApiPromptSender(metaclass=ABCMeta):
    """GPT API에 프롬프트 전송"""

class AbstractApiTextReciever(metaclass=ABCMeta):
    """GPT API에서 받은 답변에서 텍스트를 추출함"""

class AbstractApiImageReciever(metaclass=ABCMeta):
    """GPT API에서 받은 답변에서 이미지를 추출함"""
