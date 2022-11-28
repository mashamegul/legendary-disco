"""
CSSE1001 Assignment 1
Semester 2, 2022
"""
from a1_support import *


# Fill these in with your details
__author__ = "Your Name"
__email__ = "Your Email"
__date__ = "14/07/2022"


# Write your functions here


board_one = "68513294773459821621976485392687153485134967247325618956842739134291576819768342 "
board_two = "68513  477      1  1 764 5 9   7 5 48 1  9 724 3  6      42739  4 9   681 7   4 "
board_three = [
    [6, 8, 5, 1, 3, 2, 9, 4, 7],
    [7, 3, 4, 5, 9, 8, 2, 1, 6],
    [2, 1, 9, 7, 6, 4, 8, 5, 3],
    [9, 2, 6, 8, 7, 1, 5, 3, 4],
    [8, 5, 1, 3, 4, 9, 6, 7, 2],
    [4, 7, 3, 2, 5, 6, 1, 8, 9],
    [5, 6, 8, 4, 2, 7, 3, 9, 1],
    [3, 4, 2, 9, 1, 5, 7, 6, 8],
    [1, 9, 7, 6, 8, 3, 4, 2, None]
    ]

board_four = [
    [6, 8, 5, 1, 3, None, None, 4, 7],
    [7, None, None, None, None, None, None, 1, None],
    [None, 1, None, 7, 6, 4, None, 5, None],
    [9, None, None, None, 7, None, 5, None, 4],
    [8, None, 1, None, None, 9, None, 7, 2],
    [4, None, 3, None, None, 6, None, None, None],
    [None, None, None, 4, 2, 7, 3, 9, None],
    [None, 4, None, 9, None, None, None, 6, 8],
    [1, None, 7, None, None, None, 4, None, None]
    ]

def num_hours() -> float:
    '''
        Parameters:
        Returns:
    '''     
    return 5.0


def is_empty(position: tuple[int, int], board: Board) -> bool:
    row = position[0]
    column = position[1]
    if board[row][column] == None:
        empty = True
    else:
        empty = False
    return empty

def update_board(position: tuple[int, int], value: Optional[int], board: Board) -> None:
    '''
    '''
    row = position[0]
    column = position[1]
    board[row][column] = value 

    return board

def clear_position(position: tuple[int, int], board: Board) -> None:
    '''
    '''
    row = position[0]
    column = position[1]
    board[row][column] = None

    return board

def read_board(raw_board: str) -> Board:
    row = []
    board = []
    column = 0

    while column < 9:
        for i in raw_board[0:9]:
            if i == ' ':
                row += [None]
            else:
                row += [int(i)]
        board += [row]
        row = []
        column += 1
        raw_board = raw_board[9:]

    return board

def print_board(board: Board) -> None:
    row = []
    print_list = []
    print_string = ''
    
    row_board = [0, 1, 2, 3, 4, 5 ,6 ,7 ,8]
    column_board= [0, 1, 2, 3, 4, 5 ,6 ,7 ,8]

    for x in row_board:
        for y in column_board:
            if board[x][y] == None:
                board[x][y] = ' '

        row = board[x][0:3] + ['|'] + board[x][3:6] + ['|'] + board[x][6:] + [' ', x]
        print_list += row

    for i in print_list:
        print_string += str(i)

    boardprint = (print_string[0:13] + "\n" +
                  print_string[13:26] + "\n" +
                  print_string[26:39] + "\n" +
                  "-----------\n" +
                  print_string[39:52] + "\n" +
                  print_string[52:65] +  "\n" +
                  print_string[65:78] + "\n" +
                  "-----------\n" +
                  print_string[78:91] + "\n" +
                  print_string[91:104] + "\n" +
                  print_string[104:117] + "\n")


    print(boardprint)
    print('012 345 678')

def has_won(board: Board) -> bool:
    valid_value = {1, 2, 3, 4, 5, 6, 7, 8, 9}       # set of valid values (i.e 1 to 9)
    check_value = {}                        # dictionary for checking which values has been encountered

    # iterating over grid rowise
    for r in board:                  
        for c in r:                 
            if c in valid_value:            # check if it is a valid value 
                if (c in check_value):      # check if c is in dictionary
                    if (check_value[c]):     # means row contains a duplicate
                        return False
                else:               # if c is not in dictionary add it to the dictionary 
                    check_value[c] = True
            else:
                return False
        check_value.clear()         # clear dictionary for checking new row

    # iterating over grid columnwise and doing same thing as we did when iterating rowise
    for c in range(len(board[0])):
        for r in range((len(board))):
            if (board[c][r] in valid_value):
                if (board[c][r] in check_value):
                    if (check_value[board[c][r]]):
                        return False
                    else:
                        check_value[board[c][r]] = True
            
            else:
                return False
        check_value.clear()

    return True

def main() -> None:
    if __name__ == "__main__":
        main()
