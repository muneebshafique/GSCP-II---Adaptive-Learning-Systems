import random
import knowledge_base


#Stores topic proficiency of student & questions attempted by student
class StudentModel:
    def __init__(self) -> None:
        kb = knowledge_base.KnowledgeBase()
        self.syllabus = kb.syllabus

    # assigns student proficiency for every topic
    def dummy_data_student_proficiency(self):
        student_proficiency = {}
        for section, topics in self.syllabus.items():
            student_proficiency[section]={}
            for topic, subtopics in topics.items():
                if subtopics:
                    subtopic_proficiency = []
                    for subtopic in subtopics:
                        proficiency = random.randint(1, 10)
                        subtopic_proficiency.append(proficiency)
                        student_proficiency[section][topic] = {
                            'subtopics': {subtopic: proficiency for subtopic, proficiency in zip(subtopics, subtopic_proficiency)},
                            'topic_proficiency': sum(subtopic_proficiency) / len(subtopic_proficiency)
                        }
                else:
                    proficiency = random.randint(1, 10)
                    student_proficiency[section][topic] = proficiency
           
        print(student_proficiency)
        print(len(student_proficiency))

     


my_student = StudentModel()
my_student.dummy_data_student_proficiency()