from student_model import StudentModel
from knowledge_base import KnowledgeBase
from evaluation import Evaluation
from paper_generator import PaperGenerator


class MainProgram:
    def __init__(self):
        filename ="../Database/Olevels Physics Data (2023-2025).csv"
        student_model = StudentModel()
        knowledge_base = KnowledgeBase()
        paper_generator = PaperGenerator(filename)
        evaluation = Evaluation()


    def run(self):
        print("hello")

       
if __name__ == "__main__":
    program = MainProgram()
    program.run()