from game import Game

Battle = True

results = {
    'win': 0,
    'loss': 0,
    'draw': 0
}


while Battle:
    print('Welcome to Rock Paper Scissors')
    user_choice = ''
    while user_choice != 'p' and user_choice != 's' and user_choice != 'q':
        print('How do you want to proceed?')
        print('(p) to play')
        print('(s) for scores')
        print('(q) for quit')
        user_choice = input('make your choice')

    if user_choice == 'p':
        play = Game.get_game_result()
        results[play] += 1
    elif user_choice == 's':
        for key, value in results.items():
            print(f'{key} = {value}')
    else:
        print('See you later')
        for key, value in results.items():
            results[key] = 0

        break

