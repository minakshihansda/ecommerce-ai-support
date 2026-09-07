from groq import Groq

from app.core.config import GROQ_API_KEY


client = Groq(api_key=GROQ_API_KEY)


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