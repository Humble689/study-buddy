import openai
import os

# Store API key in environment variable for security
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_ai_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        if response.choices:
            return response.choices[0].message['content'].strip()
        else:
            return "No response from AI model."
    except Exception as e:
        return f"Error: {str(e)}"