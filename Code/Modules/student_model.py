import random
import copy
import knowledge_base

MAX_PROFICIENCY = 10
SIG_FIGURES=3
#Stores topic proficiency of student & questions attempted by student
class StudentModel:
    def __init__(self) -> None:
        kb = knowledge_base.KnowledgeBase()
        # kb.initialize_syllabus("../Database/Olevels Physics Data (2023-2025).csv")
        self.syllabus = kb.syllabus
        self.topic_proficiency={'Motion, forces and energy': {'Physical quantities and measurement techniques': 10, 'Motion': 3, 'Mass and Weight': 8, 'Density': 2, 'Forces': 5.5, 'Momentum': 1, 'Energy, work and power ': 3.8, 'Pressure': 7}, 'Thermal physics': {'Kinetic particle model of matter ': 1.5, 'Thermal properties and temperature': 2.333, 'Transfer of thermal energy ': 5.5}, 'Waves': {'General properties of waves ': 9, 'Light ': 6.25, 'Electromagnetic spectrum': 10, 'Sound ': 10}, 'Electricity and magnetism': {'Simple magnetism and magnetic field ': 1, 'Electrical quantities ': 6.25, 'Electric Circuits': 3.333, 'Practical Electricity': 6.0, 'Electromagnetic effects ': 5.5, 'Uses of Oscilloscope': 10}, 'Nuclear physics': {'The nuclear model of the atom ': 4.0, 'Radioactivity ': 6.333}, 'Space physics': {'Earth and the Solar System ': 4.5, 'Stars and the Universe ': 6.667}}
        self.subtopic_proficiency = {'Forces': {'Balanced and unbalanced forces': 5, 'Friction': 4, 'Elastic deformation': 3, 'Circular motion': 7, 'Turning effect of forces': 5, 'Centre of gravity': 9}, 'Energy, work and power ': {'Energy ': 1, 'Work': 6, 'Energy resources': 2, 'Efficiency': 3, 'Power': 7}, 'Kinetic particle model of matter ': {'States of matter ': 1, 'Particle model ': 2}, 'Thermal properties and temperature': {'Thermal expansion of solids, liquids and gases ': 3, 'Specific heat capacity ': 1, 'Melting, boiling and evaporation ': 3}, 'Transfer of thermal energy ': {'Conduction ': 1, 'Convection ': 9, 'Radiation ': 5, 'Consequences of thermal energy transfer ': 7}, 'Light ': {'Reflection of light ': 3, 'Refraction of light ': 10, 'Thin lenses ': 9, 'Dispersion of light ': 3}, 'Electrical quantities ': {'Electrical charge ': 9, 'Electrical current ': 10, 'Electromotive force and potential difference ': 4, 'Resistance ': 2}, 'Electric Circuits': {'Circuit diagram and circuit components': 6, 'Series and parallel circuits': 1, 'Action and use of circuit components': 3}, 'Practical Electricity': {'Uses of electricity': 4, 'Electrical Safety': 8}, 'Electromagnetic effects ': {'Electromagnetic induction ': 7, 'The a.c. generator ': 4, 'Magnetic effect of a current ': 3, 'Forces on a current-carrying conductor ': 9, 'The d.c. motor ': 8, 'The transformer ': 2}, 'The nuclear model of the atom ': {'The atom ': 3, 'The nucleus ': 5}, 'Radioactivity ': {'Detection of radioactivity ': 8, 'The three types of emission ': 4, 'Radioactive decay ': 5, 'Fission and fusion ': 10, 'Half-life ': 5, 'Safety precautions ': 6}, 'Earth and the Solar System ': {'The earth ': 5, 'The solar system ': 4}, 'Stars and the Universe ': {'The sun as a star ': 5, 'Stars ': 10, 'The universe ': 5}}

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
# print("Topic proficiency")
# print(my_student.topic_proficiency)
# print("Sub topic proficiency")
# print(my_student.subtopic_proficiency)

# normalized_topic_proficiency=my_student.topic_weightages(my_student.topic_proficiency)
# print("-------Normalized Topic proficiency---------")
# print(normalized_topic_proficiency)
# normalized_subtopic_proficiency=my_student.topic_weightages(my_student.subtopic_proficiency)
# print("\n-------Normalized SUBTopic proficiency---------")
# print(normalized_subtopic_proficiency)



