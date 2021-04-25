print('Hello world\n' * 4 + 'I love python\n' * 4)

month = input('type in month 1 to 12')
if month.isnumeric():
    if 3 <= int(month) <= 5:
        print('spring')
    elif 6 <= int(month) <= 8:
        print('summer')
    elif 9 <= int(month) <= 11:
        print('autumn')
    elif int(month) == 12 or int(month)==1 or int(month)== 2:
        print('winter')
else:
    input('number from 1 to 12')