"""abstract.py의 AbstractScriptPromptGeneratorSooni 클래스 참고"""
from modules.script_prompt_generator import ScriptPromptGeneratorSooni
from modules.check_policy_prompt_generator import CheckPolicyPromptGeneratorSooni
from modules.api_prompt_sender import ApiPromptSenderSooni

def generate_script(user_input):
    spgs = ScriptPromptGeneratorSooni(user_input)
    spgs.generate_script_prompt()
    INITIAL_PROMPT = spgs.final_prompt

    CATEGORY = spgs.user_input.category
    TOPIC = spgs.user_input.topic

    # api use - get script
    apss = ApiPromptSenderSooni()
    apss.get_api_key()
    apss.get_result_script(CATEGORY, TOPIC)
    ORIGINAL_SCRIPT = apss.response

    # policy check
    cppgs = CheckPolicyPromptGeneratorSooni(CATEGORY, TOPIC, ORIGINAL_SCRIPT)
    cppgs.generate_check_policy_prompt()
    CHECK_POLICY_PROMPT = cppgs.check_policy_prompt

    FINAL_SCRIPT = '우리가 만든 최종 대본입니다.'

    return CHECK_POLICY_PROMPT, ORIGINAL_SCRIPT
