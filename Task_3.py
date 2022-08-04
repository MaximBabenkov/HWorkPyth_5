# Создайте программу для игры в "Крестики-нолики"

board = list(range(1, 10))

wins_coord = [(1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,7)]

def create_board() -> list:
    print('-------------')
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
        print('-------------')

def take_input(token: str):
    while True:
        value = input('Where to place ' + token + ' ?\n')
        if value not in '123456789':
            print('Your data entry is incorrect. Try again !')
            continue
        value = int(value)
        if str(board[value - 1]) in 'XO':
            print('This cell is already taken')
            continue
        board[value - 1] = token
        break

def check_win():
    for elem in wins_coord:
        if (board[elem[0] - 1]) == (board[elem[1] - 1]) == (board[elem[2] - 1]):
            return board[elem[1] - 1]
    else:
        return False

print('Tic Tac Toe')
print("Let's begin to play!")
counter = 0
while True:
    create_board()
    if counter % 2 == 0:
        take_input('X')
    else:
        take_input('O')
    if counter > 3:
        winner = check_win()
        if winner:
            create_board()
            print(winner, 'won !')
            break
    counter += 1
    if counter > 8:
        create_board()
        print('The draw!')
        break
