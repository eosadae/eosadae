"""abstract.py의 AbstractScriptPromptGeneratorSooni 클래스 참고"""
from modules.regeneration_prompt_generator import RegenerationPromptGeneratorSooni
from modules.api_prompt_sender import ApiPromptSenderSooni

ORIGINAL_PROMPT = '(기존 프롬프트)'
ORIGINAL_SCRIPT = '(기존 대본)'

# api use - get regenerated script
def regenerate_script(user_input):
    ORIGINAL_PROMPT = '(기존 프롬프트)'
    ORIGINAL_SCRIPT = '(기존 대본)'

    rpgs = RegenerationPromptGeneratorSooni(ORIGINAL_PROMPT, ORIGINAL_SCRIPT, user_input)
    rpgs.generate_regeneration_prompt()
    REGENERATION_PROMPT = rpgs.final_regeneration_prompt

    apss = ApiPromptSenderSooni()
    category = user_input['category']
    topic = user_input['topic']
    apss.get_result_remake_script(category, topic)

    REFINAL_SCRIPT = apss.response

    return REFINAL_SCRIPT
