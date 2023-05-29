"""abstract.py의 AbstractScriptPromptGeneratorSooni 클래스 참고"""
from modules.script_prompt_generator import ScriptPromptGeneratorSooni
from modules.check_policy_prompt_generator import CheckPolicyPromptGeneratorSooni

def generate_script(user_input):
    spgs = ScriptPromptGeneratorSooni(user_input)
    spgs.generate_script_prompt()
    INITIAL_PROMPT = spgs.final_prompt

    CATEGORY = spgs.user_input.category
    TOPIC = spgs.user_input.topic

    # api use - get script
    BASE_ADDRESS = 'C:\\Users\\USER\\Desktop\\한국외대\\캡스톤\\eosadae-master\\data\\result_script'
    FILE_ADDRESS = BASE_ADDRESS + f'\\{CATEGORY}\\{TOPIC}\\{TOPIC}_result_script.txt'
    with open(FILE_ADDRESS, 'r', encoding='utf-8') as f:
        FINAL_SCRIPT = f.read()

    print(INITIAL_PROMPT)
    print(FINAL_SCRIPT)

    return INITIAL_PROMPT, FINAL_SCRIPT
