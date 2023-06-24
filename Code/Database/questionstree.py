import sqlite3

# Connect to the database (create a new file if it doesn't exist)
# conn = sqlite3.connect('questiontree.db')
# cursor = conn.cursor()



# Create the necessary tables
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS topics (
#         topic_id INTEGER PRIMARY KEY,
#         topic_name TEXT
#     )
# ''')

# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS subtopics (
#         subtopic_id INTEGER PRIMARY KEY,
#         subtopic_name TEXT,
#         topic_id INTEGER,
#         FOREIGN KEY (topic_id) REFERENCES topics (topic_id)
#     )
# ''')

# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS questions (
#     question_id INTEGER PRIMARY KEY,
#     question_number TEXT,
#     question_text TEXT,
#     difficulty_level INTEGER,
#     subtopic_id INTEGER,
#     FOREIGN KEY (subtopic_id) REFERENCES subtopics (subtopic_id)
#     )
# ''')



# # Commit the changes and close the connection
# conn.commit()
# conn.close()

#functions for insertion

def insert_topic(topic_name):
    conn = sqlite3.connect('questiontree.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO topics (topic_name) VALUES (?)', (topic_name,))

    topic_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return topic_id


def insert_subtopic(subtopic_name, topic_id):
    conn = sqlite3.connect('questiontree.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO subtopics (subtopic_name, topic_id) VALUES (?, ?)', (subtopic_name, topic_id))
    subtopic_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return subtopic_id


def insert_question(question_number, question_text, difficulty_level, subtopic_id):
    conn = sqlite3.connect('questiontree.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO questions (question_number, question_text, difficulty_level, subtopic_id) VALUES (?, ?, ?, ?)', (question_number, question_text, difficulty_level, subtopic_id))
    question_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return question_id

#now to insert data
# topic1_id = insert_topic('Forces')
# sub1_id = insert_subtopic('Friction', topic1_id)
# sub2_id = insert_subtopic('Circular Motion', topic1_id)
# sub3_id = insert_subtopic('Elastic deformation', topic1_id)
# sub4_id = insert_subtopic('Turning effect of forces', topic1_id)
# sub5_id = insert_subtopic('Center of gravity', topic1_id)


# for i in range(1, 11):
#     insert_question(f'Q{i}', f'Question {i}/o/n/20anything', 1, sub1_id) #10 for easy

# for i in range(1, 11):
#     insert_question(f'Q{i}', f'Question {i}/o/n/20anything', 2, sub1_id) #10 for moderate 

# for i in range(1, 11):
#     insert_question(f'Q{i}', f'Question {i}/o/n/20anything', 3, sub1_id) #10 for hard

def get_question(topic_id, subtopic_id, difficulty_level):
    conn = sqlite3.connect('questiontree.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT question_id, question_number, question_text
        FROM questions
        WHERE subtopic_id = ? AND difficulty_level = ?
        AND subtopic_id IN (
            SELECT subtopic_id
            FROM subtopics
            WHERE topic_id = ?
        )
    ''', (subtopic_id, difficulty_level, topic_id))
    question = cursor.fetchall()
    conn.close()
    return question if question else None


question = get_question(1, 1, 1)
print(question)
