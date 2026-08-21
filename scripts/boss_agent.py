import os
from openai import OpenAI

# The Boss agent connects directly to the OmniRoute Proxy (Secretary)
client = OpenAI(
    base_url="http://127.0.0.1:20128/v1",
    api_key=os.environ.get("OPENROUTER_API_KEY", "dummy-key")
)

response = client.chat.completions.create(
    model="openrouter/nousresearch/hermes-3-llama-3.1-405b:free",
    messages=[
        {
            "role": "user",
            "content": "Inspect inbox/*.txt items. Analyze taxonomy rules in CLAUDE.md. Formulate sorting directives into task_instruction.txt."
        }
    ]
)

instruction = response.choices[0].message.content

with open("task_instruction.txt", "w") as f:
    f.write(instruction)

print("Boss Agent: Formulated directives into task_instruction.txt")
