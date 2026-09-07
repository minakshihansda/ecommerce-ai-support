from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv("app/.env")

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_response(prompt: str):
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful e-commerce support assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
        max_tokens=300
    )

    return response.choices[0].message.content