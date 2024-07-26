from openai import OpenAI
import json

with open("config.json", "r") as config_file:
    config = json.load(config_file)
    openai_api_key = config["openai"]["api_key"]

client = OpenAI(api_key=openai_api_key)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "You specialize in concisely explaining complex topics to 12yo.",
        },
        {
            "role": "user",
            "content": "What's artificial neural network?",
        },
    ],
)

print(completion.choices[0].message.content)
