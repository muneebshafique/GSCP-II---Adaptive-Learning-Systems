from student_model import StudentModel
from knowledge_base import KnowledgeBase
from evaluation import Evaluation
from paper_generator import PaperGenerator


class MainProgram:
    def __init__(self):
        filename ="../Database/Olevels Physics Data (2023-2025).csv"
        self.student_model = StudentModel()
        self.knowledge_base = KnowledgeBase()

        self.knowledge_base.initialize_syllabus(filename)
        self.paper_generator = PaperGenerator(filename,self.knowledge_base, self.student_model)

        self.evaluate = Evaluation()

    def run(self):
        #generates and prints paper
        paper=self.paper_generator.generate_paper()
        self.paper_generator.print_paper(paper)

        #student responds to paper and paper is evalutated
        response=self.student_model.generate_response(paper)
        checked_paper=self.evaluate.check_paper(response)
        
        #based on evalutation student's topic and sub-topic proficiencies are updated. 
        current_student_ability=self.student_model.Q_generate_new_proficiencies(checked_paper,paper)
        # self.student_model.Q_update_student_proficiency(current_student_ability,self.knowledge_base.topic_section_mapping)

        # Option number 2 based on Elo rating system.
        self.student_model.Elo_update_student_proficiency(paper, checked_paper, self.knowledge_base.topic_section_mapping)

       
if __name__ == "__main__":
    program = MainProgram()
    program.run()
