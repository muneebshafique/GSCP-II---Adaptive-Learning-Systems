import sqlite3
import updated_questiontree
import random

# Used to asses the student's response


class Evaluation():
    def __init__(self) -> None:
        pass

    def get_answer(self, topic_name, sub_topic_name, difficulty):
        db_conn = sqlite3.connect("updated_questiontree.db")
        cursor = db_conn.cursor()
        cursor.execute('''
        SELECT ANSWER FROM Question
        WHERE Diff_Level = ? 
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
    ''', (difficulty, sub_topic_name, topic_name))
        topicid_ = cursor.fetchall()
        topicid = topicid_[0][0]
        db_conn.close()
        return topicid

    def check_paper(self, response, paper):
        checked_paper = []
        count = 0
        for qs in paper:
            qs_detail = paper[qs][0]
            topic_name, sub_topic_name, difficulty = qs_detail[0], qs_detail[1], qs_detail[2]
            correct_answer = self.get_answer(
                topic_name, sub_topic_name, difficulty)
            student_answer = response[count]
            count = count+1
            if student_answer == correct_answer:
                checked_paper.append(1)
            else:
                checked_paper.append(0)

        # checked_paper = []
        # options = [0, 1]
        # for option in response:
        #     random_option = random.choice(options)
        #     checked_paper.append(random_option)

        print("\n--------CHECKED RESPONSE-------")
        print(checked_paper)
        return checked_paper
