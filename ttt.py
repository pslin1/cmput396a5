import numpy as np
import random

global boardformat
boardformat = []

def place_move(x,y, board, letter, appending = None):
    global boardformat
    
    #place a move at x,y coordinates
    if x in ["a", "A"]:
        board[y-1][0] = letter
    elif x in ["b", "B"]:
        board[y-1][1] = letter
    elif x in ["c", "C"]:
        board[y-1][2] = letter
    if (appending is None):
        boardformat.append(str(x)+str(y))

def check_if_winner(board, letter):
    #return true if letter wins
    return ((board[0][0] == letter and board[0][1] == letter and board[0][2] == letter) or #top row
    (board[1][0] == letter and board[1][1] == letter and board[1][2] == letter) or #middle row
    (board[2][0] == letter and board[2][1] == letter and board[2][2] == letter) or #bottom row
    (board[0][0] == letter and board[1][0] == letter and board[2][0] == letter) or #left column
    (board[0][1] == letter and board[1][1] == letter and board[2][1] == letter) or #middle column
    (board[0][2] == letter and board[1][2] == letter and board[2][2] == letter) or #right column
    (board[0][0] == letter and board[1][1] == letter and board[2][2] == letter) or #diagonal \
    (board[0][2] == letter and board[1][1] == letter and board[2][0] == letter)) #diagonal /
        
def check_if_full(board):
    #check if the board is full (draw)
    if 0.0 in board:
        return False
    else:
        return True

def int_to_str(num):
    #convert int to corresponding character
    #0 = blank space
    #1 = O
    #2 = X
    if num == 0:
        return " "
    elif num == 1:
        return "O"
    elif num == 2:
        return "X"

def str_to_int(char):
    #convert character to corresponding integer
    if char == "O":
        return 1
    elif char == "X":
        return 2

def print_board(board):
    #print the board
    print("    a    b    c\n")
    print("1   " + int_to_str(board[0][0]) + "    " + int_to_str(board[0][1]) + "    " + int_to_str(board[0][2]) + "\n")
    print("2   " + int_to_str(board[1][0]) + "    " + int_to_str(board[1][1]) + "    " + int_to_str(board[1][2]) + "\n")
    print("3   " + int_to_str(board[2][0]) + "    " + int_to_str(board[2][1]) + "    " + int_to_str(board[2][2]) + "\n")
    
def isValidInput(selected):
    if (len(selected) == 2):
        selected = selected.lower()
        f = selected[0]
        s = selected[1]
        if (f == 'a' or f == 'b' or f == 'c'):
            if (int(s) and int(s) <= 3 and int(s) > 0):
                return True
    return False

def isValidMove(selected,board):
    if (isValidInput(selected) == True):
        global boardformat
        if (selected not in boardformat):
            return True
    return False    
    
def MoveMade(board, letter):
    #Was gonna make an actual AI moves with negamax
    rows = ['a','b','c']
    cols = ['1','2','3']
    success = False
    while (success == False):
        selection = ''
        a = random.randint(0,2)
        b = random.randint(0,2)
        selection = rows[int(a)] + cols[int(b)]
        if (isValidMove(selection,board) == True):
            success = True
            place_move(selection[0], int(selection[1]), board, str_to_int(letter))
        #Else its not valid so keep running till there's a good stuff
    
    #theboard = board_to_str(board)    
    #if theboard in boardformat:
        #Already made the thing
    #else:
        #Check its stuff

def main():
    #game_stop is true when game is over (someone wins or draw)
    game_stop = False
    #player turn is True when it is the players turn
    player_turn = True
    
    board = np.zeros((3,3))
    
    player_letter = input("Please enter X or O: ").upper()
    
    
    #validating input
    while player_letter not in ["X","O"]:
        player_letter = input("Please enter X or O: ").upper()
    #computer picks letter that player did not pick
    if player_letter == "X":
        computer_letter = "O"
    else:
        computer_letter = "X"

    while (game_stop == False):
        #players turn
        if player_turn == True:
            print("Players turn\n")
            print_board(board)

            #Selection must be letter and number (eg: a3, A3, b1, etc)
            print('Coordinates must be combinations of letter and numbers; (eg. a3, A3, b1, etc)')
            selection = input("Please enter coordinates: ")

            #check if input valid here
            #newboard = place_move(selection[0], int(selection[1]), board, str_to_int(player_letter))
            if (isValidMove(selection,board) == False):
                print("Invalid cmd; Try again\n")
            else:
                #place move on board
                
                place_move(selection[0], int(selection[1]), board, str_to_int(player_letter))

                #check if that move won the game
                if check_if_winner(board, str_to_int(player_letter)):
                    print_board(board)
                    print("Player wins\n")
                    game_stop = True
                #check if that move resulted in a draw
                if check_if_full(board):
                    print_board(board)
                    print("Draw\n")
                    game_stop = True

                #end of player turn
                player_turn = False
            #computers turn
        else:
            print("Computers turn\n")
            MoveMade(board, computer_letter)
            """
            Do computer move here
            """

            #check if that move won the game
            if check_if_winner(board, str_to_int(computer_letter)):
                print_board(board)
                print("Computer wins")
                game_stop = True
            #check if that move resulted in a draw
            if check_if_full(board):
                print_board(board)
                print("Draw")
                game_stop = True

            #end of computers turn
            player_turn = True

        
            
if __name__=='__main__':
    main()
