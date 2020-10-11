class tic_tac_toe:
    def player_name (self):
        print ("Enter the name of player one: ")
        player_1 =
        print("Enter the name of player two: ")
        player_2 =
        return player_1, player_2

    def roles (self, player_1: str, player_2: str):
        import random
        players = [player_1, player_2]
        random.shuffle(players)
        symbol_1 = "crosses"
        symbol_2 = "zeros"
        symbols = [symbol_1, symbol_2]
        random.shuffle(symbols)
        print("The first player to go is ", players[0], "\n",
              player_1, " plays with ", symbols[0], "\n", player_2, " plays with ",symbols[1])
        return players, symbols

    def validation (self, players: list, symbols: list,
                    count: int, row: int, column: int, field: list):
        if field[row][column] is not "-":
            print ("Cell is already occupied\n")

    def field_output (self, field: list):
        for i in range(3):
            for j in range(3):
                print("{:4d}".format(field[i][j]), end="")
            print()
