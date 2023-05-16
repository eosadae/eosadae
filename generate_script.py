"""abstract.py의 AbstractScriptPromptGeneratorSooni 클래스 참고"""
from modules.script_prompt_generator import ScriptPromptGeneratorSooni
from modules.check_policy_prompt_generator import CheckPolicyPromptGeneratorSooni

spgs = ScriptPromptGeneratorSooni()
spgs.generate_script_prompt()
INITIAL_PROMPT = spgs.final_prompt

CATEGORY = spgs.user_input.category
TOPIC = spgs.user_input.topic

# api use - get script

ORIGINAL_SCRIPT = ''

# policy check
cppgs = CheckPolicyPromptGeneratorSooni(CATEGORY, TOPIC, ORIGINAL_SCRIPT)
cppgs.generate_check_policy_prompt()
CHECK_POLICY_PROMPT = cppgs.check_policy_prompt

print(CHECK_POLICY_PROMPT)
# api use - get modified script

FINAL_SCRIPT = ''
