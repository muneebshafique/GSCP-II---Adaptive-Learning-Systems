import random
import copy
import knowledge_base

MAX_PROFICIENCY = 10
#Stores topic proficiency of student & questions attempted by student
class StudentModel:
    def __init__(self) -> None:
        kb = knowledge_base.KnowledgeBase()
        self.syllabus = kb.syllabus
        self.student_proficiency = {'Motion, forces and energy': {'Physical quantities and measurement techniques': 7, 'Motion': 1, 'Mass and Weight': 5, 'Density': 2, 'Forces': {'subtopics': {'Balanced and unbalanced forces': 5, 'Friction': 9, 'Elastic deformation': 7, 'Circular motion': 10, 'Turning effect of forces': 8, 'Centre of gravity': 6}, 'topic_proficiency': 7.5}, 'Momentum': 8, 'Energy, work and power ': {'subtopics': {'Energy ': 5, 'Work': 5, 'Energy resources': 3, 'Efficiency': 7, 'Power': 8}, 'topic_proficiency': 5.6}, 'Pressure': 6}, 'Thermal physics': {'Kinetic particle model of matter': {'subtopics': {'States of matter': 4, 'Particle model': 3}, 'topic_proficiency': 3.5}, 'Thermal properties and temperatuare': {'subtopics': {'Thermal expansion of solids, liquids and gases': 10, 'Specific heat capacity': 5, 'Melting, boiling and evaporation': 7}, 'topic_proficiency': 7.333333333333333}, 'Transfer of thermal energy': {'subtopics': {'Conduction': 8, 'Convection': 10, 'Radiation': 3, 'Consequences of thermal energy transfer': 8}, 'topic_proficiency': 7.25}}, 'Waves': {'General properties of waves': 2, 'Light': {'subtopics': {'Reflection of light': 10, 'Refraction of light': 9, 'Thin lenses': 9, 'Dispersion of light': 8}, 'topic_proficiency': 9.0}, 'Electromagnetic spectrum': 9, 'Sound': 7}, 'Electricity and magnetism': {'Simple magnetism and magnetic field': 8, 'Electrical quantities': {'subtopics': {'Electrical charge': 5, 'Electrical current': 2, 'Electromotive force and potential difference': 8, 'Resistance': 4}, 'topic_proficiency': 4.75}, 'Electric Circuits': {'subtopics': {'Circuit diagram and circuit components': 6, 'Series and parallel circuits': 1, 'Action and use of circuit components': 2}, 'topic_proficiency': 3.0}, 'Practical Electricity': {'subtopics': {'Uses of electricity': 9, 'Electrical Safety': 2}, 'topic_proficiency': 5.5}, 'Electromagnetic effects ': {'subtopics': {'Electromagnetic induction': 7, 'The a.c. generator': 5, 'Magnetic effect of a current': 8, 'Forces on a current-carrying conductor': 10, 'The d.c. motor': 9, 'The transformer': 4}, 'topic_proficiency': 7.166666666666667}, 'Uses of Oscilloscope': 1}, 'Nuclear physics': {'The nuclear model of the atom': {'subtopics': {'The atom': 9, 'The nucleus': 2}, 'topic_proficiency': 5.5}, 'Radioactivity': {'subtopics': {'Detection of radioactivity': 6, 'The three types of emission': 8, 'Radioactive decay': 4, 'Fission and fusion': 5, 'Half-life': 1, 'Safety precautions': 1}, 'topic_proficiency': 4.166666666666667}}, 'Space physics': {'Earth and the Solar System': {'subtopics': {'The earth': 1, 'The solar system': 9}, 'topic_proficiency': 5.0}, 'Stars and the Universe': {'subtopics': {'The sun as a star': 1, 'Stars': 8, 'The universe': 1}, 'topic_proficiency': 3.3333333333333335}}}
        
        # print("--------STUDENT PROFICIENCY-------")
        # print(self.student_proficiency)
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

        print("---------Student Proficiency---------")
        print(student_proficiency)
        print("---------Number of Sections -----------")
        print(len(student_proficiency))

    #assigns weightage to each topic based on student proficiency
    def topic_weightages(self):
        proficiencies=[]
        section_prof_sum=[]
        topic_prof_sum=[]
        normalized_weightage=[]
        global MAX_PROFICIENCY

        #generating nested list containing proficiency of each topic,subtopic section wise.
        for section, topics in self.student_proficiency.items():
            topic_proficiencies = []
            sum_topic_proficiency=0
            for topic, value in topics.items():
                if isinstance(value, dict):
                    subtopic_sum=0
                    subtopic_proficiencies = []
                    subtopic_proficiencies.append(value['topic_proficiency'])
                    sum_topic_proficiency+=MAX_PROFICIENCY-value['topic_proficiency']
                    for subtopic, subtopic_proficiency in (value['subtopics']).items():
                        subtopic_proficiencies.append(subtopic_proficiency)
                        subtopic_sum+=MAX_PROFICIENCY-subtopic_proficiency
                    topic_proficiencies.append(subtopic_proficiencies)
                    topic_prof_sum.append(subtopic_sum)
                else:
                    topic_proficiencies.append(value)
                    sum_topic_proficiency+=MAX_PROFICIENCY-value
                    # print(topic, value)
            proficiencies.append(topic_proficiencies)
            section_prof_sum.append(sum_topic_proficiency)

        #normalizing proficiencies
        i=0
        j=0
        for section in proficiencies:
            temp=[]
            for prof in section:
                if isinstance(prof, list):
                    # copied_prof = copy.deepcopy(prof)
                    subtopic_temp=[]
                    for subtopic_prof in prof:
                        subtopic_temp.append((MAX_PROFICIENCY-subtopic_prof)/ topic_prof_sum[j])
                    subtopic_temp[0]=(MAX_PROFICIENCY-prof[0])/section_prof_sum[i]
                    temp.append(subtopic_temp)
                    j+=1
                else:
                    temp.append((MAX_PROFICIENCY-prof)/section_prof_sum[i])
            i+=1
            normalized_weightage.append(temp)

        print("---------SECTION WISE PROFICIENCY--------")
        print(proficiencies)
        print("--------SUM SECTION PROFICIENCY---------")
        print(section_prof_sum)
        print("---------SUM TOPIC PROFICIENCY----------")
        print(topic_prof_sum)
        print("-----------NORMALIZED WEIGHTAGE---------")
        print(normalized_weightage)
        print(len(normalized_weightage))
        
        self.ranges(normalized_weightage)
   
    #defines ranges for each topic and subtopic
    def ranges(self,normalized_weightage):
        ranges={}
        
        proficiency_ranges= []

        # for section, topics in self.syllabus.items():
        #     # for section in normalized_weightage:
        #         proficiency_ranges[section]={}
        #         for topic, subtopics in topics.items():
        #             if subtopics:
        #                 subtopic_proficiency = []
        #                 for subtopic in subtopics:
        #                     subtopic_proficiency.append(0)
        #                     proficiency_ranges[section][topic] = {
        #                         'subtopics': {subtopic: proficiency for subtopic, proficiency in zip(subtopics, subtopic_proficiency)},
        #                         'topic_proficiency': 0
        #                     }
        #             else:
        #                 proficiency_ranges[section][topic] = 0
        
        # print(proficiency_ranges)

        for section in normalized_weightage:
            topic_pointer = 0
            topic_limits=[]
            for topic_prof in section:
                if isinstance(topic_prof, list):
                    subtopic_pointer=0
                    subtopic_limits=[]
                    for i in range(1,len(topic_prof)):
                        limits = [subtopic_pointer, subtopic_pointer + topic_prof[i]] 
                        subtopic_limits.append(limits)
                        subtopic_pointer+= topic_prof[i]

                    limits = [topic_pointer, topic_pointer + topic_prof[0]] 
                    topic_pointer += topic_prof[0]
                    subtopic_limits.insert(0, limits)
                    topic_limits.append(subtopic_limits)
                else:
                    limits = [topic_pointer, topic_pointer + topic_prof] 
                    topic_limits.append(limits)
                    topic_pointer += topic_prof

            proficiency_ranges.append(topic_limits)

        print(proficiency_ranges)
       


my_student = StudentModel()
# my_student.dummy_data_student_proficiency()
my_student.topic_weightages()


#[[3,5,1,[9,2,3,5],3,4] ,
# []