"""abstract.py의 AbstractScriptPromptGeneratorSooni 클래스 참고"""
from modules.regeneration_prompt_generator import RegenerationPromptGeneratorSooni

ORIGINAL_PROMPT = '(기존 프롬프트)'
ORIGINAL_SCRIPT = '(기존 대본)'

rpgs = RegenerationPromptGeneratorSooni(ORIGINAL_PROMPT, ORIGINAL_SCRIPT)
rpgs.generate_regeneration_prompt()
REGENERATION_PROMPT = rpgs.final_regeneration_prompt

# api use - get regenerated script
