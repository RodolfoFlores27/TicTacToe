from random import randint
from IPython.display import clear_output

board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

def introduction():
    print('Welcome to Tic Tac Toe!')
    print('*************************')
    print('*       *       *       *')
    print('*   ' + '1' + '   *   ' + '2'+ '   *   ' + '3' + '   *')
    print('*       *       *       *')
    print('*************************')
    print('*       *       *       *')
    print('*   ' + '4' + '   *   ' + '5' + '   *   ' + '6' + '   *')
    print('*       *       *       *')
    print('*************************')
    print('*       *       *       *')
    print('*   ' + '7' + '   *   ' + '8' + '   *   ' + '9' + '   *')
    print('*       *       *       *')
    print('*************************')

#display board
def display_board(board):
    print('')
    print('Current Board')
    print('*************************')
    print('*       *       *       *')
    print('*   ' + board[1] + '   *   ' + board[2] + '   *   ' + board[3] + '   *')
    print('*       *       *       *')
    print('*************************')
    print('*       *       *       *')
    print('*   ' + board[4] + '   *   ' + board[5] + '   *   ' + board[6] + '   *')
    print('*       *       *       *')
    print('*************************')
    print('*       *       *       *')
    print('*   ' + board[7] + '   *   ' + board[8] + '   *   ' + board[9] + '   *')
    print('*       *       *       *')
    print('*************************')

#ask for player names
def player_names():
    '''
    OUTPUT = (Player1, Player2)
    '''
    print('')
    print('Please enter your names: ')   
    name1 = input('Player1: ')
    name2 = input('Player2: ')
    return name1, name2

#assigns who on the two players will be X.
def assign_symbol_to_player(name1, name2):
    x_player = 'whatever'
    o_player = 'whatever'
    X = randint(1,2)
    
    if X == 1:
        x_player = name1
        o_player = name2
    elif X == 2:
        x_player = name2
        o_player = name1
    print('')
    print(f'{x_player} will be playing X')
    return x_player, o_player

#checks if turn made a win
def win(board):
    if ((board[1] == board[2] == board[3] != ' ') or #row1
    (board[4] == board[5] == board[6] != ' ') or     #row2
    (board[7] == board[8] == board[9] != ' ') or     #row3
    (board[1] == board[4] == board[7] != ' ') or     #column1
    (board[2] == board[5] == board[8] != ' ') or     #column2
    (board[3] == board[6] == board[9] != ' ') or     #column3
    (board[1] == board[5] == board[9] != ' ') or     #diagonal
    (board[7] == board[5] == board[3] != ' ')):      #diagonal
        return True
    return False

#checks if turn made a tie
def tie(board):
    my_list = []
    for i in range(1,len(board)):
        if board[i] != ' ':
            my_list.append(board[i])
    if len(my_list) == len(board)-1: 
        return True
    return False

#lists the possible inputs, (1-9)
def possible_inputs():
    my_list = []
    for i in range(1,10):
        my_list.append(str(i))
    return my_list

#asks the current_players move
def turn(symbol, board, input_list):
    while True:
        player_input = input(f'Pick a box to put your symbol ({symbol}): ')
        #P_input = check_if_valid(player_input, input_list, symbol)
        if player_input not in input_list:
            print('Input not in range of [1-9]')
        elif board[int(player_input)] != ' ':
            print('Box already filled!')
          #check_if_valid(player_input, input_list, symbol)
        else:
            board[int(player_input)] = symbol
            break

#gameplay
def gameplay():
    global board
    player1_turn = True
    player2_turn = False
    moves = 0
    current_player = 'none'

    if player1_turn == True:
        current_player = player1
    elif player2_turn == False:
        current_player = player2

    while moves < 9:
        if player1_turn:
            symbol = 'X'
            display_board(board)
            print(f"It's your turn {player1}")
        
            #while input is invalid
            turn(symbol, board, input_list)

            #checks if game ended
            if win(board) or tie(board):
                display_board(board)
                return current_player

            #swaps turn to next player
            else:
                player1_turn = False
                player2_turn = True
                moves += 1

        if player2_turn:
            symbol = 'O'
            display_board(board)
            print(f"It's your turn {player2}")
        
            #while input is invalid
            turn(symbol, board, input_list)

            #checks if game ended
            if win(board) or tie(board):
                display_board(board)
                return current_player

            #swaps turn to next player
            else:
                player1_turn = True
                player2_turn = False
                moves += 1

def who_won(winner):
    print(f'GG, {winner} won!')

def play_again():
    while True:
        play = input('Play another match (Y or N)?: ')
        if play == "Y":
            #rerun game
            return True

        elif play == "N":
            #do not run game
            return False

        else: 
            print('Oops!, input not in options (Y or N):')


#Run Game
introduction()

while True:
    name1, name2 = player_names()
    player1, player2 = assign_symbol_to_player(name1, name2)
    input_list = possible_inputs()
    winner = gameplay()
    who_won(winner)

    if play_again():
        board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    else:
        break