# Exercise 1  ===============

my_fav_numbers = {1, 11, 7, 18, 5, 3}

my_fav_numbers.add(10)
my_fav_numbers.add(2)
my_fav_numbers.pop()

friend_fav_numbers = {4, 8, 16}

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)
    

# Exercise 2 ===========

#integer value on tuple is the left number (left is the index) inside the parentheses
#cannot add more integers to a tuple due to immutable property


# Exercise 3 ===========

# for x in range(1,21):
    
#     print(x)


# Exercise 4 ===========

#floats are decimal numbers integers are whole

# use numpy to generate list of floats using arange()
# import decimals
# np.arange(1.5, 5, 0.5)

import numpy as np

for i in np.arange(1.5, 5, 0.5):
        print(i, end="")


# Exercise 5 ==============

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove('Banana')
basket.pop()
basket.append('Kiwi')
basket.insert(0, 'Apples')
basket.count('Apples')
del basket[0:len(basket)]
print(basket)


# Exercise 6 ============

active = True

while active:
    name = input("type in your name")
    if name == 'Yigal': 
        active = False


# Exercise 7 =============

my_list = [1, 5, 6, 8, 34, 76, 3, 1]
new_list = []

i = 0
for x in my_list:
    if i % 2 == 0:
        new_list.append(x)
    i += 1
print (new_list)


# Exercise 8 ==============

for x in range(1500, 2500, 1):
    if x % 5 == 0 or x % 7 == 0:
        print(x)


# Exercise 9 ==============

fav_fruit = input('whats your fav fruit(s)?')
favList = fav_fruit.split()

fruit = input('any fruit')
if fruit in favList:
    print('you chose one of the fruits enjoy')
else:
    print('ypu chose a new fruit enjoy')



# Exercise 10 =============

topping_list = []
active = True
while active:
    topping = input('choose a pizza topping')
    topping_list.append(topping)
    if topping == 'quit':
        active = False
        print(10 + 2.5*len(topping_list) - 2.5)
    else:
        print('we will add ' + topping + ' to your pizza')



# Exercise 11 ===============

age_people = input('how old is everyone?')
arrAges = age_people.split()
ticket = []
i = 0
for i in range(0, len(arrAges)):
        if  int(arrAges[i]) < 3:
            ticket.append(0)
        elif 3 < int(arrAges[i]) < 12:
            ticket.append(10)
        elif int(arrAges[i]) > 12:
            ticket.append(15)
i += 1
print(sum(ticket))


# Exercise 12 ===============

list_names = ['avi', 'chaim', 'yigal', 'emily']
i = 0
age = input('your age')
for i in range(0, len(list_names)):
    if int(age) < 16
list_names.remove(list_name[i])
print(list_name)


# Exercise 13 ==================

sandwich_orders = ['tuna', 'falafel', 'shwarma', 'sabich' ]
finished_sandwiches = []
i = 0
for i in range(0, len(sandwich_orders)):
    finished_sandwiches.append(sandwich_orders[i])
    print('i made your ' + sandwich_order[i] + ' sandwich')
i += 1


# Exercise 14 ================

sandwich_orders = ['tuna', 'pastrami', 'falafel', 'pastrami', 'shwarma', 'sabich', 'pastrami']
print('run out of pastrami')
i = 0
while i < len(sandwich_orders):
    if sandwich_orders[i] == pastrami:
        sandwich_orders.remove(index('pastrami'))
i += 1


    