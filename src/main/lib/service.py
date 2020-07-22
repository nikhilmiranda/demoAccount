import json

# Opening JSON file
f = open('./data/apparelConfig.json',)

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for i in data['mapping']:
    print(i)

# Closing file
f.close()
