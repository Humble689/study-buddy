import streamlit as st
from ai_helper import get_ai_response
from database import init_db, get_random_question

# Initialize the database
init_db()

st.title("🤖 AI Study Buddy for Computational Complexity")

# Study Mode
st.header("📚 Quiz Yourself!")
question = get_random_question()
if question:
    q_id, q_text, q_answer = question
    user_answer = st.text_input(f"Q: {q_text}")

    if st.button("Submit Answer"):
        if user_answer.lower().strip() == q_answer.lower().strip():
            st.success("✅ Correct!")
        else:
            st.error(f"❌ Incorrect! The correct answer was: {q_answer}")
        # You can log progress to the database here.

# AI Helper
st.header("💡 Ask the AI!")
ai_question = st.text_area("Ask me anything about computational complexity:")
if st.button("Get Answer"):
    ai_response = get_ai_response(ai_question)
    st.write(ai_response)
