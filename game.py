class tic_tac_toe:
    def player_name(self):
        print("Enter the name of player one: ")
        player_1 =
        print("Enter the name of player two: ")
        player_2 =
        return player_1, player_2

    def roles(self, player_1: str, player_2: str):
        import random
        players = [player_1, player_2]
        random.shuffle(players)
        symbol_1 = "crosses"
        symbol_2 = "zeros"
        symbols = [symbol_1, symbol_2]
        random.shuffle(symbols)
        print("The first player to go is ", players[0], "\n",
              player_1, " plays with ", symbols[0], "\n", player_2, " plays with ", symbols[1])
        return players, symbols

    def validation(self, row: int, column: int, field: list):
        return field[row][column] != "-"

    def field_output(self, field: list):
        for i in range(3):
            for j in range(3):
                print("{:4d}".format(field[i][j]), end="")
            print()

    # def check_equal(self, line: list):
    #   return len(set(line)) <= 1

    def vin_check(self, field: list, count: int, players: list):
        # from tic_tac_toe import check_equal
        import sys
        winner = (count + 1) % 2
        for i in range(3):
            if field[i][0] == field[i][1] == field[i][2] or field[0][i] == field[1][i] == field[2][i]:
                print ("The winner is ", players[winner])
                sys.exit()
        if field[0][0] == field[1][1] == field[2][2] or field[0][2] == field[1][1] == field[2][0]:
            print("The winner is ", players[winner])
            sys.exit()

    def move(self, players: list, symbols: list, count: int, field: list):
        from tic_tac_toe import validation
        from tic_tac_toe import field_output
        from tic_tac_toe import vin_check
        if count is 0:
            print("Player", players[0], "moves\n")
        else:
            print("Player", players[1], "moves\n")
        row =
        column =
        while validation(row, column, field):
            print("Cell is already occupied, choose another one\n")
            row =
            column =
            val = validation(row, column, field)
        if count is 0:
            field[row][column] = symbols[0]
        else:
            field[row][column] = symbols[1]
        count = (count + 1) % 2
        field_output(field)
        vin_check(field, count, players)
        return count
