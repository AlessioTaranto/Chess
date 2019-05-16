
from pieces import Piece
from board import Board
from player import Player


# Class were all the logic is executed
class Game:
    white_team = None

    def __init__(self):
        debug = False

        # Create board
        self.board = Board()

        # Create players
        self.player1 = Player('Alessio')

        # Create teams
        self.white_team = []
        self.white_team.append(Piece('White', 'Tower', 1, 8))
        self.white_team.append(Piece('White', 'Horse', 2, 8))
        self.white_team.append(Piece('White', 'Bishop', 3, 8))
        self.white_team.append(Piece('White', 'Queen', 4, 8))
        self.white_team.append(Piece('White', 'King', 5, 8))
        self.white_team.append(Piece('White', 'Bishop', 6, 8))
        self.white_team.append(Piece('White', 'Horse', 7, 8))
        self.white_team.append(Piece('White', 'Tower', 8, 8))
        self.white_team.append(Piece('White', 'Pawn', 1, 7))
        self.white_team.append(Piece('White', 'Pawn', 2, 7))
        self.white_team.append(Piece('White', 'Pawn', 3, 7))
        self.white_team.append(Piece('White', 'Pawn', 4, 7))
        self.white_team.append(Piece('White', 'Pawn', 5, 7))
        self.white_team.append(Piece('White', 'Pawn', 6, 7))
        self.white_team.append(Piece('White', 'Pawn', 7, 7))
        self.white_team.append(Piece('White', 'Pawn', 8, 7))

        self.black_team = []
        self.black_team.append(Piece('Black', 'Tower', 1, 1))
        self.black_team.append(Piece('Black', 'Horse', 2, 1))
        self.black_team.append(Piece('Black', 'Bishop', 3, 1))
        self.black_team.append(Piece('Black', 'Queen', 4, 1))
        self.black_team.append(Piece('Black', 'King', 5, 1))
        self.black_team.append(Piece('Black', 'Bishop', 6, 1))
        self.black_team.append(Piece('Black', 'Horse', 7, 1))
        self.black_team.append(Piece('Black', 'Tower', 8, 1))
        self.black_team.append(Piece('Black', 'Pawn', 1, 2))
        self.black_team.append(Piece('Black', 'Pawn', 2, 2))
        self.black_team.append(Piece('Black', 'Pawn', 3, 2))
        self.black_team.append(Piece('Black', 'Pawn', 4, 2))
        self.black_team.append(Piece('Black', 'Pawn', 5, 2))
        self.black_team.append(Piece('Black', 'Pawn', 6, 2))
        self.black_team.append(Piece('Black', 'Pawn', 7, 2))
        self.black_team.append(Piece('Black', 'Pawn', 8, 2))

        self.cell = [-1, -1]
        self.mouse_raw = [0, 0]

        if debug is True:
            for x in range(len(self.white_team)):
                print('White ' + str(self.white_team[x].type) + ' [' + str(x) + '] position = ' + str(
                    self.white_team[x].position))

        print("Teams created\n")

    # Draw the pieces
    def draw(self):
        self.board.draw()
        for x in range(len(self.white_team)):
            self.white_team[x].draw()
        for x in range(len(self.black_team)):
            self.black_team[x].draw()

    def update(self):
        for x in range(len(self.white_team)):
            self.white_team[x].update()
        for x in range(len(self.black_team)):
            self.black_team[x].update()

        self.handle_turn()

    # A function that handle all the player moves
    def handle_turn(self):
        # Check if a piece is selected
        piece_number = -1
        for x in range(len(self.white_team)):
            if self.white_team[x].isSelected is True:
                piece_number = x
        for x in range(len(self.black_team)):
            if self.black_team[x].isSelected is True:
                piece_number = x + len(self.white_team)

        # Check if  a cell is selected
        if piece_number is not -1:
            if self.cell[0] is not -1:
                if self.cell[1] is not -1:

                    # Black Team
                    if piece_number > len(self.white_team):
                        cell = self.black_team[piece_number - len(self.white_team)].get_cell()
                        if self.cell[0] is not cell[0] or self.cell[1] is not cell[1]:
                            piece = self.black_team[piece_number - len(self.white_team)]
                            print('Move: ' + str(piece.color) + ' - ' + str(piece.type) + ' ' + str(piece.get_cell()) + ' --> ' + str(self.cell))
                            self.black_team[piece_number - len(self.white_team)].move(self.cell[0], self.cell[1])

                            # Check collisions, so it check if a white got eaten
                            for i in range(0, len(self.white_team)):
                                c = self.white_team[i].get_cell()
                                if self.cell[0] == c[0] and self.cell[1] == c[1]:
                                    w = self.white_team[i]
                                    print(str(w.color) + ' - ' + str(w.type) + ' got eaten')
                                    del self.white_team[i]
                                    break

                            # Reset
                            self.cell = [-1, -1]
                            self.mouse_raw = [-1, -1]

                    # White team
                    elif piece_number <= len(self.white_team):
                        cell = self.white_team[piece_number].get_cell()
                        if self.cell[0] is not cell[0] or self.cell[1] is not cell[1]:
                            piece = self.white_team[piece_number]
                            print('Move: ' + str(piece.color) + ' - ' + str(piece.type) + ' ' + str(piece.get_cell()) + ' --> ' + str(self.cell))
                            self.white_team[piece_number].move(self.cell[0], self.cell[1])

                            # Check collisions, so it check if a black got eaten
                            for i in range(0, len(self.black_team)):
                                c = self.black_team[i].get_cell()
                                if self.cell[0] == c[0] and self.cell[1] == c[1]:
                                    w = self.black_team[i]
                                    print(str(w.color) + ' - ' + str(w.type) + ' got eaten')
                                    del self.black_team[i]
                                    break

                            # Reset
                            self.cell = [-1, -1]
                            self.mouse_raw = [-1, -1]
        self.mouse_select()

    # Check if the mouse click is on top of a piece
    def mouse_select(self):
        # Delete old selection
        for piece in self.white_team:
            piece.isSelected = False
        for piece in self.black_team:
            piece.isSelected = False

        for piece in self.white_team:
            piece.check_if_clicked(self.mouse_raw[0], self.mouse_raw[1])
        for piece in self.black_team:
            piece.check_if_clicked(self.mouse_raw[0], self.mouse_raw[1])

    # Update the mouse il relation to cells
    def update_mouse(self, x, y):
        self.mouse_raw = [x, y]
        pos = [x, y]
        cell = [-1, -1]

        for x in range(2):
            if 450 > pos[x] > 400:
                cell[x] = 8
            elif 400 > pos[x] > 350:
                cell[x] = 7
            elif 350 > pos[x] > 300:
                cell[x] = 6
            elif 300> pos[x] > 250:
                cell[x] = 5
            elif 250> pos[x] > 200:
                cell[x] = 4
            elif 200 > pos[x] > 150:
                cell[x] = 3
            elif 150 > pos[x] > 100:
                cell[x] = 2
            elif 100 > pos[x] > 50:
                cell[x] = 1

            self.cell = cell
        # print(str(self.cell) + ' ' + str(self.mouse_raw))

    # A function to update  the map
    def update_board(self):
        self.board.clear()
        all_pieces = self.black_team + self.white_team
        for piece in all_pieces:
            cell = piece.get_cell()
            if piece.color is 'Black':
                self.board.map[cell[1] - 1][cell[0] - 1].data = 2
            else:
                self.board.map[cell[1] - 1][cell[0] - 1].data = 1

        self.board.print()

