import streamlit as st
from ai_helper import get_ai_response
from database import init_db, get_random_question, get_all_topics

# Initialize the database
init_db()

st.title("🤖 AI Study Buddy for Computer Science")

# Sidebar for topic selection
st.sidebar.header("📚 Topics")
topics = get_all_topics()
selected_topic = st.sidebar.selectbox(
    "Choose a topic to study:",
    options=[(t[0], t[1]) for t in topics],
    format_func=lambda x: x[1]
)

# Study Mode
st.header("📚 Quiz Yourself!")
if selected_topic:
    question = get_random_question(selected_topic[0])
    if question:
        q_id, q_text, q_answer, topic_name = question
        st.subheader(f"Topic: {topic_name}")
        user_answer = st.text_input(f"Q: {q_text}")

        if st.button("Submit Answer"):
            if user_answer.lower().strip() == q_answer.lower().strip():
                st.success("✅ Correct!")
            else:
                st.error(f"❌ Incorrect! The correct answer was: {q_answer}")
    else:
        st.info("No questions available for this topic yet. Check back later!")

# AI Helper
st.header("💡 Ask the AI!")
ai_question = st.text_area("Ask me anything about computer science:")
if st.button("Get Answer"):
    ai_response = get_ai_response(ai_question)
    st.write(ai_response)

# Topic Information
st.sidebar.header("ℹ️ About Topics")
for topic in topics:
    with st.sidebar.expander(topic[1]):
        st.write(topic[2])
