from core import *

def print_board(list):
    board = f'''
                        #---#---#---#
                        | {list[0][0]} | {list[0][1]} | {list[0][2]} |
                        #---#---#---#
                        | {list[1][0]} | {list[1][1]} | {list[1][2]} |
                        #---#---#---#
                        | {list[2][0]} | {list[2][1]} | {list[2][2]} |
                        #---#---#---#
    '''
    print(board)

def check(list, symbol):
    if check_win_horizontal(list) == f"{symbol} win":
        print_board(list)
        print(f"Player {symbol} win")
        return True
    if chech_with_vertical(list) == f"{symbol} win":
        print_board(list)
        print(f"Player {symbol} win")
        return True
    if check_with_diagonal_l_r(list) == f"{symbol} win":
        print_board(list)
        print(f"Player {symbol} win")
        return True
    if check_with_diagonal_r_l(list) == f"{symbol} win":
        print_board(list)
        print(f"Player {symbol} win")
        return True

def game():
    list = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']]
    i = 0
    while True:
        if i % 2 == 0:
            print("Player 1")
            print_board(list)
            while(True):
                try:
                    user_inp = int(input("Enter position: ")) - 1
                except ValueError as e:
                    print("You entered wrong type!")
                    print(e)
                    return
                posX = user_inp % 3
                posY: int = int(user_inp / 3)
                if list[posY][posX] == ' ':
                    break
                else:
                    print("You are trying to place your symbol on an occupied space!")
                    print_board(list)
                    print("Check board and take another place")
            list[posY][posX] = 'X'
            if check(list, 'X'):
                break
        else:
            print("Player 2")
            print_board(list)
            while (True):
                try:
                    user_inp = int(input("Enter position: ")) - 1
                except ValueError as e:
                    print("You entered wrong type!")
                    print(e)
                    return
                posX = user_inp % 3
                posY: int = int(user_inp / 3)
                if list[posY][posX] == ' ':
                    break
                else:
                    print("You are trying to place your symbol on an occupied space!")
                    print_board(list)
                    print("Check board and take another place")
            list[posY][posX] = 'O'
            if check(list, 'O'):
                break

        i += 1
        if i == 9:
            print("No winner")
            break

game()