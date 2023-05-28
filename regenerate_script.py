"""abstract.py의 AbstractScriptPromptGeneratorSooni 클래스 참고"""
from modules.regeneration_prompt_generator import RegenerationPromptGeneratorSooni

ORIGINAL_PROMPT = '(기존 프롬프트)'
ORIGINAL_SCRIPT = '(기존 대본)'

<<<<<<< HEAD
# api use - get regenerated script
def regenerate_script(user_input):
    ORIGINAL_PROMPT = '(기존 프롬프트)'
    ORIGINAL_SCRIPT = '(기존 대본)'

    rpgs = RegenerationPromptGeneratorSooni(ORIGINAL_PROMPT, ORIGINAL_SCRIPT, user_input)
    rpgs.generate_regeneration_prompt()
    REGENERATION_PROMPT = rpgs.final_regeneration_prompt

    REFINAL_SCRIPT = '우리가 만든 최종 재생성 대본입니다.'

    return REFINAL_SCRIPT
=======
rpgs = RegenerationPromptGeneratorSooni(ORIGINAL_PROMPT, ORIGINAL_SCRIPT)
rpgs.generate_regeneration_prompt()
REGENERATION_PROMPT = rpgs.final_regeneration_prompt

# api use - get regenerated script
>>>>>>> 4f6cd6af505c79bf1c92710beea504b55cd0f369
