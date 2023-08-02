from student_onboarding import *
from knowledge_base import KnowledgeBase


class Student_onboarding:
    def __init__(self, syllabus) -> None:
        self.syllabus = syllabus
        self.topic_proficiency = {}
        self.subtopic_proficiency = {}

    def normalized_val(self, original_value):
        min_value = -4
        max_value = 4

        # Calculate the normalized value
        normalized_value = (original_value - min_value) / \
            (max_value - min_value)
        # Make sure the normalized value is within the range [0, 1]
        normalized_value = max(0, min(normalized_value, 1))

        return normalized_value

    def generate_topic_prof(self, topic):
        prof = get_proficiency(topic, 'None')

        # Normalized proficiency of a topic with no subtopic:
        prof_normalized = self.normalized_val(prof)
        # print(topic, prof)
        return prof_normalized

    def generate_subtopic_prof(self, subtop_lst, topic):
        avg = 0
        subtop = {}
        for i in subtop_lst:
            prof = get_proficiency(topic, i)
            prof_normalized = self.normalized_val(prof)
            subtop[i] = prof_normalized
            avg = avg+prof_normalized
            # print(i, prof)
        top_prof = avg/len(subtop_lst)

        # Normalized proficiency of a topic with subtopics = top_prof
        # dictionary of each subtopic's normalized proficiency = subtop
        return top_prof, subtop

    def generate_initial_prof(self):
        print("------INITIAL TESTING IN PROGRESS------")
        for sec in self.syllabus:
            topics = {}
            for topic in self.syllabus[sec]:
                if self.syllabus[sec][topic] == []:
                    # print(topic)
                    proficiency_top = self.generate_topic_prof(topic)
                else:
                    # print(self.syllabus[sec][topic])
                    proficiency_top, subtop = self.generate_subtopic_prof(
                        self.syllabus[sec][topic], topic)
                    self.subtopic_proficiency[topic] = subtop
                topics[topic] = proficiency_top
            self.topic_proficiency[sec] = topics
        
        print("--------Initial topic proficiency---------")
        print(self.topic_proficiency)
        print("--------Initial subtopic proficiency---------")
        print(self.subtopic_proficiency)

# change file path here.
# filename = '../Database/Olevels Physics Data (2023-2025).csv'
# kb = KnowledgeBase()
# kb.initialize_syllabus(filename)
# student = Student_onboarding(kb.syllabus)
# student.generate_initial_prof()
# print(student.topic_proficiency)
# print(student.subtopic_proficiency)
