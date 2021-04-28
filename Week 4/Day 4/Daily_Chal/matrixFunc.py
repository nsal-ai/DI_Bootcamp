# read from top to bottom
# only select alpha characters (a-z)
# connect the alphas
# every group of symbols between 2 alpha characters replaced
# by a space


code_message = [
    [ 7, 'i', 3],
    ['T', 's', 'i'],
    ['h', '%', 'x'],
    ['i', ' ', '#'],
    ['s', 'M', ' '],
    ['$', 'a', ' '],
    ['#', 't', '%'],
    ['^', 'r', '!']

]

x = 0
y = 0

for y in range(0, 3):
    for x in range(0, len(code_message)):
        if code_message[x][y].isalpha() == True:
            print(code_message[x][y], end = '')
        elif code_message[x][y].isalpha() == False and code_message[x][y-1].isalpha() == False:
            print('', end = ' ')
        elif code_message[x][y] == ' ':
            print(' ', end= ' ')
         
