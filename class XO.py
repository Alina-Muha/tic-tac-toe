class TicTacToe:
    def __init__(self, move1: int, cells: list,
                 count: int, players: list, symbols: list, free_cells: list):
        self.move1 = move1
        self.cells = cells
        self.count = count
        self.players = players
        self.symbols = symbols
        self.free_cells = free_cells

    def roles(self):
        import random
        random.shuffle(self.players)
        random.shuffle(self.symbols)
        print("The first player to go is ", players[0], "\n",
              players[0], " plays with ", symbols[0], "\n", players[1], " plays with ", symbols[1], "\n")

    def field(self):
        print(" ", self.cells[0], " | ", self.cells[1], " | ", self.cells[2], "\n -------------- \n",
              self.cells[3], " | ", self.cells[4], " | ", self.cells[5], "\n -------------- \n",
              self.cells[6], " | ", self.cells[7], " | ", self.cells[8])

    def validation(self):
        if self.move1 not in self.free_cells:
            print("Cell is already occupied or doesn't exist. Please choose free cell\n")
            self.move1 = int(input())
            TicTacToe.validation(self)

    def vin_check(self):
        import sys
        win_str = {(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 4, 8),
                   (2, 4, 6), (0, 3, 6), (1, 4, 7), (2, 5, 8)}
        for i in win_str:
            if self.cells[i[0]] == self.cells[i[1]] == self.cells[i[2]]:
                print("The winner is ", self.players[(self.count + 1) % 2])
                sys.exit()

    def move(self):
        print("Player", self.players[self.count], "moves. Enter the cell number:")
        self.move1 = int(input())
        TicTacToe.validation(self)
        if self.symbols[self.count] == "zeros (O)":
            self.cells[self.move1] = "0"
        else:
            self.cells[self.move1] = "X"
        del self.free_cells[free_cells.index(self.move1)]
        self.count = (self.count + 1) % 2
        TicTacToe.field(self)
        TicTacToe.vin_check(self)


print("Enter the name of player one: ")
player_1 = input()
print("Enter the name of player two: ")
player_2 = input()
cells = [0, 1, 2, 3, 4, 5, 6, 7, 8]
players = [player_1, player_2]
symbols = ["crosses (X)", "zeros (O)"]
free_cells = [0, 1, 2, 3, 4, 5, 6, 7, 8]
game = TicTacToe(0, cells, 0, players, symbols, free_cells)
game.roles()
game.field()
while True:
    game.move()