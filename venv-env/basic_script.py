from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("No API key found in .env file")
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
