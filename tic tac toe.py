cells = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def field():
    print("---------")
    print("|", cells[0], cells[1], cells[2], "|")
    print("|", cells[3], cells[4], cells[5], "|")
    print("|", cells[6], cells[7], cells[8], "|")
    print("---------")

field()

moves = 1

while moves < 10:
    coordinates = input("Enter the coordinates: >").split()
    m_coord = []

    if coordinates[0].isdigit() is True and coordinates[1].isdigit() is True:
        for number in coordinates:
            m_coord.append(int(number))
        if m_coord[0] in range(1, 4) and m_coord[1] in range(1, 4):
            coord_index = ((m_coord[0] - 1) + (9 - (3 * m_coord[1])))

            if len(cells[coord_index]) == 1 and moves % 2 == 1:
                cells[coord_index] = 'X'
                field()
                moves += 1

            elif len(cells[coord_index]) == 1 and moves % 2 == 0:
                cells[coord_index] = 'O'
                field()
                moves += 1
            else:
                print("This cell is occupied! Choose another one!")
        else:
            print('Coordinates should be from 1 to 3!')

    else:
        print('You should enter numbers!')
    row_1 = [cells[0], cells[1], cells[2]]
    row_2 = [cells[3], cells[4], cells[5]]
    row_3 = [cells[6], cells[7], cells[8]]

    col_1 = [cells[0], cells[3], cells[6]]
    col_2 = [cells[1], cells[4], cells[7]]
    col_3 = [cells[2], cells[5], cells[8]]

    diag_1 = [cells[0], cells[4], cells[8]]
    diag_2 = [cells[2], cells[4], cells[6]]


    combinations = (row_1, row_2, row_3, col_1, col_2, col_3, diag_1, diag_2)

    win_X_count = 0
    win_O_count = 0

    for combination in combinations:
        if combination[0] == combination[1] == combination[2] == 'X':
            win_X_count += 1
        elif combination[0] == combination[1] == combination[2] == 'O':
            win_O_count += 1
    if win_X_count == 1 and win_O_count == 0:
        print('X wins')
        break
    elif win_O_count == 1 and win_X_count == 0:
        print('O wins')
        break
    elif moves == 10:
        print('Draw')



