from student_model import StudentModel
from knowledge_base import KnowledgeBase
from evaluation import Evaluation
from paper_generator import PaperGenerator
import random


class Good_Simulated_Student:
    def __init__(self):
        # change your path here.
        # filename = "C:/Users/LAIBA/Downloads/GSCP-II---Adaptive-Learning-Systems-main (1)/GSCP-II---Adaptive-Learning-Systems-main/Code/Database/Olevels Physics Data (2023-2025).csv"
        filename ="../Database/Olevels Physics Data (2023-2025).csv"
        self.student_model = StudentModel()
        self.knowledge_base = KnowledgeBase()

        self.knowledge_base.initialize_syllabus(filename)
        self.paper_generator = PaperGenerator(
            filename, self.knowledge_base, self.student_model)

        self.evaluate = Evaluation()

    def generate_response(self, paper):
        response = []
        count = 0
        for qs in paper:
            qs_detail = paper[qs][0]
            topic_name, sub_topic_name, difficulty = qs_detail[0], qs_detail[1], qs_detail[2]
            correct_answer = self.evaluate.get_answer(
                topic_name, sub_topic_name, difficulty)
            response.append(correct_answer)
        return response

    def run(self):
        paper = self.paper_generator.generate_paper()
        self.paper_generator.print_paper(paper)

        response = self.generate_response(paper)
        checked_paper = self.evaluate.check_paper(response, paper)

        # based on evalutation student's topic and sub-topic proficiencies are updated.
        current_student_ability = self.student_model.Q_generate_new_proficiencies(
            checked_paper, paper)
        # self.student_model.Q_update_student_proficiency(
        #     current_student_ability, self.knowledge_base.topic_section_mapping)
        self.student_model.Elo_update_student_proficiency(
            paper, checked_paper, self.knowledge_base.topic_section_mapping)

# Generate a paper in which the student performs correctly:

program = Good_Simulated_Student()
program.run()


class Bad_Simulated_Student:
    def __init__(self):
        # change your path here.
        filename = "C:/Users/LAIBA/Downloads/GSCP-II---Adaptive-Learning-Systems-main (1)/GSCP-II---Adaptive-Learning-Systems-main/Code/Database/Olevels Physics Data (2023-2025).csv"
        self.student_model = StudentModel()
        self.knowledge_base = KnowledgeBase()

        self.knowledge_base.initialize_syllabus(filename)
        self.paper_generator = PaperGenerator(
            filename, self.knowledge_base, self.student_model)

        self.evaluate = Evaluation()

    def generate_response(self, paper):
        response = []
        count = 0
        for qs in paper:
            qs_detail = paper[qs][0]
            topic_name, sub_topic_name, difficulty = qs_detail[0], qs_detail[1], qs_detail[2]
            correct_answer = self.evaluate.get_answer(
                topic_name, sub_topic_name, difficulty)
            options = ["A", "B", "C", "D"]
            options_without_correct = [
                option for option in options if option != correct_answer]
            random_answer = random.choice(options_without_correct)
            response.append(random_answer)
        return response

    def run(self):
        paper = self.paper_generator.generate_paper()
        self.paper_generator.print_paper(paper)

        response = self.generate_response(paper)
        checked_paper = self.evaluate.check_paper(response, paper)

        # based on evalutation student's topic and sub-topic proficiencies are updated.
        current_student_ability = self.student_model.Q_generate_new_proficiencies(
            checked_paper, paper)
        # self.student_model.Q_update_student_proficiency(
        #     current_student_ability, self.knowledge_base.topic_section_mapping)
        self.student_model.Elo_update_student_proficiency(
            paper, checked_paper, self.knowledge_base.topic_section_mapping)


# Generate a paper in which the student performs poorly:

# program = Bad_Simulated_Student()
# program.run()
