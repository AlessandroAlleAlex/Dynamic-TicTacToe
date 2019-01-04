import itertools


def win(current_game):  # make it dynamic
    # nested function that serves only as a helper for repeated statements
    # to reduce repetition
    def same_condition(list):  
        # if the first element of the passed list is the same for the entire list and not zero:
        if list.count(list[0]) == len(list) and list[0] != 0:  # dynamic win check
            return True
        else:
            return False

    # Horizontal win check
    for row in game:  # 3 nested lists and so on for a dynamic board
        if same_condition(row):  # if True
            print(f'Player {row[0]} is the winner horizontally!')
            return True

    # Vertical win check 
    for column in range(len(game)):  # 1, 2, 3, ... - index values
        check = []  # resets as many times the above statement
        for row in game:  # list1, list2, list3, ... - nested lists 
            check.append(row[column])  
        # here the check list contains the entire vertical values
        if same_condition(check):
            print(f'Player {check[0]} is the winner vertically! (|)')
            return True

    # Diagonal win check \
    diags = []
    for index in range(len(game)):
        diags.append(game[index][index])  # 00,11,22, ...
    if same_condition(diags):
        print(f'Player {diags[0]} is the winner diagonally! (\\)')  # double escape prints \
        return True

    # Diagonal win check /
    diags = []
    # col is the index and row is the inversed range of the len game board:
    # output -> example -> 3x3:
    # 0 2
    # 1 1
    # 2 0
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])  # in this case the order does not matter
    if same_condition(diags):
        print(f'Player {diags[0]} is the winner diagonally! (/)')
        return True 
    
    return False  # False if the function did not hit any True conditions


def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print("This position is already taken/occupied. Choose another.")
            return game_map, False
        # print("  0  1  2")
        print("   "+"  ".join([str(i) for i in range(len(game_map))]))
        if just_display is False:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map, True
    except IndexError as err:
        print("Error: make sure you input row/column correctly.", err)
        return game_map, False
    except Exception as err:
        print("Something went very wrong!", err)
        return game_map, False
    

play = True 
players = [1, 2]
while play:
    # game = [[0, 0, 0],
    #         [0, 0, 0],
    #         [0, 0, 0]]
    game_size = int(input('input board size: '))  
    game = []  # make the board dynamic 
    for i in range(game_size):
        row_board = []  # temp holder
        for i in range (game_size):
            row_board.append(0)  # append zeros in the list
        game.append(row_board)  # append the list
    game_won = False
    # _ means we do not care the second return value in the corresponding function call
    game, _ = game_board(game, just_display=True)  
    player_choise = itertools.cycle([1, 2])
    while not game_won:
        current_player = next(player_choise)
        print(f'Current Player: {current_player}')
        played = False
        while not played:
            column_choice = int(input("what column do you want to play? "))
            row_choice = int(input("what row do you want to play? "))
            # game_board() return 2 values
            game, played = game_board(game, current_player, row_choice, column_choice)
        if win(game):
            game_won = True
            again = input("play again? (y/n)")
            if again.lower() == 'y':
                # play keeps looping because of the True bool value
                print("restarting...")  
            elif again.lower() == 'n':
                print("end..")
                play = False
            else:
                print('invalid enter..End..')
                play = False





