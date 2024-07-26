from openai import OpenAI
import yaml

with open("config.yaml", "r") as config_file:
    config = yaml.safe_load(config_file)
    openai_api_key = config["openai"]["api_key"]


client = OpenAI()

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
