import streamlit as st
from ai_helper import get_ai_response
from database import init_db, get_random_question, get_all_topics
import random

# Initialize the database
init_db()

# Initialize session state for streak counting and chat history
if 'correct_streak' not in st.session_state:
    st.session_state.correct_streak = 0
if 'total_correct' not in st.session_state:
    st.session_state.total_correct = 0
if 'total_attempted' not in st.session_state:
    st.session_state.total_attempted = 0
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

st.title("🤖 AI Study Buddy for Computer Science")
st.markdown("Your friendly companion for learning computer science! 🎓")

# Sidebar for topic selection and stats
st.sidebar.header("📚 Topics")
topics = get_all_topics()
selected_topic = st.sidebar.selectbox(
    "Choose a topic to study:",
    options=[(t[0], t[1]) for t in topics],
    format_func=lambda x: x[1]
)

# Display stats in sidebar
st.sidebar.header("📊 Your Progress")
st.sidebar.metric("Current Streak", f"🔥 {st.session_state.correct_streak}")
if st.session_state.total_attempted > 0:
    accuracy = (st.session_state.total_correct / st.session_state.total_attempted) * 100
    st.sidebar.metric("Accuracy", f"🎯 {accuracy:.1f}%")

# Study Mode
st.header("📚 Quiz Yourself!")
if selected_topic:
    question = get_random_question(selected_topic[0])
    if question:
        q_id, q_text, q_answer, topic_name = question
        st.subheader(f"Topic: {topic_name}")
        user_answer = st.text_input(f"Q: {q_text}")

        col1, col2 = st.columns([1, 2])
        with col1:
            if st.button("Submit Answer", key="submit"):
                st.session_state.total_attempted += 1
                if user_answer.lower().strip() == q_answer.lower().strip():
                    st.session_state.correct_streak += 1
                    st.session_state.total_correct += 1
                    st.success(f"✅ Correct! Streak: {st.session_state.correct_streak} 🔥")
                    if st.session_state.correct_streak % 5 == 0:
                        st.balloons()
                        st.success(f"🎉 Amazing! You've got a streak of {st.session_state.correct_streak}!")
                else:
                    st.session_state.correct_streak = 0
                    st.error(f"❌ Not quite! The correct answer was: {q_answer}")
                    st.write("Don't worry! Keep trying! 💪")
        with col2:
            if st.button("Next Question ➡️"):
                st.rerun()
    else:
        st.info("No questions available for this topic yet. Check back later! 📝")

# AI Helper
st.header("💡 Chat with AI Study Buddy!")
st.markdown("""
Ask me anything about computer science! I can:
- Explain concepts in detail with code examples
- Help you understand difficult topics
- Guide you through problems step by step
- Share best practices and common pitfalls
- Provide real-world applications and examples
""")

# Chat interface
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
if prompt := st.chat_input("Type your message here..."):
    # Add user message to chat history
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.write(prompt)
    
    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking... 🤔"):
            response = get_ai_response(prompt)
            st.write(response)
            st.session_state.chat_history.append({"role": "assistant", "content": response})

# Topic Information
st.sidebar.header("ℹ️ About Topics")
for topic in topics:
    with st.sidebar.expander(topic[1]):
        st.write(topic[2])

# Motivational quote (changes daily)
st.sidebar.markdown("---")
quotes = [
    "The only way to learn a new programming language is by writing programs in it. - Dennis Ritchie",
    "Sometimes it pays to stay in bed on Monday, rather than spending the rest of the week debugging Monday's code. - Dan Salomon",
    "Code is like humor. When you have to explain it, it's bad. - Cory House",
    "First, solve the problem. Then, write the code. - John Johnson",
    "Experience is the name everyone gives to their mistakes. - Oscar Wilde"
]
st.sidebar.markdown("### 💭 Quote of the Day")
st.sidebar.markdown(f"*{random.choice(quotes)}*")
