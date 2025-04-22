import openai
import random

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

def is_greeting(text):
    greetings = ['hi', 'hello', 'hey', 'howdy', 'hola', 'greetings']
    return any(text.lower().startswith(word) for word in greetings)

def is_how_are_you(text):
    patterns = ['how are you', 'how r u', 'how do you do', 'how are u']
    return any(pattern in text.lower() for pattern in patterns)

def get_ai_response(prompt):
    # Handle casual interactions
    if not prompt.strip():
        return "Feel free to ask me anything about computer science! I'm here to help! 😊"
    
    if is_greeting(prompt):
        return random.choice(GREETINGS)
    
    if is_how_are_you(prompt):
        return "I'm doing great and excited to help you learn! How can I assist you with computer science today? 🌟"
    
    # Add a fun study tip randomly (20% chance)
    should_add_tip = random.random() < 0.2
    
    system_prompt = """You are a friendly and enthusiastic computer science tutor with a great sense of humor. 
    You have deep knowledge across all areas of computer science including:
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

    Make learning fun by:
    1. Using emojis appropriately
    2. Including interesting real-world examples
    3. Breaking down complex concepts into simple explanations
    4. Adding fun facts when relevant
    5. Being encouraging and supportive
    6. Using analogies that students can relate to
    7. Maintaining a conversational tone while being educational

    If the student seems frustrated or confused, offer extra encouragement and simpler explanations.
    If they show interest in a topic, suggest related interesting areas they might enjoy exploring.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
    )
    
    ai_response = response.choices[0].message['content'].strip()
    
    # Add a random study tip if applicable
    if should_add_tip:
        ai_response += f"\n\n💡 Quick Tip: {random.choice(STUDY_TIPS)}"
    
    return ai_response