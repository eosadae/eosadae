"""abstract.py의 AbstractImagePromptGenerator 클래스 참고"""
from modules.image_prompt_generator import ImagePromptGeneratorSooni
from modules.api_prompt_sender import ApiPromptSenderSooni
from modules.api_image_receiver import ApiImageReceiverSooni

ipgs = ImagePromptGeneratorSooni()
ipgs.generate_image_prompt()

IMAGE_GENERATION_PROMPT = ipgs.final_prompt

# api use - get image
apss = ApiPromptSenderSooni()
apss.get_api_key()

apss.generate_response(IMAGE_GENERATION_PROMPT)
GENERATED_IMAGE_RESPONSE = apss.response

# # api use - image only
airs = ApiImageReceiverSooni(GENERATED_IMAGE_RESPONSE)
GENERATED_IMAGE_URL = airs.image_url

print(GENERATED_IMAGE_URL)
