# this function generates an item bank, in case the user cannot provide one
from catsim.cat import generate_item_bank
# simulation package contains the Simulator and all abstract classes
from catsim.simulation import *
# initialization package contains different initial proficiency estimation strategies
from catsim.initialization import *
# selection package contains different item selection strategies
from catsim.selection import *
# estimation package contains different proficiency estimation methods
from catsim.estimation import *
# stopping package contains different stopping criteria for the CAT
from catsim.stopping import *
import catsim.plot as catplot
from catsim.irt import icc

import random
import matplotlib.pyplot as plt


class Catsim:
    def __init__(self) -> None:
        self.administered_items = []
        self.responses=[]
        self.bank_size = 5000
        self.initializer = FixedPointInitializer(0)
        self.selector = UrrySelector()
        # self.selector =  MaxInfoSelector()
        self.estimator = NumericalSearchEstimator()
        self.stopper = MinErrorStopper(.5)

    
    def generate_question_bank(self):
        self.items = generate_item_bank(self.bank_size,itemtype='1PL')

        ## visualize item
        # catplot.gen3d_dataset_scatter(self.items)
        # a, b, c, d = self.items[0]
        # catplot.item_curve(a,b,c,d)

    def initialize_examinee_proficiency(self):
        self.est_theta = self.initializer.initialize()
        print('Examinee initial proficiency:', self.est_theta)

    def ask_initial_question_receive_response(self):
        self.administered_items.append(1435)
        self.responses.append(True)
    
    def update_proficiency(self):
        self.est_theta = self.estimator.estimate(items=self.items, administered_items=self.administered_items, response_vector=self.responses, est_theta=self.est_theta)
        print('Estimated proficiency, given answered items:', self.est_theta)

    def is_test_end(self):
        _stop = self.stopper.stop(administered_items=self.items[self.administered_items], theta=self.est_theta)
        print('Should the test be stopped:', _stop)
        return _stop

    def select_next_item(self):
        item_index = self.selector.select(items=self.items, administered_items=self.administered_items, est_theta=self.est_theta)
        print('Next item to be administered:', item_index," difficulty", self.items[item_index][1])
        return item_index

    def simulate_response(self, item_index):
        true_theta = 0.8
        a, b, c, d = self.items[item_index]
        prob = icc(true_theta, a, b, c, d)
        correct = prob > random.uniform(0, 1)

        print('Probability to correctly answer item:', prob)
        print('Did the user answer the selected item correctly?', correct)

        return correct

    def update_items_and_responses(self,item_index, response):
        self.administered_items.append(item_index)
        self.responses.append(response)


# -----------------------------

cat=Catsim()
cat.generate_question_bank()
cat.initialize_examinee_proficiency()
cat.ask_initial_question_receive_response()


for i in range(50):
    print("\n--------ITERATION:",i,"--------")
    cat.update_proficiency()
    test_end=cat.is_test_end()
    if test_end == False:
        item_index=cat.select_next_item()
        response=cat.simulate_response(item_index)
        cat.update_items_and_responses(item_index, response)
    else:
        print("----- TEST ENDED------")
        print("FINAL PROFICIENCY",cat.est_theta)
        break

        



