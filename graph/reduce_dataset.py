import json
import random

# Load the JSON data into a Python dictionary
with open('preprocessed_reduce_4.json', 'r') as f:
    data = json.load(f)

# Get half of the keys randomly
keys_to_drop = random.sample(list(data.keys()), k=len(data) // 3)

# Remove the corresponding key-value pairs from the dictionary
for key in keys_to_drop:
    del data[key]

# Write the modified data back to the JSON file
with open('preprocessed_reduce_4.json', 'w') as f:
    json.dump(data, f)
