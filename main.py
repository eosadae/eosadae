from prompt_generator import PromptWriterSooni
from openai_api_user import ApiUserSooni

pws = PromptWriterSooni()
pws.create_prompt_for_model_2('힐링', '꽃말_수업', '')
created_prompt = pws.final_script

aus = ApiUserSooni()
aus.create_response(created_prompt)
created_response = aus.final_response

print(created_response)
