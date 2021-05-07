import random

class Game:

    def __init__(self, score):
        self.score = score

    @staticmethod
    def get_user_item():
       
            game_dict = {'Rock': 1, 'Paper' : 2, 'Scissors': 3}

            while True:
                player_a = input('Choose your weapon')
                
                if player_a not in game_dict.keys():
                    print(f'Invalid weapon choice try again')
                    continue
                else:
                    break
            return player_a


    
    @staticmethod
    def get_computer_item():
        #game_dict = {'Rock': 1, 'Paper' : 2, 'Scissors': 3}
        weapons = ['Rock', 'Paper', 'Scissors']
        return random.choice(weapons)


    @classmethod
    def get_game_result(cls):
        game_dict = {'Rock': 1, 'Paper' : 2, 'Scissors': 3}
        user_item = cls.get_user_item()
        computer_item = cls. get_computer_item()
        print(f'{user_item} is your choice')
        print(f'{computer_item} is the computer\'s choice')

        difference = game_dict[user_item] - game_dict[computer_item]

        if abs(difference) == 2 or abs(difference) == 1:
            print('You WIN')
            return 'win'
        
        elif abs(difference) == 0:
            print('You drew')
            return 'draw'

        else:
            print('you lost')
            return 'loss'

# Game.get_user_item()
# Game.get_computer_item()
# Game.get_game_result()


        