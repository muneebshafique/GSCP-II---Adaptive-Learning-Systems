import pandas as pd

TOPIC_WEIGHTAGE = 1
SUBTOPIC_WEIGHTAGE = 0.5
NUM_QUESTIONS=40

class KnowledgeBase:
    def __init__(self) -> None:
        self.section_weightage={}
        self.syllabus={}
        

    def initialize_syllabus(self,filename):
        df = pd.read_csv(filename)
        for index, row in df.iterrows():
            section = row['Section']
            topic = row['Topic']
            sub_topic = row['Sub Topic']
            
            # Check if the section already exists in the dictionary
            if section in self.syllabus:
                # Check if the topic exists within the section
                if topic in self.syllabus[section]:
                    # Append the sub_topic to the existing topic
                    if sub_topic and not pd.isnull(sub_topic):
                        self.syllabus[section][topic].append(sub_topic)
                else:
                    # Add the new topic and sub_topic
                    if sub_topic and not pd.isnull(sub_topic):
                        self.syllabus[section][topic] = [sub_topic]
                    else:
                        self.syllabus[section][topic] = []
            else:
                # Create a new section with the topic and sub_topic
                if sub_topic and not pd.isnull(sub_topic):
                    self.syllabus[section] = {topic: [sub_topic]}
                else:
                    self.syllabus[section] = {topic: []}



        # print(self.syllabus)
        self.stats_from_syllabus()
    #calculates num of (section, topics and subtopics)
    def stats_from_syllabus(self):
        num_of_sections=len(self.syllabus)
        num_of_topics=0
        num_of_subtopics=0

        sectionwise_topic_subtopic_totals=[]
        for section,topics in self.syllabus.items():
            temp_topics=0
            temp_subtopics=0
            for topic in topics:
                num_of_topics+=1
                temp_topics+=1     
                for subtopic in self.syllabus[section][topic]:
                    num_of_subtopics+=1
                    temp_subtopics+=1
            sectionwise_topic_subtopic_totals.append([temp_topics,temp_subtopics])

        # print("Number of sections",num_of_sections)
        # print("Number of topics",num_of_topics)
        # print("Number of subtopics", num_of_subtopics)
        # print("section wise totals", sectionwise_topic_subtopic_totals)

        self.generate_section_weightage(num_of_topics,num_of_subtopics,sectionwise_topic_subtopic_totals)

    # defines num of qs to be picked from each section. 
    def generate_section_weightage(self,num_topics,num_subtopics,sectionwise_topic_subtopic_totals):
        global TOPIC_WEIGHTAGE, SUBTOPIC_WEIGHTAGE,NUM_QUESTIONS

        total = (num_topics*TOPIC_WEIGHTAGE)+(num_subtopics*SUBTOPIC_WEIGHTAGE)
        
        i=0
        for section, topics in self.syllabus.items():
            weight=((sectionwise_topic_subtopic_totals[i][0]*TOPIC_WEIGHTAGE)+(sectionwise_topic_subtopic_totals[i][1]*SUBTOPIC_WEIGHTAGE))/total
            self.section_weightage[section]= round(weight*NUM_QUESTIONS)
            i+=1
        
        # print(self.section_weightage)

filename ="../Database/Olevels Physics Data (2023-2025).csv"
kb=KnowledgeBase()
kb.initialize_syllabus(filename)
