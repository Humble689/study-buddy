import openai

# Ensure your OpenAI API key is set as an environment variable for security
import os
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_ai_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
    )
    return response.choices[0].message['content'].strip()
