import openai
import random
import json
import os

#openai.api_key = "Replace with your API key"

# Fun responses for different situations
GREETINGS = [
    "Hello! Ready to learn something cool? 😊",
    "Hi there! What shall we explore today? 🚀",
    "Hey! I'm excited to help you study! 📚",
    "Greetings, fellow knowledge seeker! 🎓"
]

ENCOURAGEMENTS = [
    "That's a great question! Let's dive in! 💡",
    "Awesome topic! You're going to love learning about this! ⭐",
    "Get ready for some fascinating computer science! 🌟",
    "Love your curiosity! Let's explore this together! 🔍"
]

STUDY_TIPS = [
    "Remember to take short breaks every 25 minutes! 🕒",
    "Try explaining this concept to someone else - it's a great way to learn! 🗣️",
    "Drawing diagrams can help visualize complex concepts! ✏️",
    "Don't forget to practice with real examples! 💻"
]

# Store conversation history
CONVERSATION_FILE = "conversation_history.json"

def load_conversation_history():
    if os.path.exists(CONVERSATION_FILE):
        with open(CONVERSATION_FILE, 'r') as f:
            return json.load(f)
    return []

def save_conversation_history(history):
    with open(CONVERSATION_FILE, 'w') as f:
        json.dump(history, f)

def is_greeting(text):
    greetings = ['hi', 'hello', 'hey', 'howdy', 'hola', 'greetings']
    return any(text.lower().startswith(word) for word in greetings)

def is_how_are_you(text):
    patterns = ['how are you', 'how r u', 'how do you do', 'how are u']
    return any(pattern in text.lower() for pattern in patterns)

def is_thank_you(text):
    patterns = ['thank', 'thanks', 'appreciate']
    return any(pattern in text.lower() for pattern in patterns)

def is_confused(text):
    patterns = ['confused', 'don\'t understand', 'not clear', 'unclear', 'help']
    return any(pattern in text.lower() for pattern in patterns)

def get_ai_response(prompt):
    # Load conversation history
    conversation_history = load_conversation_history()
    
    system_prompt = """You are an expert computer science tutor and programming mentor, similar to Cursor AI. 
    Your goal is to help students learn computer science concepts through interactive, engaging conversations.

    Key characteristics:
    1. Be conversational and friendly, but professional
    2. Provide detailed, step-by-step explanations
    3. Include relevant code examples when appropriate
    4. Use analogies and real-world examples
    5. Break down complex concepts into digestible parts
    6. Ask follow-up questions to ensure understanding
    7. Provide practical applications and use cases
    8. Share best practices and common pitfalls
    9. Use emojis sparingly but effectively
    10. Maintain context throughout the conversation

    When explaining concepts:
    - Start with a high-level overview
    - Break down into smaller components
    - Provide concrete examples
    - Show code snippets when relevant
    - Explain the "why" behind concepts
    - Connect to real-world applications
    - Suggest related topics for deeper learning

    When answering questions:
    - First understand what the student is asking
    - Provide a clear, structured response
    - Include relevant code examples
    - Explain any technical terms
    - Ask if they need clarification
    - Suggest related topics to explore

    When showing code:
    - Use clear, well-commented examples
    - Explain the code step by step
    - Highlight important concepts
    - Show best practices
    - Include error handling when relevant
    - Explain the reasoning behind design choices

    If the student seems confused:
    - Ask clarifying questions
    - Provide simpler explanations
    - Use more examples
    - Break down the concept further
    - Suggest alternative approaches
    - Offer to explain in a different way

    If the student shows interest in a topic:
    - Suggest related concepts
    - Share interesting applications
    - Provide additional resources
    - Ask if they want to explore further
    - Share practical examples
    - Discuss real-world implications

    Always maintain a supportive, encouraging tone while being educational and professional.
    """
    
    # Prepare messages with conversation history
    messages = [{"role": "system", "content": system_prompt}]
    
    # Include relevant conversation history for context
    if conversation_history:
        # Get the last 6 messages (3 exchanges) for context
        messages.extend(conversation_history[-6:])
    
    # Add the current prompt
    messages.append({"role": "user", "content": prompt})
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.7,
    )
    
    ai_response = response.choices[0].message['content'].strip()
    
    # Save conversation history
    conversation_history.append({"role": "user", "content": prompt})
    conversation_history.append({"role": "assistant", "content": ai_response})
    save_conversation_history(conversation_history)
    
    return ai_response