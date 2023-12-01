#convert .pkl files to json

import pickle
import json

# Load the pkl file
with open('words.pkl', 'rb') as f:
    data = pickle.load(f)

# Convert the loaded object to JSON
json_data = json.dumps(data)

# Write the JSON data to a file
with open('words_20231130.json', 'w') as f:
    f.write(json_data)