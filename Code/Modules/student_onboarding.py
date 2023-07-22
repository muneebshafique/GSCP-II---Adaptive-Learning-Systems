from catsim.cat import generate_item_bank
from catsim.simulation import *
from catsim.initialization import *
from catsim.selection import *
from catsim.estimation import *
from catsim.stopping import *

import random
import matplotlib.pyplot as plt
from evaluation import *


class Catsim:
    def __init__(self) -> None:
        self.administered_items = [150]
        self.responses = [True]
        self.bank_size = 500
        self.initializer = FixedPointInitializer(0)
        self.selector = UrrySelector()
        self.estimator = NumericalSearchEstimator()
        self.stopper = MinErrorStopper(.5)
        # Assuming the student started off with 0 knowledge.
        self.est_theta = 0
        self.eval = Evaluation()

    def generate_question_bank(self):
        # 1PL (One-Parameter Logistic Model): Assumes that the probability of a correct response depends only on the item's difficulty.
        self.items = generate_item_bank(self.bank_size, itemtype='1PL')
        # Each row of the array will represent an item, and the four columns will contain the numerical values of
        # the item parameters (discrimination, difficulty, pseudo-guessing, and upper asymptote)

    def update_proficiency(self):
        self.est_theta = self.estimator.estimate(
            items=self.items, administered_items=self.administered_items, response_vector=self.responses, est_theta=self.est_theta)

    def is_test_end(self):
        _stop = self.stopper.stop(
            administered_items=self.items[self.administered_items], theta=self.est_theta)
        return _stop

    def select_next_item(self):
        item_index = self.selector.select(
            items=self.items, administered_items=self.administered_items, est_theta=self.est_theta)
        return item_index

    def simulate_response(self, item_index, topic, subtopic):
        # b is the difficulty.
        a, b, c, d = self.items[item_index]
        # Easy qs.
        if b >= 1.3333333333333333:
            difficulty = 1
        # Medium level qs.
        elif b >= -1.3333333333333333:
            difficulty = 2
        # Hard qs.
        elif b >= -4:
            difficulty = 3

        # Fetching correct answer from data base.
        correct_answer = self.eval.get_answer(topic, subtopic, difficulty)
        student_answer = random.choice(['A', 'B', 'C', 'D'])
        if student_answer == correct_answer:
            correct = True
        else:
            correct = False
        # print(correct_answer, student_answer)
        return correct

    def update_items_and_responses(self, item_index, response):
        self.administered_items.append(item_index)
        self.responses.append(response)


def get_proficiency(topic, subtopic):
    cat = Catsim()
    cat.generate_question_bank()
    for i in range(50):
        cat.update_proficiency()
        test_end = cat.is_test_end()
        if test_end == False:
            item_index = cat.select_next_item()
            response = cat.simulate_response(item_index, topic, subtopic)
            cat.update_items_and_responses(item_index, response)
        else:
            print("Test ended for", topic, "in", i, "iterations.")
            # print("FINAL PROFICIENCY", cat.est_theta)
            break
    return cat.est_theta


# print(get_proficiency('Physical quantities and measurement techniques', 'None'))
