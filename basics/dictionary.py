# kinda js object -> Not allow duplicated indexes

capitals = {'France': 'Paris',
            'Spain': 'Madrid',
            'United Kingdom': 'London',
            'India': 'New Delhi'}

capitals.update({'United States': 'Washington, D.C.'})
capitals.pop('India')

# print(capitals)
# print(capitals['Spain'])
# print(capitals.get('Spain'))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())

for key,value in capitals.items():
    print("{} is the capital of {}".format(value,key))