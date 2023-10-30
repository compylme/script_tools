import json
postcode_list = []

with open('../data/UK_postcode_districts.json') as f:
    postcodes = json.load(f)

for each in postcodes["features"]:
   postcode_list.append(each['properties']['name']) 

with open('postcode_list.json', 'w') as f:
    json.dump(postcode_list, f) 