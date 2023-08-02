import random
import copy
import knowledge_base
import math
from student_initial_testing import Student_onboarding

MAX_PROFICIENCY = 10
SIG_FIGURES=3
CATSIM_WEIGHTAGE=10


#Stores topic,subtopic proficiency of student & questions attempted by student
class StudentModel:
    def __init__(self, topic_proficiency, subtopic_proficiency) -> None:
        # so=Student_onboarding()
        self.topic_proficiency=topic_proficiency
        self.subtopic_proficiency = subtopic_proficiency
        self.options = 4
        self.K = 0.04

    # assigns proficiency for every topic and subtopic (0-1)
    def dummy_data_student_proficiency(self):
        global SIG_FIGURES
        self.topic_proficiency={}
        self.subtopic_proficiency={}

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
         
         # recalibrating topic proficiency for topics with sub-topics -- taking(avg)
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
    def Q_update_student_proficiency(self, response,paper, topic_section_mapping):
        student_ability=self.Q_generate_new_proficiencies(response, paper)
        for topic_subtopic, details in student_ability.items():
            num_correct_attempts,num_total_attempts=details[0],details[1]
            topic_proficiency= num_correct_attempts/num_total_attempts
            if topic_subtopic[1]== "None":
                section=topic_section_mapping[topic_subtopic[0]]
                self.topic_proficiency[section][topic_subtopic[0]]=  ((topic_proficiency*num_total_attempts) +  (self.topic_proficiency[section][topic_subtopic[0]]*CATSIM_WEIGHTAGE))/(CATSIM_WEIGHTAGE+num_total_attempts)
            else:
                self.subtopic_proficiency[topic_subtopic[0]][topic_subtopic[1]]=  ((topic_proficiency*num_total_attempts) +  (self.subtopic_proficiency[topic_subtopic[0]][topic_subtopic[1]]*CATSIM_WEIGHTAGE))/(CATSIM_WEIGHTAGE+num_total_attempts)

       
        self.topic_proficiency=self.update_topic_proficiencies(self.topic_proficiency, self.subtopic_proficiency)
        print("\n-----------POST-UPDATE TOPIC PROFICIENCY----------")
        print(self.topic_proficiency)
        print("\n-----------POST-UPDATE SUB TOPIC PROFICIENCY----------")
        print(self.subtopic_proficiency)

        

    def Elo_update_student_proficiency(self, paper, response, topic_section_mapping):
        self.difficulty = {1: 0.33, 2: 0.67, 3: 0.99}
        for i in range(len(response)):
            qs_info = paper[i+1]
            for topic_info in qs_info:
                topic, sub_topic, difficulty = topic_info[0], topic_info[1], topic_info[2]
                difficulty_in_dec = self.difficulty[difficulty]
                if sub_topic == 'None':
                    section = topic_section_mapping[topic]
                    skill = self.topic_proficiency[section][topic]
                    student_attempt = response[i]
                    correct_prob = self.Logistic_Function_2(
                        difficulty_in_dec, skill)
                    updated_skill = self.change_in_skill(
                        student_attempt, correct_prob, skill)
                    self.topic_proficiency[section][topic] = updated_skill
                else:
                    skill = self.subtopic_proficiency[topic][sub_topic]
                    student_attempt = response[i]
                    correct_prob = self.Logistic_Function_2(
                        difficulty_in_dec, skill)
                    updated_skill = self.change_in_skill(
                        student_attempt, correct_prob, skill)
                    self.subtopic_proficiency[topic][sub_topic] = updated_skill
        self.topic_proficiency = self.update_topic_proficiencies(
            self.topic_proficiency, self.subtopic_proficiency)
        print("\n-----------POST-UPDATE ELO TOPIC PROFICIENCY----------")
        print(self.topic_proficiency)

    def Logistic_Function_2(self, difficulty, skill):
        # For question with k options the probability of a correct answer becomes:
        # P(correctsi = 1) = 1/k + (1 − 1/k)/(1 + e−(θs−di))
        reciprocal = 1/self.options
        denominator = 1+math.exp(-skill + difficulty)
        correct_probability = reciprocal + ((1-reciprocal)/denominator)
        return correct_probability

    def change_in_skill(self, student_attempt, correct_prob, skill):
        estimate = student_attempt - correct_prob
        skill = skill + self.K*(estimate)
        return skill
      


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



