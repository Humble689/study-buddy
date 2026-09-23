import ast
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import init_db, get_all_topics, get_random_question  # noqa: E402


def test_app_py_has_valid_syntax():
    """Catches typos/syntax errors without needing a running Streamlit server."""
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(os.path.join(repo_root, "app.py")) as f:
        source = f.read()
    ast.parse(source)  # raises SyntaxError if app.py is broken


def test_init_db_seeds_default_topics(tmp_path, monkeypatch):
    # Run against a throwaway sqlite file so tests never touch study_buddy.db
    monkeypatch.chdir(tmp_path)
    init_db()

    topics = get_all_topics()
    assert len(topics) == 10
    for topic_id, name, description in topics:
        assert isinstance(topic_id, int)
        assert name
        assert description


def test_get_random_question_handles_empty_topic(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    init_db()

    # No questions have been added yet, so this should return None rather than error
    question = get_random_question(1)
    assert question is None