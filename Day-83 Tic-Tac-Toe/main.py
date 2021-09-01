# Tic-Tac-Toe


def print_board(board):
    print(f"  {board['1']}  |  {board['2']}  |  {board['3']}")
    print("---------------")
    print(f"  {board['4']}  |  {board['5']}  |  {board['6']}")
    print("---------------")
    print(f"  {board['7']}  |  {board['8']}  |  {board['9']}")


def check_for_win(board, element):
    if board['1'] == element and board['2'] == element and board['3'] == element:
        return True
    elif board['1'] == element and board['4'] == element and board['7'] == element:
        return True
    elif board['1'] == element and board['5'] == element and board['9'] == element:
        return True
    elif board['3'] == element and board['6'] == element and board['9'] == element:
        return True
    elif board['3'] == element and board['5'] == element and board['7'] == element:
        return True
    elif board['2'] == element and board['5'] == element and board['8'] == element:
        return True
    elif board['4'] == element and board['5'] == element and board['6'] == element:
        return True
    elif board['7'] == element and board['8'] == element and board['9'] == element:
        return True


def tic_tac_toe():
    print_board(the_board)

    for i in range(10):
        # while loop runs until legal position is given
        while True:
            x_index = int(input("Enter X. Positions start from 1,2,...9. "))
            # Check if the block is empty or not
            if the_board[f"{x_index}"] == "Y" or the_board[f"{x_index}"] == "X":
                print("Enter another position.")
            else:
                # if block is empty, put X in it
                the_board[f"{x_index}"] = "X"
                print_board(the_board)
                break
        # check for X's win
        if check_for_win(the_board, "X"):
            print("\n\n.....X wins.....\n\n")
            return

        # while loop runs until legal position is given
        while True:
            y_index = int(input("Enter Y. Positions start from 1,2,...9. "))
            # Check if the block is empty or not
            if the_board[f"{y_index}"] == "Y" or the_board[f"{y_index}"] == "X":
                print("Enter another position.")
            else:
                # if block is empty, put Y in it
                the_board[f"{y_index}"] = "Y"
                print_board(the_board)
                break
        # check for Y's win
        if check_for_win(the_board, "Y"):
            print("\n\n.....Y wins.....\n\n")
            return

        # check for the draw
        if i == 9:
            print("\n\n.....Match Draw.....\n\n")
            return


while True:
    the_board = {
        "1": "", "2": "", "3": "",
        "4": "", "5": "", "6": "",
        "7": "", "8": "", "9": "",
    }
    choice = input("PRESS Y to start Tic-Tac-Toe?").upper()
    if choice == "Y":
        tic_tac_toe()
    else:
        exit()
