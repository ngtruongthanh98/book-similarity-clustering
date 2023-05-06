import os
import json

# Create an empty dictionary to store the combined data
combined_data = {}

# Set the directory where the JSON files are stored
directory = 'D:/Documents/Master/Mathematics/Assignment/BTL/book-similarity-clustering/graph/'

# Loop through all the files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.json'):
        # Open the file and load the JSON data
        with open(os.path.join(directory, filename)) as file:
            data = json.load(file)
            for key, value in data.items():
                keys = key.split('-')
                inverted_key = keys[1] + '-' + keys[0]
                if inverted_key in combined_data:
                    # Add the value to the existing key
                    combined_data[inverted_key] += value
                elif key in combined_data:
                    # Add the value to the existing key
                    combined_data[key] += value
                else:
                    # Add the new key-value pair
                    combined_data[key] = value

# Print the combined data
# Write the results to a JSON file
with open(f'preprocessed.json', 'w') as f:
    json.dump(combined_data, f)

print('Results written to book_pairs.json')
