person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = [51]
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

#print(person)

#print(type(person['children']))

#print(person['children'][1])

#print(person['pets']['cat'])

for rec in person['children']:
    print(rec)

for rec in (person['pets']):
    print(person['pets'][rec])
    
for rec in (person['pets'].values()):
    print(rec)
for rec in person['age']:
    print (rec+1)