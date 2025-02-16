import sqlite3

def init_db():
    conn = sqlite3.connect('study_buddy.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY,
            question TEXT,
            answer TEXT,
            complexity TEXT
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS progress (
            user TEXT,
            question_id INTEGER,
            correct BOOLEAN
        )
    ''')
    conn.commit()
    conn.close()

def add_question(question, answer, complexity):
    conn = sqlite3.connect('study_buddy.db')
    c = conn.cursor()
    c.execute('INSERT INTO questions (question, answer, complexity) VALUES (?, ?, ?)', 
              (question, answer, complexity))
    conn.commit()
    conn.close()

def get_random_question():
    conn = sqlite3.connect('study_buddy.db')
    c = conn.cursor()
    c.execute('SELECT id, question, answer FROM questions ORDER BY RANDOM() LIMIT 1')
    question = c.fetchone()
    conn.close()
    return question
