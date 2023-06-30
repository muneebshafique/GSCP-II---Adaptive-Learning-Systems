import random
import copy
import knowledge_base

MAX_PROFICIENCY = 10
SIG_FIGURES=3
#Stores topic proficiency of student & questions attempted by student
class StudentModel:
    def __init__(self) -> None:
        kb = knowledge_base.KnowledgeBase()
        self.syllabus = kb.syllabus
        self.topic_proficiency={'Motion, forces and energy': {'Physical quantities and measurement techniques': 5, 'Motion': 6, 'Mass and Weight': 4, 'Density': 1, 'Forces': 5.833, 'Momentum': 7, 'Energy, work and power ': 5.0, 'Pressure': 5}, 'Thermal physics': {'Kinetic particle model of matter': 7.5, 'Thermal properties and temperatuare': 5.0, 'Transfer of thermal energy': 5.0}, 'Waves': {'General properties of waves': 3, 'Light': 7.75, 'Electromagnetic spectrum': 5, 'Sound': 4}, 'Electricity and magnetism': {'Simple magnetism and magnetic field': 7, 'Electrical quantities': 4.75, 'Electric Circuits': 2.667, 'Practical Electricity': 3.0, 'Electromagnetic effects ': 4.667, 'Uses of Oscilloscope': 8}, 'Nuclear physics': {'The nuclear model of the atom': 6.5, 'Radioactivity': 5.167}, 'Space physics': {'Earth and the Solar System': 4.5, 'Stars and the Universe': 6.0}}
        self.subtopic_proficiency = {'Forces': {'Balanced and unbalanced forces': 7, 'Friction': 2, 'Elastic deformation': 2, 'Circular motion': 10, 'Turning effect of forces': 10, 'Centre of gravity': 4}, 'Energy, work and power ': {'Energy': 3, 'Work': 7, 'Energy resources': 1, 'Efficiency': 9, 'Power': 5}, 'Kinetic particle model of matter': {'States of matter': 7, 'Particle model': 8}, 'Thermal properties and temperatuare': {'Thermal expansion of solids, liquids and gases': 5, 'Specific heat capacity': 9, 'Melting, boiling and evaporation': 1}, 'Transfer of thermal energy': {'Conduction': 1, 'Convection': 8, 'Radiation': 2, 'Consequences of thermal energy transfer': 9}, 'Light': {'Reflection of light': 10, 'Refraction of light': 10, 'Thin lenses': 9, 'Dispersion of light': 2}, 'Electrical quantities': {'Electrical charge': 5, 'Electrical current': 9, 'Electromotive force and potential difference': 3, 'Resistance': 2}, 'Electric Circuits': {'Circuit diagram and circuit components': 4, 'Series and parallel circuits': 2, 'Action and use of circuit components': 2}, 'Practical Electricity': {'Uses of electricity': 5, 'Electrical Safety': 1}, 'Electromagnetic effects ': {'Electromagnetic induction': 5, 'The a.c. generator': 4, 'Magnetic effect of a current': 2, 'Forces on a current-carrying conductor': 7, 'The d.c. motor': 2, 'The transformer': 8}, 'The nuclear model of the atom': {'The atom': 3, 'The nucleus': 10}, 'Radioactivity': {'Detection of radioactivity': 7, 'The three types of emission': 3, 'Radioactive decay': 5, 'Fission and fusion': 3, 'Half-life': 9, 'Safety precautions': 4}, 'Earth and the Solar System': {'The earth': 4, 'The solar system': 5}, 'Stars and the Universe': {'The sun as a star': 5, 'Stars': 7, 'The universe': 6}}

        # print("-------Topic proficiency---------")
        # print(self.topic_proficiency)
        # print("------SUB - Topic proficiency---------")
        # print(self.subtopic_proficiency)

    # assigns student proficiency for every topic
    def dummy_data_student_proficiency(self):
        global SIG_FIGURES
        self.topic_proficiency={}
        self.subtopic_proficiency={}

        # initializing topic proficiency and sub-topic proficiency
        for section, topics in self.syllabus.items():
            self.topic_proficiency[section]={}
            for topic, subtopics in topics.items():
                proficiency = random.randint(1, MAX_PROFICIENCY)
                self.topic_proficiency[section][topic] = proficiency
                if (len(subtopics) != 0):
                    self.subtopic_proficiency[topic]={}
                    for subtopic in subtopics:
                        proficiency = random.randint(1, 10)
                        self.subtopic_proficiency[topic][subtopic] = proficiency
 
        # initializing topic proficiency for topics with sub-topics(avg)
        for topic, subtopics in self.subtopic_proficiency.items():
            subtopic_proficiency_sum=0
            for subtopic in subtopics:
                subtopic_proficiency_sum+= self.subtopic_proficiency[topic][subtopic]
            # print(subtopic_proficiency_sum)
            for section, topics in self.topic_proficiency.items():
                if topic in topics:
                    self.topic_proficiency[section][topic]=round(subtopic_proficiency_sum/len(subtopics),SIG_FIGURES)
    

    #normalizes topic and sub-topic proficiency
    def topic_weightages(self,proficiency_dict):
        global MAX_PROFICIENCY
        normalized_proficiency_dict={}

        for section,topics in proficiency_dict.items():
            normalized_proficiency_dict[section]={}
            topic_proficiency_sum=0
            for topic in topics:
                topic_proficiency_sum+=MAX_PROFICIENCY-proficiency_dict[section][topic]
            pointer=0
            for topic in topics:
                normalized_prof=(MAX_PROFICIENCY-proficiency_dict[section][topic])/topic_proficiency_sum
                
                normalized_proficiency_dict[section][topic] = pointer+normalized_prof
                pointer += normalized_prof
        return (normalized_proficiency_dict)
      


# my_student = StudentModel()
# my_student.dummy_data_student_proficiency()
# normalized_topic_proficiency=my_student.topic_weightages(my_student.topic_proficiency)
# print("-------Normalized Topic proficiency---------")
# print(normalized_topic_proficiency)
# normalized_subtopic_proficiency=my_student.topic_weightages(my_student.subtopic_proficiency)
# print("\n-------Normalized SUBTopic proficiency---------")
# print(normalized_subtopic_proficiency)



