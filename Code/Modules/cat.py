# this function generates an item bank, in case the user cannot provide one
from catsim.cat import generate_item_bank
# # simulation package contains the Simulator and all abstract classes
# from catsim.simulation import *
# # initialization package contains different initial proficiency estimation strategies
# from catsim.initialization import *
# # selection package contains different item selection strategies
# from catsim.selection import *
# # estimation package contains different proficiency estimation methods
# from catsim.estimation import *
# # stopping package contains different stopping criteria for the CAT
# from catsim.stopping import *
# import catsim.plot as catplot
# from catsim.irt import icc

# import random

import matplotlib.pyplot as plt

bank_size = 5000
items = generate_item_bank(bank_size,itemtype='3PL')
# catplot.gen3d_dataset_scatter(items)

# catplot.param_dist(items, figsize=(9,7))