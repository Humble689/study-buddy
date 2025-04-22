import random
import json
import os

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

# Predefined responses for common topics
TOPIC_RESPONSES = {
    "data structures": [
        "Data structures are ways of organizing and storing data for efficient access and modification. Common examples include arrays, linked lists, stacks, queues, trees, and graphs.",
        "Arrays provide O(1) access time but fixed size, while linked lists offer dynamic size but O(n) access time.",
        "Hash tables provide O(1) average case lookup time by using a hash function to map keys to values."
    ],
    "algorithms": [
        "Algorithms are step-by-step procedures for solving problems. Common examples include sorting algorithms (quicksort, mergesort) and search algorithms (binary search).",
        "Time complexity measures how the runtime of an algorithm grows with input size. Common notations are O(1), O(log n), O(n), O(n log n), and O(n²).",
        "Space complexity measures how much memory an algorithm uses relative to input size."
    ],
    "computer architecture": [
        "Computer architecture refers to the design of computer systems, including CPU, memory, and I/O devices.",
        "The CPU consists of the control unit, ALU, and registers. It executes instructions fetched from memory.",
        "Pipelining is a technique where multiple instructions are overlapped in execution to improve performance."
    ],
    "operating systems": [
        "Operating systems manage hardware resources and provide services for computer programs.",
        "Process management involves creating, scheduling, and terminating processes.",
        "Memory management handles allocation and deallocation of memory for processes."
    ],
    "networks": [
        "Computer networks connect devices to share resources and information.",
        "The OSI model has 7 layers: Physical, Data Link, Network, Transport, Session, Presentation, and Application.",
        "TCP provides reliable, ordered communication, while UDP offers faster but unreliable communication."
    ],
    "databases": [
        "Databases store and manage structured data. Common types include relational (SQL) and non-relational (NoSQL).",
        "SQL databases use tables with rows and columns, while NoSQL databases use various data models like documents, key-value pairs, or graphs.",
        "Normalization is the process of organizing data to minimize redundancy and dependency."
    ],
    "software engineering": [
        "Software engineering is the application of engineering principles to software development.",
        "Common methodologies include waterfall, agile, and DevOps.",
        "Version control systems like Git help track changes to code over time."
    ],
    "programming languages": [
        "Programming languages are used to create computer programs. They can be compiled or interpreted.",
        "High-level languages like Python and Java are easier to read and write than low-level languages like assembly.",
        "Object-oriented programming uses objects to design applications and computer programs."
    ],
    "artificial intelligence": [
        "Artificial intelligence is the simulation of human intelligence by machines.",
        "Machine learning is a subset of AI that enables systems to learn from data.",
        "Deep learning uses neural networks with many layers to analyze various factors of data."
    ],
    "web development": [
        "Web development involves creating websites and web applications.",
        "Frontend development focuses on user interface and experience, while backend development handles server-side logic.",
        "Common technologies include HTML, CSS, JavaScript, and various frameworks like React, Angular, and Vue."
    ]
}

# Greeting responses
GREETINGS = [
    "Hello! Ready to learn something cool? 😊",
    "Hi there! What shall we explore today? 🚀",
    "Hey! I'm excited to help you study! 📚",
    "Greetings, fellow knowledge seeker! 🎓"
]

# Follow-up questions
FOLLOW_UP_QUESTIONS = [
    "Would you like me to explain this concept in more detail?",
    "Is there a specific aspect of this topic you'd like to explore further?",
    "Would you like to see some code examples related to this concept?",
    "Do you have any questions about what I just explained?",
    "Would you like to learn about related topics?"
]

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

def get_topic_from_text(text):
    text = text.lower()
    for topic in TOPIC_RESPONSES:
        if topic in text:
            return topic
    return None

def get_ai_response(prompt):
    # Load conversation history
    conversation_history = load_conversation_history()
    
    # Handle casual interactions
    if not prompt.strip():
        response = "Feel free to ask me anything about computer science! I'm here to help! 😊"
        conversation_history.append({"role": "user", "content": prompt})
        conversation_history.append({"role": "assistant", "content": response})
        save_conversation_history(conversation_history)
        return response
    
    if is_greeting(prompt):
        response = random.choice(GREETINGS)
        conversation_history.append({"role": "user", "content": prompt})
        conversation_history.append({"role": "assistant", "content": response})
        save_conversation_history(conversation_history)
        return response
    
    if is_how_are_you(prompt):
        response = "I'm doing great and excited to help you learn! How can I assist you with computer science today? 🌟"
        conversation_history.append({"role": "user", "content": prompt})
        conversation_history.append({"role": "assistant", "content": response})
        save_conversation_history(conversation_history)
        return response
    
    if is_thank_you(prompt):
        response = "You're welcome! Feel free to ask more questions - I'm here to help you learn! 🌟"
        conversation_history.append({"role": "user", "content": prompt})
        conversation_history.append({"role": "assistant", "content": response})
        save_conversation_history(conversation_history)
        return response
    
    # Check if the prompt is about a specific topic
    topic = get_topic_from_text(prompt)
    if topic:
        response = random.choice(TOPIC_RESPONSES[topic])
        # Add a follow-up question
        response += f"\n\n{random.choice(FOLLOW_UP_QUESTIONS)}"
    else:
        # Generic response for other questions
        response = "I'd be happy to help you with that! Could you please provide more details about what you'd like to learn? For example, you could ask about data structures, algorithms, computer architecture, operating systems, networks, databases, software engineering, programming languages, artificial intelligence, or web development."
    
    # Save conversation history
    conversation_history.append({"role": "user", "content": prompt})
    conversation_history.append({"role": "assistant", "content": response})
    save_conversation_history(conversation_history)
    
    return response