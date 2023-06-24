import random

generated_strings = set()  # Set to store generated strings

def generate_random_string():
    session = random.choice(['m/j', 'o/n'])
    year = random.randint(2005, 2022)
    paper_number = random.choice([11, 12])
    question_number = random.randint(1, 40)
    
    random_string = f"{session}/{year}/{paper_number}/Q{question_number}"
    
    if random_string in generated_strings:
        return generate_random_string()  # Generate again if string is already generated
    else:
        generated_strings.add(random_string)
        return random_string

# Generate 10 unique random strings
count=0
for _ in range(1600):
    random_string = generate_random_string()
    print(random_string)
    count+=1
    if (count %10 ==0):
        print("----------------------",count//10,"----------------")
    
