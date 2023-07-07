import json

data = json.load(open("states.json"))
print(data)

# for getting states alone
for i in data['states']:
    print(i)

print("*************************")

# for getting name and abbrevation
for i in data['states']:
    print(i['name'], i['abbreviation'])


# now deleting the 'area_codes' and dump a create a new json file
# inside that new file, dump this data again

for i in data['states']:
    del i['area_codes']

data = json.load(open("new_states.json"), 'w')
data = json.dumps(data)
