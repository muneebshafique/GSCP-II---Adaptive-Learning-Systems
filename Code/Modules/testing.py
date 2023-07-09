# class BKT:
#     def __init__(self, p_trans, p_guess, p_slip):
#         self.p_trans = p_trans
#         self.p_guess = p_guess
#         self.p_slip = p_slip
#         self.p_know = None  # Initial knowledge state

#     def update(self, response):
#         if self.p_know is None:
#             self.p_know = 0.5  # Assuming equal probability for initial knowledge

#         # Update knowledge state based on the binary response
#         p_not_know = 1 - self.p_know
#         p_guess_correct = self.p_guess * p_not_know
#         p_slip_incorrect = self.p_slip * self.p_know
#         p_correct = p_guess_correct + (1 - p_slip_incorrect)

#         if response == 1:  # Correct response
#             self.p_know = (p_correct * self.p_know) / ((p_correct * self.p_know) + ((1 - self.p_slip) * p_not_know))
#         else:  # Incorrect response
#             self.p_know = (self.p_know * (1 - self.p_trans)) / ((self.p_know * (1 - self.p_trans)) + ((1 - self.p_guess) * p_not_know))

#     def predict(self):
#         return self.p_know

# # Example usage
# bkt = BKT(p_trans=0.2, p_guess=0.1, p_slip=0.1)

# # Simulating student responses
# responses = [1, 1, 0, 1]  # Assuming 1 represents a correct response and 0 represents an incorrect response

# for i, response in enumerate(responses):
#     bkt.update(response)
#     print(f"Knowledge state {i+1}: {bkt.predict()}")


nested_list = [[1, 1, '-'], ['-', 0, 0], [0, '-', 0], [1, '-', '-'], ['-', '-', 0]]
column_sums = []
num_entries = []

for column in zip(*nested_list):
    filtered_column = [value for value in column if value != "-"]
    column_sums.append(sum(filtered_column))
    num_entries.append(len(filtered_column))

Kcs=[]
for i in range(len(column_sums)):
    Kcs.append(column_sums[i]/num_entries[i])

print(column_sums)
print("Total entries (excluding 2) per column:", num_entries)
print(Kcs)