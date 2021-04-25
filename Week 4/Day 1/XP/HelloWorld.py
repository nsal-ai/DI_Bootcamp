# Exercise 1

print('Hello world\n'*4)

# Exercise 2

number = (99**3) * 8
print(number)

#Exercise 3

5 < 3 #false
3 == 3 #true
3 == "3" #false
"3" > 3 #false
"Hello" == "hello" #false

#Exercise 4

computer_brand = "lenovo"

print('i have a ' + computer_brand + ' computer')


# Exercise 5

name = "Yigal"
age = 30
shoe_size = 43
info = "My name is " + name + " and my age is " + str(age) + "I am left-handed"
print(info)


# Esercise 6

number1 = input('choose number A')
number2 = input('choose number B')

if number1.isnumeric() and number2.isnumeric():
    number1 = int(number1)
    number2 = int(number2)
    if number1 > number2:
            print("Hello World")
    else:
            print('false')



#Exercise 7

number = input('choose an integer')
if number.isnumeric():
    if int(number) % 2 == 0:
        print('even')
    else:
        print('odd')


# Exercise 8

name = input('type your name')
my_name = 'Yigal'

if name == my_name:
    print('no way you must be crazy')
else:
    print('interesting')


#Exercise 9

height = input('height in cm?')
if height.isnumeric():
    if int(height) > 145:
        print('tall enough to ride')
    else:
        print('not tall enough')
else:
    print('not correct input')

