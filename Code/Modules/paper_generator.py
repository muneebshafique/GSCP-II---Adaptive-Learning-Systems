import evaluation
import student_model
import knowledge_base
import random
import sqlite3
import updated_questiontree

DIFF_LEVEL_1 = 0.33
DIFF_LEVEL_2 = 0.66

class PaperGenerator():
    def __init__(self,filename) -> None:
        self.evaluate = evaluation.Evaluation()
        kb = knowledge_base.KnowledgeBase()
        kb.initialize_syllabus(filename)
        self.my_student = student_model.StudentModel()
        self.topic_proficiency=self.my_student.topic_proficiency
        self.subtopic_proficiency = self.my_student.subtopic_proficiency
        self.normalized_topic_proficiency = self.my_student.topic_probability(self.topic_proficiency)
        self.normalized_subtopic_proficiency = self.my_student.topic_probability(self.subtopic_proficiency)
        self.section_weightage=kb.section_weightage
        self.paper={}
        # # print("-------Topic proficiency------")
        # # print(self.topic_proficiency)
        # # print("-------SUB Topic proficiency------")
        # # print(self.subtopic_proficiency)
        # print("-------Normalized topic proficiency ------")
        # print(self.normalized_topic_proficiency)
        # print("-------Normalized Sub topic proficiency ------")
        # print(self.normalized_subtopic_proficiency)

        self.generate_paper()


    # fetches questions from database
    def get_question(self, topic_name, subtopic_name, difficulty_level):
        db_conn = sqlite3.connect("updated_questiontree.db")
        cursor =db_conn.cursor()
        cursor.execute('''
        SELECT q.QuestionID, q.QuestionName, q.QuestionNumber, q.Diff_Level
        FROM Question q
        INNER JOIN SubTopic st ON q.SubTopicID = st.SubTopicID
        INNER JOIN Topic t ON st.TopicID = t.TopicID
        WHERE t.TopicName = ? AND st.SubTopicName = ? AND q.Diff_Level = ?
    ''', (topic_name, subtopic_name, difficulty_level))

        question_rows = cursor.fetchall()
        random_question = random.choice(question_rows)
        print(random_question)
        # print(question_rows)
        # db_conn.close()

        # for row in question_rows:
        #     print(row)
        db_conn.close()


    
    #picks topics and subtopics based on user proficiency 
    def generate_paper(self):
        qs_num = 1
        for section, weightage in self.section_weightage.items():
            # print("-------------",section,"------------")
            for i in range (self.section_weightage[section]):
                self.paper[qs_num]=[]
                randomnumber = random.random()
                selected_topic,selected_subtopic="None","None"
                topics = self.normalized_topic_proficiency[section]
                for topic, topic_weightage in topics.items():
                    
                    if randomnumber <= topic_weightage:
                        selected_topic = topic
                        if selected_topic in self.normalized_subtopic_proficiency:
                            subtopics= self.normalized_subtopic_proficiency[selected_topic]
                            for subtopic,subtopic_weightage in subtopics.items():
                                if randomnumber <= subtopic_weightage:
                                    selected_subtopic = subtopic
                                    proficiency = self.subtopic_proficiency[selected_topic][selected_subtopic]
                                    qs_difficulty=self.get_difficulty_level(proficiency)
                                    self.paper[qs_num].append((selected_topic,selected_subtopic,qs_difficulty))
                                    # print(selected_topic,selected_subtopic,qs_difficulty)
                                    # self.get_question(selected_topic, selected_subtopic, qs_difficulty)
                                    break
                            break
                        else:
                            proficiency=self.topic_proficiency[section][selected_topic]
                            qs_difficulty=self.get_difficulty_level(proficiency)
                            self.paper[qs_num].append((selected_topic,selected_subtopic,qs_difficulty))
                            # print(selected_topic,selected_subtopic,qs_difficulty)
                            # self.get_question(selected_topic, selected_subtopic, qs_difficulty)
                            break
                qs_num+=1
                
        self.print_paper()
        response=self.my_student.generate_response(self.paper)
        checked_paper=self.evaluate.check_paper(response)
        student_ability=self.my_student.Q_generate_new_proficiencies(checked_paper,self.paper)
        self.my_student.Q_update_student_proficiency(student_ability)
        # self.my_student.Q_update_student_model

        
    # converts proficiency to difficulty level of question to be picked. 
    def get_difficulty_level(self,proficiency):

        if proficiency <= DIFF_LEVEL_1:
            difficulty = 1
        elif proficiency <= DIFF_LEVEL_2:
            difficulty = 2
        else:
            difficulty = 3
            
        return difficulty
    

    def print_paper(self):
        print("------------PRINTING PAPER-------")
        # print(len(self.paper))
        for qs_num, qs_info in self.paper.items():
            print(qs_num, " : ", qs_info)

            # print(qs)

filename ="../Database/Olevels Physics Data (2023-2025).csv"
pg = PaperGenerator(filename)

