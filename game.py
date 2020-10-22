class TicTacToe:
    def __init__(self, player_1: str, player_2: str):
        self.player_1 = player_1
        self.player_2 = player_2

    def roles(self):
        import random
        players = [player_1, player_2]
        random.shuffle(players)
        symbols = ["crosses", "zeros"]
        random.shuffle(symbols)
        print("The first player to go is ", players[0], "\n",
              players[0], " plays with ", symbols[0], "\n", players[1], " plays with ", symbols[1])
        return players, symbols

    def validation(self, row: int, column: int):
        if row != {0, 1, 2} or column != {0, 1, 2}:
            print("Cell doesn't exist. Choose numbers of row and column from 0 to 2\n")
            row = input()
            column = input()
            validation(self, row, column)

    def free_cell(self, row: int, column: int, field: list):
        from tic_tac_toe import validation
        if field[row][column] != "-":
            print("Cell is already occupied, choose another one\n")
            row = input()
            column = input()
            validation(self, row, column)
            free_cell(self, row, column, field)

    def field_output(self, field: list):
        for i in range(3):
            for j in range(3):
                print("{:4d}".format(field[i][j]), end="")
            print()

    def vin_check(self, field: list, count: int, players: list):
        import sys
        for i in range(3):
            if field[i][0] == field[i][1] == field[i][2] or field[0][i] == field[1][i] == field[2][i]:
                print("The winner is ", players[(count + 1) % 2])
                sys.exit()
        if field[0][0] == field[1][1] == field[2][2] or field[0][2] == field[1][1] == field[2][0]:
            print("The winner is ", players[(count + 1) % 2])
            sys.exit()

    def whose_turn(self, count: int, players: list, symbols: list):
        print("Player", players[count], "moves with ", symbols[count])

    def move(self, players: list, symbols: list, count: int, field: list):
        from tic_tac_toe import validation
        from tic_tac_toe import free_cell
        from tic_tac_toe import field_output
        from tic_tac_toe import vin_check
        from tic_tac_toe import whose_turn
        whose_turn(count, players, symbols)
        print("Enter the row number(from 0 to 2)\n")
        row = input()
        print("\nEnter the column number(from 0 to 2)")
        column = input()
        validation(self, row, column)
        free_cell(self, row, column, field)
        field[row][column] = symbols[count]
        count = (count + 1) % 2
        field_output(self, field)
        vin_check(self, field, count, players)
        return count

if __name__ == '__main__':
    print("Enter the name of player one: ")
    player_1 = input()
    print("Enter the name of player two: ")
    player_2 = input()
    TicTacToe = TicTacToe(player_1, player_2)

    field = [["-", "-", "-"],
             ["-", "-", "-"],
             ["-", "-", "-"]]
    count = 0
    field_output(self, field)
    while 1:
        count = move(self, players, symbols, count, field)
