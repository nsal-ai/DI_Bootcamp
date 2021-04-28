# Ex 1

def display_message(message):
    print(f'{message}')

display_message('i am learning python')


#Ex 2

def favourite_book(title):
    print(f'One of my favourite books is {title}')
favourite_book('art of war')

#Ex 3

def describe_city(name, country):
    print(f'{name} is in {country}')
describe_city(*('Bogota', 'Colombia'))

#Ex 4

import random
def num_choice(num):
    if 1 < int(num) < 100:
        a = int(num)
        b = (random.randint(1,100))
        if a == b:
            print('success!')
        else:
            print('fail')
            print(a)
            print(b)
    else:
        False
num_choice('10')


#Ex 5

def make_shirt(size, text):
    return f'the shirt is size {size} {text}'

print(make_shirt('M', 'and it is great'))

def make_shirt(size, text):
    size = 'L'
    return f'the shirt is size {size} {text}'

print(make_shirt('size', 'and i love python'))



def make_shirt(size, text):
    if size == 'M' or size == 'L':
        return f'the shirt is size {size} and that is a fact'
    else:
        print('that'+'s another size!!')


print(make_shirt('M', 'text'))



#Ex 6

def show_magicians(name_magicians):
    for x in name_magicians:
        print(x)


magicians = ['houdini', 'blaine', 'penTeller']
        
show_magicians(magicians)


