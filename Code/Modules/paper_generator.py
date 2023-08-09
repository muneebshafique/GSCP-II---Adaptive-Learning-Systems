import evaluation
import student_model
import knowledge_base
import random
import sqlite3
import updated_questiontree

DIFF_LEVEL_1 = 0.33
DIFF_LEVEL_2 = 0.66

class PaperGenerator():
    def __init__(self,filename,kb, my_student) -> None:

        self.my_student = my_student
        self.topic_proficiency=my_student.topic_proficiency
        self.subtopic_proficiency = my_student.subtopic_proficiency
        self.normalized_topic_proficiency = my_student.topic_probability(self.topic_proficiency)
        self.normalized_subtopic_proficiency = my_student.topic_probability(self.subtopic_proficiency)
        self.section_weightage=kb.section_weightage


    # fetches questions from database
    # problem : Picking same questions if more qs are coming from a topic/subtopic.
    def get_question(self, topic_name, subtopic_name, difficulty_level):
        db_conn = sqlite3.connect("updated_questiontree.db")
        cursor =db_conn.cursor()
        cursor.execute('''
        SELECT q.QuestionID, q.QuestionName, q.QuestionNumber, q.Diff_Level, q.Diff_Val
        FROM Question q
        INNER JOIN SubTopic st ON q.SubTopicID = st.SubTopicID
        INNER JOIN Topic t ON st.TopicID = t.TopicID
        WHERE t.TopicName = ? AND st.SubTopicName = ? AND q.Diff_Level = ? 
    ''', (topic_name, subtopic_name, difficulty_level))

        question_rows = cursor.fetchall()
        # print(question_rows)
        sorted_list_question = sorted(question_rows, key=lambda x: x[4])
        # random_question = random.choice(question_rows)
        question = sorted_list_question[-1]
        i=-2
        while question[0] in self.paper:
            question=sorted_list_question[i]
            i-=1

        return(question[0])
   
        db_conn.close()


    
    #picks topics and subtopics based on user proficiency 
    def generate_paper(self,):
        self.paper=[]
        paper_info={}
        qs_num = 1

        for section, weightage in self.section_weightage.items():
            # print("-------------",section,"------------")
            for i in range (self.section_weightage[section]):
                paper_info[qs_num]=[]
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
                                    paper_info[qs_num].append((selected_topic,selected_subtopic,qs_difficulty))
                                    # print(selected_topic,selected_subtopic,qs_difficulty)
                                    actual_qs=self.get_question(selected_topic, selected_subtopic, qs_difficulty)
                                    self.paper.append(actual_qs)
                                    break
                            break
                        else:
                            proficiency=self.topic_proficiency[section][selected_topic]
                            qs_difficulty=self.get_difficulty_level(proficiency)
                            paper_info[qs_num].append((selected_topic,selected_subtopic,qs_difficulty))
                            # print(selected_topic,selected_subtopic,qs_difficulty)
                            actual_qs=self.get_question(selected_topic, selected_subtopic, qs_difficulty)
                            self.paper.append(actual_qs)
                            break
                qs_num+=1
        
        return self.paper,paper_info
        
        
    # converts proficiency to difficulty level of question to be picked. 
    def get_difficulty_level(self,proficiency):

        if proficiency <= DIFF_LEVEL_1:
            difficulty = 1
        elif proficiency <= DIFF_LEVEL_2:
            difficulty = 2
        else:
            difficulty = 3
            
        return difficulty
    
    #prints the paper_info
    def print_paper_info(self,paper_info):
        print("------------PRINTING PAPER INFO---------")
        for qs_num, qs_info in paper_info.items():
            print(qs_num, " : ", qs_info)

    def print_paper(self, paper):
        print("------------PRINTING ACTUAL PAPER---------")
        for i in range(len(paper)):
            print(i+1,": ",paper[i])


# filename ="../Database/Olevels Physics Data (2023-2025).csv"
# pg = PaperGenerator(filename)

