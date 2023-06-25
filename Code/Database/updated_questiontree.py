import sqlite3
import pandas as pd

# db_conn = sqlite3.connect("updated_questiontree.db")
# cursor = db_conn.cursor()

# cursor.execute(
#     ''' CREATE TABLE IF NOT EXISTS Section(
#     SectionID INTEGER,
#     SectionName TEXT,
#     PRIMARY KEY(SectionID)
#     )
# ''')


# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS Topic(
#     TopicID INTEGER,
#     TopicName TEXT,
#     SectionID INTEGER,
#     PRIMARY KEY(TopicID)
#     FOREIGN KEY(SectionID) REFERENCES Section(SectionID)
#     )
#     ''')

# cursor.execute(
#     """CREATE TABLE IF NOT EXISTS SubTopic(
#     SubTopicID INTEGER,
#     SubTopicName TEXT,
#     TopicID INTEGER,
#     PRIMARY KEY(SubTopicID)
#     FOREIGN KEY(TopicID) REFERENCES Topic(TopicID)
#     )
#     """
# )

# cursor.execute(
#     """CREATE TABLE IF NOT EXISTS Question(
#     QuestionID INTEGER,
#     QuestionName TEXT,
#     QuestionNumber TEXT,
#     Diff_Level INTEGER,
#     SubTopicID INTEGER,
#     PRIMARY KEY(QuestionID)
#     FOREIGN KEY(SubTopicID) REFERENCES SubTopic(SubTopicID)
#     )
#     """
# )

# db_conn.commit()
# db_conn.close()


############# INSERTING DIRECTLY FROM CSV FILE #############
df = pd.read_csv("Olevels Physics Data (2023-2025).csv")


########### INSERTING DATA INTO SECTION TABLE ###########

# def insert_section():
#     sections = df["Section"].unique()
#     print(sections)
#     db_conn = sqlite3.connect('updated_questiontree.db')
#     cursor = db_conn.cursor()
#     count = 1
#     for i in sections:
#         cursor.execute(
#             'INSERT INTO Section (SectionID, SectionName) VALUES (?, ?)', (count, i))
#         count = count+1

#     db_conn.commit()
#     db_conn.close()


# insert_section()

############## INSERTING DATA INTO TOPIC TABLE ##########


# def insert_topic():
#     sections = df["Section"].unique()
#     db_conn = sqlite3.connect("updated_questiontree.db")
#     cursor = db_conn.cursor()
#     tid = 1
#     for i in sections:
#         cursor.execute('''
#         SELECT SectionID
#         FROM Section
#         WHERE SectionName = ? ''', (i, ))
#         s_id = cursor.fetchall()
#         s_id = s_id[0][0]
#         topics = df[df['Section'] == i]['Topic'].unique()
#         for t in topics:
#             cursor.execute(
#                 'INSERT INTO Topic (TopicID, TopicName, SectionID) VALUES (?, ?, ?)', (tid, t, s_id))
#             tid = tid+1
#     db_conn.commit()
#     db_conn.close()


# insert_topic()


############## INSERTING DATA INTO SUB-TOPIC TABLE ##########

# def insert_subtopic(topic, subtop_arr, count):
#     db_conn = sqlite3.connect("updated_questiontree.db")
#     cursor = db_conn.cursor()
#     cursor.execute('''
#         SELECT TopicID
#         FROM Topic
#         WHERE TopicName = ? ''', (topic, ))
#     t_id = cursor.fetchall()
#     t_id = t_id[0][0]
#     for sub in subtop_arr:
#         cursor.execute(
#             'INSERT INTO SubTopic (SubTopicID, SubTopicName, TopicID) VALUES (?, ?, ?)', (count, sub, t_id))
#         count = count+1
#     db_conn.commit()
#     db_conn.close()
#     return count


# sections = df["Section"].unique()
# count = 1
# for i in sections:
#     topics = df[df['Section'] == i]['Topic'].unique()
#     for t in topics:
#         subtopics = df[df['Topic'] == t]['Sub Topic'].unique()
#         if subtopics.size > 1:
#             count = insert_subtopic(t, subtopics, count)


########## INSERTING DATA INTO QUESTION TABLE (MANUALLY) #############

# def insert_question(question_number, question_text, difficulty_level, subtopic_id):
#     db_conn = sqlite3.connect("updated_questiontree.db")
#     cursor = db_conn.cursor()
#     cursor.execute('INSERT INTO Question (QuestionNumber, QuestionName, Diff_Level, SubTopicID) VALUES (?, ?, ?, ?)',
#                    (question_number, question_text, difficulty_level, subtopic_id))
#     question_id = cursor.lastrowid
#     db_conn.commit()
#     db_conn.close()
#     return question_id


# # For subtopic 1:
# sub1_id = 1
# for i in range(1, 11):
#     insert_question(f'Q{i}', f'Question {i}/o/n/20anything',
#                     1, sub1_id)  # 10 for easy

# for i in range(1, 11):
#     insert_question(f'Q{i}', f'Question {i}/o/n/20anything',
#                     2, sub1_id)  # 10 for moderate

# for i in range(1, 11):
#     insert_question(f'Q{i}', f'Question {i}/o/n/20anything',
#                     3, sub1_id)  # 10 for hard


###################### PRINTING TABLES #########################

# Printing sections Table:
db_conn = sqlite3.connect("updated_questiontree.db")
cursor = db_conn.cursor()
cursor.execute('''
    SELECT * FROM Section
''',)
sections = cursor.fetchall()
print(sections)

db_conn.commit()
db_conn.close()

# Printing Topic Table:
db_conn = sqlite3.connect("updated_questiontree.db")
cursor = db_conn.cursor()
cursor.execute('''
    SELECT * FROM Topic
''',)
topics = cursor.fetchall()
print(topics)

db_conn.commit()
db_conn.close()

# Printing SubTopic Table:
db_conn = sqlite3.connect("updated_questiontree.db")
cursor = db_conn.cursor()
cursor.execute('''
    SELECT * FROM SubTopic
''',)
topics = cursor.fetchall()
print(topics)

db_conn.commit()
db_conn.close()

# Printing Question Table
db_conn = sqlite3.connect("updated_questiontree.db")
cursor = db_conn.cursor()
cursor.execute('''
    SELECT * FROM Question
''',)
topics = cursor.fetchall()
print(topics)

db_conn.commit()
db_conn.close()


def get_question(topic_id, subtopic_id, difficulty_level):
    db_conn = sqlite3.connect("updated_questiontree.db")
    cursor = db_conn.cursor()
    cursor.execute('''
        SELECT QuestionID, QuestionNumber, QuestionName
        FROM Question
        WHERE SubTopicID = ? AND Diff_Level = ?
        AND SubTopicID IN (
            SELECT SubTopicID
            FROM SubTopic
            WHERE TopicID = ?
        )
    ''', (subtopic_id, difficulty_level, topic_id))
    question = cursor.fetchall()
    db_conn.close()
    return question if question else None


question = get_question(1, 1, 1)
print(question)
