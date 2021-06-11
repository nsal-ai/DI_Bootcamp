
def print_tic_tac_toe(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")
 

def check_win(player_pos, cur_player):
 
    
    soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
 
    # Loop to check if any winning combination is satisfied
    for x in soln:
        if all(y in player_pos[cur_player] for y in x):
 
            # Return True if any winning combination satisfies
            return True
    # Return False if no combination is satisfied       
    return False       
 

def check_draw(player_pos):
    if len(player_pos['X']) + len(player_pos['O']) == 9:
        return True
    return False       
 

def single_game(cur_player):
    values = [' ' for x in range(9)]
    # Stores the positions occupied by X and O
    player_pos = {'X':[], 'O':[]}
     
    #Game Loop for a single game of Tic Tac Toe
    while True:
        print_tic_tac_toe(values)
         
        
        try:
            print("Player ", cur_player, " turn. Which box? : ", end="")
            move = int(input()) 
        except ValueError:
            print("Wrong Input!!! Try Again")
            continue
 
        if move < 1 or move > 9:
            print("Wrong Input!!! Try Again")
            continue
 
        # Check if the box is not occupied already
        if values[move-1] != ' ':
            print("Place already filled. Try again!!")
            continue
 
        
 
    # Updating grid status 
        values[move-1] = cur_player

        # Updating player positions
        player_pos[cur_player].append(move)

        # Function call for checking win
        if check_win(player_pos, cur_player):
            print_tic_tac_toe(values)
            print("Player ", cur_player, " has won the game!!")     
            print("\n")
            return cur_player

        # Function call for checking draw game
        if check_draw(player_pos):
            print_tic_tac_toe(values)
            print("Game Drawn")
            print("\n")
            return 'D'

        # Switch player moves
        if cur_player == 'X':
            cur_player = 'O'
        else:
            cur_player = 'X'



if __name__ == "__main__":

    print("Player 1")
    player1 = input("Enter the name : ")
    print("\n")

    print("Player 2")
    player2 = input("Enter the name : ")
    print("\n")
    
    # Stores the player who chooses X and O
    cur_player = player1

    player_choice = {'X' : "", 'O' : ""}

    options = ['X', 'O']

    
while True:

    print("Turn to choose for", cur_player)
    print("Enter 1 for X")
    print("Enter 2 for O")
    

    try:
        choice = int(input())   
    except ValueError:
        print("Wrong Input!!! Try Again")
        continue
    # Conditions for player choice  
    if choice == 1:
        player_choice['X'] = cur_player
        if cur_player == player1:
            player_choice['O'] = player2
        else:
            player_choice['O'] = player1

    elif choice == 2:
        player_choice['O'] = cur_player
        if cur_player == player1:
            player_choice['X'] = player2
        else:
            player_choice['X'] = player1

    

    # Stores the winner in a single game of Tic Tac Toe
    winner = single_game(options[choice-1])
         
