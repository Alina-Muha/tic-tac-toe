class TicTacToe:
    def __init__(self, move1: int, cells: list,
                 count: int, players: list, symbols: list, free_cells: list, moves: int):
        self.move1 = move1
        self.cells = cells
        self.count = count
        self.players = players
        self.symbols = symbols
        self.free_cells = free_cells
        self.moves = moves

    def roles(self):
        """Определяет случайным образом порядок, в котором будут ходить игроки,
         и кто какими символами ходит."""

        import random
        random.shuffle(self.players)
        random.shuffle(self.symbols)
        print("The first player to go is ", players[0], "\n",
              players[0], " plays with ", symbols[0], "\n", players[1], " plays with ", symbols[1], "\n")

    def field(self):
        """Выводит игровое поле."""

        print(" ", self.cells[0], " | ", self.cells[1], " | ", self.cells[2], "\n -------------- \n",
              self.cells[3], " | ", self.cells[4], " | ", self.cells[5], "\n -------------- \n",
              self.cells[6], " | ", self.cells[7], " | ", self.cells[8])

    def validation(self):
        """Проверяет корректность введенного номера хода.
        Если ход невозможен, сообщает об этом и просит переходить."""

        if self.move1 not in self.free_cells:
            print("Cell is already occupied or doesn't exist. Please choose free cell\n")
            self.move1 = int(input())
            TicTacToe.validation(self)

    def vin_check(self):
        """Проверяет, не стоят ли на поле три одинаковых символа в ряд,
         то есть не был ли предыдущий ход выигрышным."""

        import sys
        win_str = {(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 5, 9),
                   (3, 5, 7), (1, 4, 7), (2, 5, 8), (3, 6, 9)}
        for i in win_str:
            if self.cells[i[0] - 1] == self.cells[i[1] - 1] == self.cells[i[2] - 1]:
                print("The winner is ", self.players[(self.count + 1) % 2])
                sys.exit()

    def move(self):
        """Осуществляет ход игрока. Считывает номер клетки,
        на которую игрок сходил и записывает нужный символ в соответсвующую клетку поля."""

        import sys
        if self.moves == 9:
            print("The game is tied")
            sys.exit()
        print("Player", self.players[self.count], "moves. Enter the cell number:")
        self.move1 = int(input())
        TicTacToe.validation(self)
        if self.symbols[self.count] == "zeros (O)":
            self.cells[self.move1 - 1] = "0"
        else:
            self.cells[self.move1 - 1] = "X"
        del self.free_cells[free_cells.index(self.move1)]
        self.count = (self.count + 1) % 2
        TicTacToe.field(self)
        TicTacToe.vin_check(self)
        self.moves += 1


print("Enter the name of player one: ")
player_1 = input()
print("Enter the name of player two: ")
player_2 = input()
cells = [1, 2, 3, 4, 5, 6, 7, 8, 9]
players = [player_1, player_2]
symbols = ["crosses (X)", "zeros (O)"]
free_cells = [1, 2, 3, 4, 5, 6, 7, 8, 9]
game = TicTacToe(0, cells, 0, players, symbols, free_cells, 0)
game.roles()
game.field()
while True:
    game.move()
