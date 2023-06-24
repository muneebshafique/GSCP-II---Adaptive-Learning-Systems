

class PaperGenerator:
    def __init__(self) -> None:
        # self.num_of_sections = 6
        # self.num_of_topics = 25
        # self.num_of_subtopics = 52
        # self.syllabus_info = {"Motion, forces and energy": }
        pass
    
    def section_weigtage(self):
        total = self.num_of_topics+ (self.num_of_subtopics/2)
        

# Correct way
paper_generator = PaperGenerator()
paper_generator.section_weigtage()
