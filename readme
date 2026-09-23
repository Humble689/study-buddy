import streamlit as st
from ai_helper import get_ai_response
from database import init_db, get_random_question, get_all_topics

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
    'href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">'
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&'
    'family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">',
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
            font-family: "IBM Plex Sans", -apple-system, sans-serif;
        }}
        h1, h2, h3, .section-title, .navbar .brand {{
            font-family: "Space Grotesk", "IBM Plex Sans", sans-serif;
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

        /* Navbar */
        .navbar {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: {NAVY};
            padding: 0.9rem 1.75rem;
            border-radius: 8px;
            margin-bottom: 2rem;
        }}
        .navbar .brand {{
            display: flex;
            align-items: center;
            gap: 0.55rem;
            color: #FFFFFF;
            font-size: 1.1rem;
            font-weight: 600;
        }}
        .navbar .brand i {{
            color: {TEAL};
            font-size: 1.15rem;
        }}
        .navbar .navbar-tag {{
            color: #94A3B8;
            font-size: 0.85rem;
        }}

        .section-title {{
            font-size: 1.25rem;
            font-weight: 600;
            color: {NAVY};
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}
        .section-title i {{
            color: {TEAL_DARK};
            font-size: 1.05rem;
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
# Navbar
# ----------------------------------------------------------------------------
st.markdown(
    f"""
    <div class="navbar">
        <div class="brand">{icon('bi-mortarboard-fill')} Study Buddy</div>
        <div class="navbar-tag">Computer science practice</div>
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

# ----------------------------------------------------------------------------
# Quiz section
# ----------------------------------------------------------------------------
left, right = st.columns([1, 1], gap="large")

with left:
    st.markdown(f'<div class="section-title">{icon("bi-pencil-square")} Quiz yourself</div>', unsafe_allow_html=True)

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
    st.markdown(f'<div class="section-title">{icon("bi-chat-dots")} AI study assistant</div>', unsafe_allow_html=True)

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

st.markdown('<div class="footer-note">Study Buddy — local practice tool</div>', unsafe_allow_html=True)