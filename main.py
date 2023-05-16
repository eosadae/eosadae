from modules.script_prompt_generator import ScriptPromptGeneratorSooni

spgs = ScriptPromptGeneratorSooni()
spgs.generate_script_prompt()
print(spgs.final_prompt)
