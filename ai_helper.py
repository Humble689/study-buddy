import openai

#openai.api_key = "Replace with your API key"

def get_ai_response(prompt):
    system_prompt = """You are an expert computer science tutor with deep knowledge across all areas of computer science including:
    - Data Structures and Algorithms
    - Computer Architecture
    - Operating Systems
    - Computer Networks
    - Databases
    - Software Engineering
    - Programming Languages
    - Artificial Intelligence
    - Web Development
    - And other computer science topics

    Provide clear, accurate, and educational responses. When appropriate:
    1. Include relevant examples
    2. Explain concepts step by step
    3. Reference real-world applications
    4. Suggest related topics for further study
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
    )
    return response.choices[0].message['content'].strip()