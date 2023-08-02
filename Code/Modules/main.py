from student_model import StudentModel
from knowledge_base import KnowledgeBase
from evaluation import Evaluation
from paper_generator import PaperGenerator
from student_initial_testing import Student_onboarding


class MainProgram:
    def __init__(self):
        filename ="../Database/Olevels Physics Data (2023-2025).csv"
        self.knowledge_base = KnowledgeBase()
        self.knowledge_base.initialize_syllabus(filename)

        self.student_initial = Student_onboarding(self.knowledge_base.syllabus)
        self.student_initial.generate_initial_prof()
        self.student_model = StudentModel(self.student_initial.topic_proficiency,self.student_initial.subtopic_proficiency)
        
        self.paper_generator = PaperGenerator(filename,self.knowledge_base, self.student_model)

        self.evaluate = Evaluation()

    def run(self):
        
        

        #generates and prints paper and its information
        paper,paper_info=self.paper_generator.generate_paper()
        self.paper_generator.print_paper(paper)
        self.paper_generator.print_paper_info(paper_info)

        #student responds to paper and paper is evalutated
        response = self.student_model.generate_response(paper_info)
        checked_paper = self.evaluate.check_paper(response, paper_info)
        
        #based on evalutation student's topic and sub-topic proficiencies are updated.
        #   (Q_matrix)
        self.student_model.Q_update_student_proficiency(checked_paper,paper_info,self.knowledge_base.topic_section_mapping)
        #   Elo rating system.
        # self.student_model.Elo_update_student_proficiency(paper, checked_paper, self.knowledge_base.topic_section_mapping)

       
if __name__ == "__main__":
    program = MainProgram()
    program.run()
