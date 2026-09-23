import streamlit as st
from ai_helper import get_ai_response
from database import init_db, get_random_question, get_all_topics
import random

# ----------------------------------------------------------------------------
# Setup
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title="Study Buddy",
    layout="wide",
    initial_sidebar_state="expanded",
)

init_db()

if "correct_streak" not in st.session_state:
    st.session_state.correct_streak = 0
if "total_correct" not in st.session_state:
    st.session_state.total_correct = 0
if "total_attempted" not in st.session_state:
    st.session_state.total_attempted = 0
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "current_question" not in st.session_state:
    st.session_state.current_question = None
if "feedback" not in st.session_state:
    st.session_state.feedback = None

NAVY = "#0B1F3A"
NAVY_SOFT = "#13294B"
TEAL = "#14B8A6"
TEAL_DARK = "#0F9488"
SLATE = "#64748B"
BORDER = "#E2E8F0"
BG = "#F8FAFC"

# ----------------------------------------------------------------------------
# Icons (Bootstrap Icons, loaded once)
# ----------------------------------------------------------------------------
st.markdown(
    '<link rel="stylesheet" '
    'href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">',
    unsafe_allow_html=True,
)


def icon(name: str) -> str:
    """Return a Bootstrap Icons <i> tag, e.g. icon('bi-collection')."""
    return f'<i class="bi {name}"></i>'


