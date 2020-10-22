class TicTacToe:
    def __init__(self, player_1: str, player_2: str, """move1: int, cells: list,
                 count: int, players: list, symbols: list, free_cells: list"""):
        self.player_1 = player_1
        self.player_2 = player_2
        """self.move1 = move1
        self.cells = cells
        self.count = count
        self.players = players
        self.symbols = symbols
        self.free_cells = free_cells"""

    def roles(self):
        import random
        players = [player_1, player_2]
        random.shuffle(players)
        symbols = ["crosses (X)", "zeros (O)"]
        random.shuffle(symbols)
        print("The first player to go is ", players[0], "\n",
              players[0], " plays with ", symbols[0], "\n", players[1], " plays with ", symbols[1], "\n")

    def field(self, cells):
        print(cells[0], " | ", cells[1], " | ", cells[2], "\n --------- \n",
              cells[3], " | ", cells[4], " | ", cells[5], "\n --------- \n",
              cells[6], " | ", cells[7], " | ", cells[8])

    def validation(self, free_cells, move1):
        if move1 not in free_cells:
            print("Cell is already occupied or doesn't exist. Please choose free cell\n")
            self.move1 = input()
            TicTacToe.validation()

    def vin_check(self):
        import sys
        win_str = {(0, 1, 2),(3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6)}
        for i in win_str:
            if i[0] == i[1] == i[2]:
                print("The winner is ", self.players[(self.count + 1) % 2])
                sys.exit()
    def move(self):
        print("Player", self.players[self.count], "moves. Enter the cell number:")
        self.move1 = input()
        TicTacToe.validation()
        if self.symbols[self.count] == "zeros (O)":
            self.cells[self.move1] = "O"
        else:
            self.cells[self.move1] = "X"

print("Enter the name of player one: ")
player_1 = input()
print("Enter the name of player two: ")
player_2 = input()
game = TicTacToe(player_1, player_2)
game.roles()
game.field()
