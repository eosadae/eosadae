"""abstract.py의 AbstractScriptPromptGeneratorSooni 클래스 참고"""
from modules.regeneration_prompt_generator import RegenerationPromptGeneratorSooni
from modules.check_policy_prompt_generator import CheckPolicyPromptGeneratorSooni
from modules.script_prompt_generator import ScriptPromptGeneratorSooni

# api use - get regenerated script
def regenerate_script(user_input):
    spgs = ScriptPromptGeneratorSooni(user_input)
    
    CATEGORY = spgs.user_input.category
    TOPIC = spgs.user_input.topic

    BASE_ADDRESS = 'C:\\Users\\USER\\Desktop\\한국외대\\캡스톤\\eosadae-master\\data\\result_script'
    FILE_ADDRESS = BASE_ADDRESS + f'\\{CATEGORY}\\{TOPIC}\\{TOPIC}_result_remake_script.txt'
    with open(FILE_ADDRESS, 'r', encoding='utf-8') as f:
        REFINAL_SCRIPT = f.read()

    print(REFINAL_SCRIPT)

    return REFINAL_SCRIPT
