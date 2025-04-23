import sqlite3

def init_db():
    conn = sqlite3.connect('study_buddy.db')
    c = conn.cursor()
    
    # Create topics table
    c.execute('''
        CREATE TABLE IF NOT EXISTS topics (
            id INTEGER PRIMARY KEY,
            name TEXT,
            description TEXT
        )
    ''')
    
    # Create questions table with topic reference
    c.execute('''
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY,
            topic_id INTEGER,
            question TEXT,
            answer TEXT,
            difficulty TEXT,
            FOREIGN KEY (topic_id) REFERENCES topics (id)
        )
    ''')
    
    # Create progress table
    c.execute('''
        CREATE TABLE IF NOT EXISTS progress (
            user TEXT,
            question_id INTEGER,
            correct BOOLEAN,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (question_id) REFERENCES questions (id)
        )
    ''')
    
    # Insert default topics if they don't exist
    default_topics = [
        (1, "Data Structures", "Fundamental data structures and their implementations"),
        (2, "Algorithms", "Common algorithms and their complexity analysis"),
        (3, "Computer Architecture", "CPU, memory, and computer organization"),
        (4, "Operating Systems", "Process management, memory management, and file systems"),
        (5, "Networks", "Computer networks and protocols"),
        (6, "Databases", "Database design and SQL"),
        (7, "Software Engineering", "Software development methodologies and practices"),
        (8, "Programming Languages", "Language paradigms and concepts"),
        (9, "Artificial Intelligence", "AI and machine learning fundamentals"),
        (10, "Web Development", "Frontend and backend web technologies")
    ]

    
    c.executemany('INSERT OR IGNORE INTO topics (id, name, description) VALUES (?, ?, ?)', default_topics)
    conn.commit()
    conn.close()

def add_question(topic_id, question, answer, difficulty):
    conn = sqlite3.connect('study_buddy.db')
    c = conn.cursor()
    c.execute('INSERT INTO questions (topic_id, question, answer, difficulty) VALUES (?, ?, ?, ?)', 
              (topic_id, question, answer, difficulty))
    conn.commit()
    conn.close()

def get_random_question(topic_id=None):
    conn = sqlite3.connect('study_buddy.db')
    c = conn.cursor()
    
    if topic_id:
        c.execute('''
            SELECT questions.id, questions.question, questions.answer, topics.name 
            FROM questions 
            JOIN topics ON questions.topic_id = topics.id
            WHERE questions.topic_id = ?
            ORDER BY RANDOM() LIMIT 1
        ''', (topic_id,))
    else:
        c.execute('''
            SELECT questions.id, questions.question, questions.answer, topics.name 
            FROM questions 
            JOIN topics ON questions.topic_id = topics.id
            ORDER BY RANDOM() LIMIT 1
        ''')
    
    question = c.fetchone()
    conn.close()
    return question

def get_all_topics():
    conn = sqlite3.connect('study_buddy.db')
    c = conn.cursor()
    c.execute('SELECT id, name, description FROM topics')
    topics = c.fetchall()
    conn.close()
    return topics
