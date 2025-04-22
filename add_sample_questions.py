from database import init_db, add_question

def add_sample_questions():
    # Data Structures
    add_question(1, "What is the time complexity of searching in a binary search tree?", "O(log n)", "Medium")
    add_question(1, "What is the main advantage of a hash table over a binary search tree?", "O(1) average case lookup time", "Easy")
    
    # Algorithms
    add_question(2, "What is the time complexity of quicksort in the average case?", "O(n log n)", "Medium")
    add_question(2, "What is the difference between BFS and DFS?", "BFS explores level by level, DFS explores as far as possible along each branch", "Medium")
    
    # Computer Architecture
    add_question(3, "What is the difference between RAM and ROM?", "RAM is volatile and can be written to, ROM is non-volatile and read-only", "Easy")
    add_question(3, "What is pipelining in CPU architecture?", "A technique where multiple instructions are overlapped in execution", "Hard")
    
    # Operating Systems
    add_question(4, "What is the difference between a process and a thread?", "A process is an independent program with its own memory space, while a thread is a lightweight process that shares memory with other threads", "Medium")
    add_question(4, "What is virtual memory?", "A memory management technique that uses disk space to extend RAM", "Medium")
    
    # Networks
    add_question(5, "What is the difference between TCP and UDP?", "TCP is connection-oriented and reliable, UDP is connectionless and unreliable", "Medium")
    add_question(5, "What is the purpose of DNS?", "To translate domain names into IP addresses", "Easy")
    
    # Databases
    add_question(6, "What is normalization in database design?", "The process of organizing data to minimize redundancy", "Medium")
    add_question(6, "What is the difference between SQL and NoSQL databases?", "SQL databases are relational and structured, NoSQL databases are non-relational and flexible", "Medium")
    
    # Software Engineering
    add_question(7, "What is the difference between waterfall and agile methodologies?", "Waterfall is sequential and rigid, agile is iterative and flexible", "Easy")
    add_question(7, "What is version control?", "A system that records changes to files over time", "Easy")
    
    # Programming Languages
    add_question(8, "What is the difference between compiled and interpreted languages?", "Compiled languages are translated to machine code before execution, interpreted languages are executed line by line", "Medium")
    add_question(8, "What is garbage collection?", "Automatic memory management that reclaims memory no longer in use", "Medium")
    
    # Artificial Intelligence
    add_question(9, "What is machine learning?", "A subset of AI that enables systems to learn from data", "Easy")
    add_question(9, "What is the difference between supervised and unsupervised learning?", "Supervised learning uses labeled data, unsupervised learning uses unlabeled data", "Medium")
    
    # Web Development
    add_question(10, "What is the difference between frontend and backend development?", "Frontend deals with user interface, backend deals with server-side logic", "Easy")
    add_question(10, "What is REST API?", "A software architectural style for distributed systems", "Medium")

if __name__ == "__main__":
    init_db()
    add_sample_questions()
    print("Sample questions added successfully!") 