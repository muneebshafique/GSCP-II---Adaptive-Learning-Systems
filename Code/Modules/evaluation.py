
import random

# Used to asses the student's response
class Evaluation():
    def __init__(self) -> None:
        pass

    def check_paper(self,response):
        checked_paper=[]
        options = [0,1]
        for option in response:
            random_option = random.choice(options)
            checked_paper.append(random_option)

        print("\n--------CHECKED RESPONSE-------")
        print(checked_paper)
        return checked_paper

