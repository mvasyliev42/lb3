from services.tictactoe import *

board = [[" " for _ in range(3)] for _ in range(3)]
current_player = "X"

while True:
    print_board(board)
    row = int(input(f"Гравець {current_player}, введіть номер рядка (0-2): "))
    col = int(input(f"Гравець {current_player}, введіть номер стовпця (0-2): "))
    if make_move(row, col, current_player, board):
        if check_win(board):
            print_board(board)
            print(f"Гравець {current_player} переміг!")
            break
        elif check_draw(board):
            print_board(board)
            print("Нічия!")
            break
        else:
            current_player = "X" if current_player == "O" else "O"
    else:
        print("Ця клітинка вже зайнята. Спробуйте іншу.")
