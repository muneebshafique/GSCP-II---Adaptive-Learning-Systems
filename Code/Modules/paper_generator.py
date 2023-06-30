import student_model
import random
import sqlite3
import updated_questiontree
#Generates Paper using Student Model and Knowledge base. 






class PaperGenerator:
    def __init__(self) -> None:
        my_student = student_model.StudentModel()
        self.topic_prof = my_student.topic_weightages(my_student.topic_proficiency)
        self.subtopic_dict = my_student.topic_weightages(my_student.subtopic_proficiency)

        # self.origi_topic_prof=my_student.topic_proficiency
        # self.origin_topic_prof=my_student.subtopic_proficiency

        self.subsec1 = ['Motion, forces and energy', 14]
        self.subsec2 = ['Thermal physics', 2]
        self.subsec3 = ['Waves', 4]
        self.subsec4 = ['Electricity and magnetism', 8]
        self.subsec5 = ['Nuclear physics', 4]
        self.subsec6 = ['Space physics', 8]

        # df = pd.read_csv("Olevels Physics Data (2023-2025).csv")

    def get_question1(self, topic_name, subtopic_name, difficulty_level):
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
        
        for row in question_rows:
            print(row)
        db_conn.close()
    

        
    def initial(self):
        for i in range(self.subsec1[1]):
            randomnumber = random.random()
            print(randomnumber)
            topics = self.topic_prof[self.subsec1[0]]
            print(topics)
            count = 0
            for i in topics:
                if randomnumber <= topics[i]:
                    yourtopic = i
                    if count == 0:
                        profficiency = topics[yourtopic]
                        break
                    else:
                        profficiency = topics[yourtopic] - topics[y]
                        break
                count += 1
                y = i
            print(yourtopic)
            print(profficiency)
            if yourtopic in self.subtopic_dict:
                subtopics = self.subtopic_dict[yourtopic]
                print(subtopics)
                randomnumber2 = random.random()
                for j in subtopics:
                    if randomnumber2 < subtopics[j]:
                        yoursubtopic = j
                        print(yoursubtopic)
                        flag = True
            else:
                
                flag = False
            
            if profficiency <= 0.3333:
                difficulty = 1
            elif profficiency > 0.3333 and profficiency <= 0.666:
                difficulty = 2
            else:
                difficulty = 3
            
            if flag == True:
                print(self.get_question1(yourtopic, yoursubtopic, difficulty))
            else:
                print( self.get_question1(yourtopic, "None", difficulty))




        

   

# Correct way
my_paper= PaperGenerator()
# paper_generator.section_weigtage()
print(my_paper.initial())
