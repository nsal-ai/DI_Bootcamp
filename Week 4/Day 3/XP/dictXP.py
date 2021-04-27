
# Exercise 1 ===========

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dictionary = dict(zip(keys, values))

print(dictionary)


# Exercise 2 ===========

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

keys = ['rick', 'beth', 'morty', 'summer']
ticket = []

i = 0
for i in range(0, len(keys)):
    if family[keys[i]] < 3: 
        ticket.append(0)
    elif 3 < family[keys[i]] < 12:
        ticket.append(10)
    elif family[keys[i]] > 12:
        ticket.append(15)
i += 1
print(sum(ticket))



age = input('age?')
list_age = []
list_age.append(age)
name =input('name')
list_name = []
list_name.append(name)
family = []
family = dict(zip(list_name, list_age))

# Exercise 3 ============


brand = {
'name': 'Zara', 
'creation_date': '1975', 
'creator_name': 'Amancio Ortega Gaona', 
'type_of_clothes': ['men', 'women', 'children', 'home'], 
'international_competitors': ['Gap', 'H&M', 'Benetton'], 
'number_stores': 7000, 
'major_color':{ 
    'France': 'blue', 
    'Spain': 'red', 
    'US': ['pink', 'green']}
    }

brand['number_stores'] = 2
print(brand)
print('Zara' + ' s' + 'clients are international')
x = {'country_creation': 'Spain'}
brand.update(x)
print(x)

if 'international_competitors' in brand:
    brand['international_competitors'].append('Desigual')
    print(brand)

del(brand['creation_date'])
print(brand['international_competitor'][2])
print(brand['major_color']['US'])
print(len(brand))
print(brand.keys())

more_on_zara = {'creation_date': 1975,
'number_stores': 10000}

brand.update(more_on_zara)
print(brand)

print(brand['number_stores'])
#the latest data overwrites the previous key value


# Exercise 4 ==================

users = [ "Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
users_2 = {}
for index, user in enumerate(users):
    users_2[index] = user
print(users_2)

for key, value in enumerate(users):
    disney_users_B[value] = key
print(disney_users_B)

disney_users_C = {}
newList = sorted(users)
for key, value in enumerate(newList):
    disney_users_C[value] = key
print(disney_users_C)

disney_users_A = {}
for key, value in enumerate(users):
    if 'i' in users[key]:
        continue
    disney_users_A[value] = key
print(disney_users_A)

disney_users_A = {}
for key, value in enumerate(users):
    if users[key][0] == 'M' or users[key][0] == 'P':
        disney_users_A[value] = key
    
print(disney_users_A)



    






