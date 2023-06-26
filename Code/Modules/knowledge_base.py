

TOPIC_WEIGHTAGE = 1
SUBTOPIC_WEIGHTAGE = 0.5
NUM_QUESTIONS=40

class KnowledgeBase:
    def __init__(self) -> None:
        self.syllabus= {
            'Motion, forces and energy':{
                'Physical quantities and measurement techniques': [],
                'Motion': [],
                'Mass and Weight': [],
                'Density': [],
                'Forces': ['Balanced and unbalanced forces', 'Friction', 'Elastic deformation', 'Circular motion','Turning effect of forces','Centre of gravity'],
                'Momentum':[],
                'Energy, work and power': ['Energy', 'Work', 'Energy resources', 'Efficiency','Power'],
                'Pressure':[]
                },
            'Thermal physics':{
                'Kinetic particle model of matter': ['States of matter', 'Particle model'],
                'Thermal properties and temperatuare': ['Thermal expansion of solids, liquids and gases', 'Specific heat capacity','Melting, boiling and evaporation'],
                'Transfer of thermal energy': ['Conduction', 'Convection', 'Radiation', 'Consequences of thermal energy transfer']
                },
            'Waves':{
                'General properties of waves':[],
                'Light': ['Reflection of light', 'Refraction of light','Thin lenses', 'Dispersion of light'],
                'Electromagnetic spectrum':[],
                'Sound':[]
                },
            'Electricity and magnetism':{
                'Simple magnetism and magnetic field': [],
                'Electrical quantities':['Electrical charge', 'Electrical current', 'Electromotive force and potential difference', 'Resistance'],
                'Electric Circuits':['Circuit diagram and circuit components', 'Series and parallel circuits','Action and use of circuit components'],
                'Practical Electricity':['Uses of electricity','Electrical Safety'],
                'Electromagnetic effects ':['Electromagnetic induction', 'The a.c. generator', 'Magnetic effect of a current','Forces on a current-carrying conductor', 'The d.c. motor', 'The transformer'],
                'Uses of Oscilloscope':[],
            },
            'Nuclear physics':{
                'The nuclear model of the atom':['The atom','The nucleus'],
                'Radioactivity':['Detection of radioactivity', 'The three types of emission', 'Radioactive decay','Fission and fusion','Half-life','Safety precautions']
            },
            'Space physics':{
                'Earth and the Solar System':['The earth','The solar system'],
                'Stars and the Universe':['The sun as a star', 'Stars', 'The universe']
            }
        }

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

        self.section_weightage(num_of_topics,num_of_subtopics,sectionwise_topic_subtopic_totals)

    # defines num of qs to be picked from each section. 
    def section_weightage(self,num_topics,num_subtopics,sectionwise_topic_subtopic_totals):
        global TOPIC_WEIGHTAGE, SUBTOPIC_WEIGHTAGE,NUM_QUESTIONS

        total = (num_topics*TOPIC_WEIGHTAGE)+(num_subtopics*SUBTOPIC_WEIGHTAGE)
        section_weightage={}

        i=0
        for section, topics in self.syllabus.items():
            weight=((sectionwise_topic_subtopic_totals[i][0]*TOPIC_WEIGHTAGE)+(sectionwise_topic_subtopic_totals[i][1]*SUBTOPIC_WEIGHTAGE))/total
            section_weightage[section]= round(weight*NUM_QUESTIONS)
            i+=1
        
        print(section_weightage)

kb=KnowledgeBase()
kb.stats_from_syllabus()