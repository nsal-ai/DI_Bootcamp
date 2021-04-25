# string = input('please write string with 10 characters')
# if len(string) < 10:
#         print('string not long enough')
#     elif len(string) > 10:
#         print('string is too long')

string = input('please write string with 10 characters')
if len(string) < 10:
        print('string not long enough')
elif len(string) > 10:
        print('string is too long')

print(string[0])
print(string[-1])



i = 0
for i in range(len(string)):

    print(string[0:i+1])


import random
print(random.shuffle(string))