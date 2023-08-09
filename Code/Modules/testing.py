import sqlite3
import updated_questiontree


def get_diff_val(qs_id, topic_name, sub_topic_name):
    db_conn = sqlite3.connect("updated_questiontree.db")
    cursor = db_conn.cursor()
    cursor.execute('''
        SELECT Diff_Val FROM Question
        WHERE QuestionID = ? 
        AND SubTopicID = (
            SELECT SubTopicID
            FROM SubTopic
            WHERE SubTopicName = ? 
            AND TopicID = (
                SELECT TopicID 
                FROM Topic 
                WHERE TopicName = ?
            )
        )
    ''', (qs_id, sub_topic_name, topic_name))
    diff_val = cursor.fetchall()
    diff = diff_val[0][0]
    db_conn.close()
    return diff


print(get_diff_val(230, 'Forces', 'Circular motion'))
