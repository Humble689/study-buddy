import openai

openai.api_key = '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'  # Replace with the key you just copied

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