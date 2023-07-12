import random
import copy
import knowledge_base

MAX_PROFICIENCY = 10
SIG_FIGURES=3
CATSIM_WEIGHTAGE=10

#Stores topic,subtopic proficiency of student & questions attempted by student
class StudentModel:
    def __init__(self) -> None:
        kb = knowledge_base.KnowledgeBase()
        kb.initialize_syllabus("../Database/Olevels Physics Data (2023-2025).csv")
        self.topic_section_mapping = kb.topic_section_mapping
        self.syllabus = kb.syllabus
        self.topic_proficiency={'Motion, forces and energy': {'Physical quantities and measurement techniques': 0.566, 'Motion': 0.628, 'Mass and Weight': 0.544, 'Density': 0.962, 'Forces': 0.528, 'Momentum': 0.446, 'Energy, work and power ': 0.616, 'Pressure': 0.294}, 'Thermal physics': {'Kinetic particle model of matter ': 0.469, 'Thermal properties and temperature': 0.35, 'Transfer of thermal energy ': 0.354}, 'Waves': {'General properties of waves ': 0.936, 'Light ': 0.913, 'Electromagnetic spectrum': 0.051, 'Sound ': 0.889}, 'Electricity and magnetism': {'Simple magnetism and magnetic field ': 0.974, 'Electrical quantities ': 0.473, 'Electric Circuits': 0.541, 'Practical Electricity': 0.463, 'Electromagnetic effects ': 0.757, 'Uses of Oscilloscope': 0.551}, 'Nuclear physics': {'The nuclear model of the atom ': 0.449, 'Radioactivity ': 0.241}, 'Space physics': {'Earth and the Solar System ': 0.477, 'Stars and the Universe ': 0.233}}
        self.subtopic_proficiency = {'Forces': {'Balanced and unbalanced forces': 0.344, 'Friction': 0.43, 'Elastic deformation': 0.905, 'Circular motion': 0.201, 'Turning effect of forces': 0.492, 'Centre of gravity': 0.796}, 'Energy, work and power ': {'Energy ': 0.525, 'Work': 0.853, 'Energy resources': 0.871, 'Efficiency': 0.642, 'Power': 0.187}, 'Kinetic particle model of matter ': {'States of matter ': 0.208, 'Particle model ': 0.731}, 'Thermal properties and temperature': {'Thermal expansion of solids, liquids and gases ': 0.022, 'Specific heat capacity ': 0.538, 'Melting, boiling and evaporation ': 0.491}, 'Transfer of thermal energy ': {'Conduction ': 0.88, 'Convection ': 0.019, 'Radiation ': 0.464, 'Consequences of thermal energy transfer ': 0.052}, 'Light ': {'Reflection of light ': 0.915, 'Refraction of light ': 0.845, 'Thin lenses ': 0.908, 'Dispersion of light ': 0.985}, 'Electrical quantities ': {'Electrical charge ': 0.391, 'Electrical current ': 0.157, 'Electromotive force and potential difference ': 0.735, 'Resistance ': 0.611}, 'Electric Circuits': {'Circuit diagram and circuit components': 0.714, 'Series and parallel circuits': 0.665, 'Action and use of circuit components': 0.243}, 'Practical Electricity': {'Uses of electricity': 0.109, 'Electrical Safety': 0.818}, 'Electromagnetic effects ': {'Electromagnetic induction ': 0.856, 'The a.c. generator ': 0.956, 'Magnetic effect of a current ': 0.942, 'Forces on a current-carrying conductor ': 0.7, 'The d.c. motor ': 0.564, 'The transformer ': 0.527}, 'The nuclear model of the atom ': {'The atom ': 0.746, 'The nucleus ': 0.151}, 'Radioactivity ': {'Detection of radioactivity ': 0.246, 'The three types of emission ': 0.443, 'Radioactive decay ': 0.244, 'Fission and fusion ': 0.036, 'Half-life ': 0.013, 'Safety precautions ': 0.464}, 'Earth and the Solar System ': {'The earth ': 0.852, 'The solar system ': 0.103}, 'Stars and the Universe ': {'The sun as a star ': 0.358, 'Stars ': 0.221, 'The universe ': 0.12}}

        # print("-------Topic proficiency---------")
        # print(self.topic_proficiency)
        # print("------SUB - Topic proficiency---------")
        # print(self.subtopic_proficiency)

    # assigns proficiency for every topic and subtopic (0-1)
    def dummy_data_student_proficiency(self):
        global SIG_FIGURES
        self.topic_proficiency={}
        self.subtopic_proficiency={}
        self.topic_section_mapping={}

        # initializing topic proficiency and sub-topic proficiency
        for section, topics in self.syllabus.items():
            self.topic_proficiency[section]={}
            for topic, subtopics in topics.items():
                proficiency = random.random()
                self.topic_proficiency[section][topic] = round(proficiency,SIG_FIGURES)
                if (len(subtopics) != 0):
                    self.subtopic_proficiency[topic]={}
                    for subtopic in subtopics:
                        proficiency =random.random()
                        self.subtopic_proficiency[topic][subtopic] = round(proficiency,SIG_FIGURES)
        
        self.topic_proficiency=self.update_topic_proficiencies(self.topic_proficiency, self.subtopic_proficiency)
    
    # recalibrating topic proficiency for topics with sub-topics -- taking(avg)
    def update_topic_proficiencies(self, topic_proficiency, subtopic_proficiency):
        for topic, subtopics in subtopic_proficiency.items():
            subtopic_proficiency_sum=0
            for subtopic in subtopics:
                subtopic_proficiency_sum+= subtopic_proficiency[topic][subtopic]
            for section, topics in topic_proficiency.items():
                if topic in topics:
                    topic_proficiency[section][topic]=round(subtopic_proficiency_sum/len(subtopics),SIG_FIGURES)

        return topic_proficiency

    #normalizes topic and sub-topic proficiency
    def topic_probability(self,proficiency_dict):
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
      
    # randomly generates response for every question in the paper. 
    def generate_response(self,paper):
        self.response=[]
        options = ["A","B","C","D"]
        
        for i in range (len(paper)):
            random_option = random.choice(options)
            self.response.append(random_option)

        print("\n--------RESPONSE OF STUDENT-------")    
        print(self.response)
        return self.response

    # Generates new topic and subtopic proficiency based on student responses
    def Q_generate_new_proficiencies(self,response, paper):
        # response = [1,0,0,1,0]
        # paper={1: [("T1","None",1),("T2","None",1)],
        # 2:[("T2","None",1),("T3","None",1)],
        # 3:[("T1","None",1),("T3","None",1)],
        # 4:[("T1","None",1)],
        # 5:[("T3","None",1)]}

        student_ability={}
        for i in range (len(response)):
            qs_info=paper[i+1]
            for topic_info in qs_info:
                # print(topic_info)
                if (topic_info[0],topic_info[1]) not in student_ability:
                    student_ability[topic_info[0],topic_info[1]]=[0,0]
                    updated_topic_record=self.Q_update_topic_record(student_ability[(topic_info[0],topic_info[1])],response[i])
                    student_ability[(topic_info[0],topic_info[1])]=updated_topic_record
                else:
                    updated_topic_record=self.Q_update_topic_record(student_ability[(topic_info[0],topic_info[1])],response[i])
                    student_ability[(topic_info[0],topic_info[1])]=updated_topic_record
        
        print("\n-------- STUDENT INFO FROM RESPONSES-------")
        print(student_ability)
        return(student_ability)

    #helper function to Q_generate_new_proficiencies
    def Q_update_topic_record(self,record, response):
        num_correct_attempts,num_total_attempts=record[0], record[1]
        if response == 1:
            num_correct_attempts+=1
        num_total_attempts+=1

        record[0], record[1] = num_correct_attempts,num_total_attempts

        return record

    #Updates student topic and sub-topic proficiency
    def Q_update_student_proficiency(self, student_ability):
        for topic_subtopic, details in student_ability.items():
            num_correct_attempts,num_total_attempts=details[0],details[1]
            topic_proficiency= num_correct_attempts/num_total_attempts
            if topic_subtopic[1]== "None":
                section=self.topic_section_mapping[topic_subtopic[0]]
                self.topic_proficiency[section][topic_subtopic[0]]=  ((topic_proficiency*num_total_attempts) +  (self.topic_proficiency[section][topic_subtopic[0]]*CATSIM_WEIGHTAGE))/(CATSIM_WEIGHTAGE+num_total_attempts)
            else:
                self.subtopic_proficiency[topic_subtopic[0]][topic_subtopic[1]]=  ((topic_proficiency*num_total_attempts) +  (self.subtopic_proficiency[topic_subtopic[0]][topic_subtopic[1]]*CATSIM_WEIGHTAGE))/(CATSIM_WEIGHTAGE+num_total_attempts)

        # print("\n-----------PRE-UPDATE TOPIC PROFICIENCY----------")
        # print(self.topic_proficiency)
        self.topic_proficiency=self.update_topic_proficiencies(self.topic_proficiency, self.subtopic_proficiency)
        print("\n-----------POST-UPDATE TOPIC PROFICIENCY----------")
        print(self.topic_proficiency)
        # print(self.subtopic_proficiency)
            # print(topic_subtopic)
            # print(topic_proficiency)
            # topic_proficiency*num_total_attempts + self.topic_proficiency[tu]




        # R= [1,0,0,1,0]
        # Q = [[1,1,0],
        #     [0,1,1],
        #     [1,0,1],
        #     [1,0,0],
        #     [0,0,1],
        #     ]

        # student_info = []
        # for i in range(len(R)):
        #     temp=[]
        #     for j in range(len(Q[i])):
        #         if Q[i][j]==0:
        #             result= "-"
        #         elif (R[i]==0 and Q[i][j]==0):
        #             result= "-"
        #         else:
        #             result= R[i]*Q[i][j]
        #         temp.append(result)
        #     student_info.append(temp)

        
        # print("-------STUDENT INFORMATION")
        # print(student_info)

        # column_sums = []
        # num_entries = []

        # for column in zip(*student_info):
        #     filtered_column = [value for value in column if value != "-"]
        #     column_sums.append(sum(filtered_column))
        #     num_entries.append(len(filtered_column))

        # topic_proficiency=[]
        # for i in range(len(column_sums)):
        #     topic_proficiency.append(column_sums[i]/num_entries[i])

        # print(column_sums)
        # print("Total entries per column:", num_entries)
        # print(topic_proficiency)

    

            

      


# my_student = StudentModel()
# my_student.dummy_data_student_proficiency()
# print("Topic proficiency")
# print(my_student.topic_proficiency)
# print("Sub topic proficiency")
# print(my_student.subtopic_proficiency)

# normalized_topic_proficiency=my_student.topic_probability(my_student.topic_proficiency)
# print("-------Normalized Topic proficiency---------")
# print(normalized_topic_proficiency)
# normalized_subtopic_proficiency=my_student.topic_probability(my_student.subtopic_proficiency)
# print("\n-------Normalized SUBTopic proficiency---------")
# print(normalized_subtopic_proficiency)



