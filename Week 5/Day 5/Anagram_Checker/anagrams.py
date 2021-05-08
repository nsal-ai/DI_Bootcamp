from anagram_checker import AnagramChecker

anagram_game = True

while anagram_game:
    user_choice = ''
    print('Welcome to the Anagram Game')
    while user_choice != 'p' and user_choice != 'e':
        print('(p)lay the game')
        print('(e)xit')
        user_choice = input('What do you want to do?')

    if user_choice == 'p':
        chosen_word = str(input('Enter your word')).upper()
        while chosen_word == True:
            if len(chosen_word.split()) > 1:
                print('Error only type 1 word') 
                continue
            else:
                print(f'Your chosen word is {chosen_word}')
        user_word = AnagramChecker()
            if user_word.is_valid_word(chosen_word) == True: 
                print('This is a valid word')
                continue
            else:
                print('This is NOT valid')
                break
        result = user_word.get_anagrams(chosen_word)
        sep = ','
        print(f'Anagrams for your word:{sep.join(result)}')

    elif user_choice == 'e'
        print('see ya later')
        break