# ----------------------------------------------------------------------------
# Styling
# ----------------------------------------------------------------------------
st.markdown(
    f"""
    <style>
        .bi {{
            vertical-align: -0.125em;
        }}
        html, body, [class*="css"] {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Inter, Roboto, sans-serif;
        }}

        .main {{
            background-color: {BG};
        }}

        /* Sidebar */
        [data-testid="stSidebar"] {{
            background-color: {NAVY};
        }}
        [data-testid="stSidebar"] * {{
            color: #E2E8F0 !important;
        }}
        [data-testid="stSidebar"] h1,
        [data-testid="stSidebar"] h2,
        [data-testid="stSidebar"] h3 {{
            color: #FFFFFF !important;
            font-weight: 600;
        }}
        [data-testid="stSidebar"] [data-testid="stMetricValue"] {{
            color: {TEAL} !important;
        }}
        [data-testid="stSidebar"] [data-testid="stMetricLabel"] {{
            color: #94A3B8 !important;
        }}
        [data-testid="stSidebar"] .stSelectbox > div > div {{
            background-color: {NAVY_SOFT};
            border: 1px solid #334155;
            color: #E2E8F0;
        }}

        /* Header band */
        .app-header {{
            background: linear-gradient(135deg, {NAVY} 0%, {NAVY_SOFT} 100%);
            padding: 2rem 2.25rem;
            border-radius: 14px;
            margin-bottom: 1.75rem;
        }}
        .app-header h1 {{
            color: #FFFFFF;
            font-size: 1.9rem;
            font-weight: 700;
            margin: 0;
            letter-spacing: -0.01em;
        }}
        .app-header p {{
            color: #94A3B8;
            margin: 0.35rem 0 0 0;
            font-size: 0.98rem;
        }}

        /* Section headers */
        .section-label {{
            font-size: 0.78rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            color: {TEAL_DARK};
            margin-bottom: 0.25rem;
        }}
        .section-title {{
            font-size: 1.3rem;
            font-weight: 700;
            color: {NAVY};
            margin-bottom: 1rem;
        }}

        /* Card */
        .sb-card {{
            background: #FFFFFF;
            border: 1px solid {BORDER};
            border-radius: 12px;
            padding: 1.5rem 1.6rem;
            margin-bottom: 1.25rem;
        }}

        /* Buttons */
        .stButton > button {{
            background-color: {TEAL};
            color: #FFFFFF;
            border: none;
            border-radius: 8px;
            font-weight: 600;
            padding: 0.5rem 1.1rem;
            transition: background-color 0.15s ease;
        }}
        .stButton > button:hover {{
            background-color: {TEAL_DARK};
            color: #FFFFFF;
        }}
        .stButton > button:focus:not(:active) {{
            color: #FFFFFF;
        }}

        /* Secondary / next-question button */
        button[kind="secondary"] {{
            background-color: #FFFFFF !important;
            color: {NAVY} !important;
            border: 1px solid {BORDER} !important;
        }}
        button[kind="secondary"]:hover {{
            border-color: {TEAL} !important;
            color: {TEAL_DARK} !important;
        }}

        /* Chat bubbles */
        [data-testid="stChatMessage"] {{
            border: 1px solid {BORDER};
            border-radius: 10px;
            padding: 0.4rem 0.2rem;
        }}

        /* Streak / result banners */
        .result-correct {{
            background: #ECFDF5;
            border: 1px solid #A7F3D0;
            color: #065F46;
            padding: 0.9rem 1.1rem;
            border-radius: 8px;
            font-weight: 500;
        }}
        .result-incorrect {{
            background: #FEF2F2;
            border: 1px solid #FECACA;
            color: #991B1B;
            padding: 0.9rem 1.1rem;
            border-radius: 8px;
            font-weight: 500;
        }}

        .footer-note {{
            color: {SLATE};
            font-size: 0.85rem;
            text-align: center;
            margin-top: 2rem;
        }}

        #MainMenu, footer {{visibility: hidden;}}
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# Header
# ----------------------------------------------------------------------------
st.markdown(
    f"""
    <div class="app-header">
        <h1>{icon('bi-mortarboard')} Study Buddy</h1>
        <p>A focused practice space for computer science fundamentals.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# Sidebar
# ----------------------------------------------------------------------------
st.sidebar.markdown(f"### {icon('bi-collection')} Topics", unsafe_allow_html=True)
topics = get_all_topics()
selected_topic = st.sidebar.selectbox(
    "Choose a topic to study",
    options=[(t[0], t[1]) for t in topics],
    format_func=lambda x: x[1],
    label_visibility="collapsed",
)

st.sidebar.markdown("---")
st.sidebar.markdown(f"### {icon('bi-graph-up-arrow')} Your Progress", unsafe_allow_html=True)
col_a, col_b = st.sidebar.columns(2)
col_a.metric("Streak", st.session_state.correct_streak)
accuracy = (
    (st.session_state.total_correct / st.session_state.total_attempted) * 100
    if st.session_state.total_attempted > 0
    else 0
)
col_b.metric("Accuracy", f"{accuracy:.0f}%")

st.sidebar.markdown("---")
st.sidebar.markdown(f"### {icon('bi-info-circle')} About This Topic", unsafe_allow_html=True)
for topic in topics:
    with st.sidebar.expander(topic[1]):
        st.write(topic[2])

st.sidebar.markdown("---")
quotes = [
    "The only way to learn a new programming language is by writing programs in it. — Dennis Ritchie",
    "Code is like humor. When you have to explain it, it's bad. — Cory House",
    "First, solve the problem. Then, write the code. — John Johnson",
    "Experience is the name everyone gives to their mistakes. — Oscar Wilde",
]
st.sidebar.caption(random.choice(quotes))

# ----------------------------------------------------------------------------
# Quiz section
# ----------------------------------------------------------------------------
left, right = st.columns([1, 1], gap="large")

with left:
    st.markdown(f'<div class="section-label">{icon("bi-pencil-square")} Practice</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Quiz yourself</div>', unsafe_allow_html=True)

    st.markdown('<div class="sb-card">', unsafe_allow_html=True)

    if selected_topic:
        if st.session_state.current_question is None:
            st.session_state.current_question = get_random_question(selected_topic[0])

        question = st.session_state.current_question

        if question:
            q_id, q_text, q_answer, topic_name = question
            st.caption(topic_name)
            st.markdown(f"**{q_text}**")
            user_answer = st.text_input("Your answer", label_visibility="collapsed", key=f"answer_{q_id}")

            btn_col1, btn_col2 = st.columns([1, 1])
            with btn_col1:
                submit = st.button("Submit", key="submit")
            with btn_col2:
                next_q = st.button("Next question", key="next", type="secondary")

            if submit:
                st.session_state.total_attempted += 1
                if user_answer.lower().strip() == q_answer.lower().strip():
                    st.session_state.correct_streak += 1
                    st.session_state.total_correct += 1
                    st.session_state.feedback = ("correct", f"Correct — streak is now {st.session_state.correct_streak}.")
                else:
                    st.session_state.correct_streak = 0
                    st.session_state.feedback = ("incorrect", f"Not quite. The correct answer was: {q_answer}")

            if st.session_state.feedback:
                kind, msg = st.session_state.feedback
                css_class = "result-correct" if kind == "correct" else "result-incorrect"
                banner_icon = icon("bi-check-circle-fill") if kind == "correct" else icon("bi-x-circle-fill")
                st.markdown(f'<div class="{css_class}">{banner_icon} {msg}</div>', unsafe_allow_html=True)

            if next_q:
                st.session_state.current_question = get_random_question(selected_topic[0])
                st.session_state.feedback = None
                st.rerun()
        else:
            st.info("No questions available for this topic yet.")
    else:
        st.info("Select a topic from the sidebar to begin.")

    st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# AI helper section
# ----------------------------------------------------------------------------
with right:
    st.markdown(f'<div class="section-label">{icon("bi-chat-dots")} Ask</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">AI study assistant</div>', unsafe_allow_html=True)

    st.markdown('<div class="sb-card">', unsafe_allow_html=True)
    st.caption(
        "Ask about a concept, request a walkthrough, or get help understanding "
        "a problem step by step."
    )

    chat_box = st.container(height=320)
    with chat_box:
        for message in st.session_state.chat_history:
            with st.chat_message(message["role"]):
                st.write(message["content"])

    prompt = st.chat_input("Type your message here...")
    if prompt:
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        with chat_box:
            with st.chat_message("user"):
                st.write(prompt)
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    response = get_ai_response(prompt)
                    st.write(response)
        st.session_state.chat_history.append({"role": "assistant", "content": response})

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown('<div class="footer-note">Study Buddy · built for focused CS practice</div>', unsafe_allow_html=True)
