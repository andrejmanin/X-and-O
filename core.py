def check_win_horizontal(list):
    count_X = 0
    count_O = 0

    # i - y, j - x
    for i in range(3):
        for j in range(3):
            if list[i][j] == 'X':
                count_X += 1
            elif list[i][j] == 'O':
                count_O += 1
            if count_X == 3:
                return "X win"
            if count_O == 3:
                return "O win"
        count_O = 0
        count_X = 0

def chech_with_vertical(list):
    count_X = 0
    count_O = 0

    # i - y, j - x
    for i in range(3):
        for j in range(3):
            if list[j][i] == 'X':
                count_X += 1
            elif list[j][i] == 'O':
                count_O += 1
            if count_X == 3:
                return "X win"
            if count_O == 3:
                return "O win"
        count_O = 0
        count_X = 0

def check_with_diagonal_r_l(list):
    symbol = list[0][2]

    j = 2
    for i in range(3):
        if list[i][j] != symbol:
            return
        j -= 1

    if symbol == 'O':
        return "O win"

    elif symbol == 'X':
        return "X win"

def check_with_diagonal_l_r(list):
    symbol = list[0][0]

    j = 0
    for i in range(3):
        if list[i][j] != symbol:
            return
        j += 1

    if symbol == 'O':
        return "O win"

    elif symbol == 'X':
        return "X win"