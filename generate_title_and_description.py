from modules.api_prompt_sender import ApiPromptSenderSooni

def get_title_and_description(script):
    apss = ApiPromptSenderSooni()
    apss.get_api_key()

    title_prompt = 'This is the script I have.\n' + script + 'Please write down the title of the script you just created in Korean.\nUse the subject "순이" and write a script title that will attract attention.'

    description_prompt = 'This is the script I have.\n' + script + 'Please write down the description of the script you just created in Korean.\nUse the subject "순이" and the explanation should be simple.\nWrite only one line centering on the subject so that people can understand the contents of the script at a glance.'

    apss.generate_title_response(title_prompt)
    title = apss.title_response

    apss.generate_description_response(description_prompt)
    description = apss.description_response

    return title, description
