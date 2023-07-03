import pandas as pd

# Read the CSV file
df = pd.read_csv("../Database/Olevels Physics Data (2023-2025).csv")

# Create an empty dictionary
data_dict = {}

# Iterate over the DataFrame rows
for index, row in df.iterrows():
    section = row['Section']
    topic = row['Topic']
    sub_topic = row['Sub Topic']
    
    # Check if the section already exists in the dictionary
    if section in data_dict:
        # Check if the topic exists within the section
        if topic in data_dict[section]:
            # Append the sub_topic to the existing topic
            if sub_topic and not pd.isnull(sub_topic):
                data_dict[section][topic].append(sub_topic)
        else:
            # Add the new topic and sub_topic
            if sub_topic and not pd.isnull(sub_topic):
                data_dict[section][topic] = [sub_topic]
            else:
                data_dict[section][topic] = []
    else:
        # Create a new section with the topic and sub_topic
        if sub_topic and not pd.isnull(sub_topic):
            data_dict[section] = {topic: [sub_topic]}
        else:
            data_dict[section] = {topic: []}


# Print the resulting dictionary
print(data_dict)