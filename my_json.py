import json

people_string = '''
{
    "people" : [
        {
            "name" : "Arc",
            "phone" : "9334422880",
            "emails" : ["arc@gmail.com", "arcsana@gmail.com"],
            "has_license" : false
        },
        {
            "name" : "Kalp",
            "phone" : "9123456780",
            "emails" : null ,
            "has_license" : true
        }
    ]
}
'''

data = json.loads(people_string)

#print(data)

print(type(data))# now see we get 'dict' as a type

# people is an array and it is equal to list as per json
# So we can access the 'people' as list in python
# so now the list is access as dictionary 

print(type('people')) # array (normally it is array)

print(type(data['people'])) # list(as per json)

# To list out the individual list of person's in people

for person in data['people']:
    print(person['name'])



# Removing phone numbers

for person in data['people']:
    del person['phone']

new_string = json.dumps(data)

print(new_string)