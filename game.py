import pyglet

from pieces import Piece
from board import Board


# Class were all the logic is executed
class Game:
    white_team = None

    def __init__(self):
        debug = False
        # Create board
        self.board = Board()

        # Create teams
        self.white_team = []
        self.white_team.append(Piece('W', 'Tower', 1, 8))
        self.white_team.append(Piece('W', 'Horse', 2, 8))
        self.white_team.append(Piece('W', 'Bishop', 3, 8))
        self.white_team.append(Piece('W', 'Queen', 4, 8))
        self.white_team.append(Piece('W', 'King', 5, 8))
        self.white_team.append(Piece('W', 'Bishop', 6, 8))
        self.white_team.append(Piece('W', 'Horse', 7, 8))
        self.white_team.append(Piece('W', 'Tower', 8, 8))
        self.white_team.append(Piece('W', 'Pawn', 1, 7))
        self.white_team.append(Piece('W', 'Pawn', 2, 7))
        self.white_team.append(Piece('W', 'Pawn', 3, 7))
        self.white_team.append(Piece('W', 'Pawn', 4, 7))
        self.white_team.append(Piece('W', 'Pawn', 5, 7))
        self.white_team.append(Piece('W', 'Pawn', 6, 7))
        self.white_team.append(Piece('W', 'Pawn', 7, 7))
        self.white_team.append(Piece('W', 'Pawn', 8, 7))

        self.black_team = []
        self.black_team.append(Piece('B', 'Tower', 1, 1))
        self.black_team.append(Piece('B', 'Horse', 2, 1))
        self.black_team.append(Piece('B', 'Bishop', 3, 1))
        self.black_team.append(Piece('B', 'Queen', 4, 1))
        self.black_team.append(Piece('B', 'King', 5, 1))
        self.black_team.append(Piece('B', 'Bishop', 6, 1))
        self.black_team.append(Piece('B', 'Horse', 7, 1))
        self.black_team.append(Piece('B', 'Tower', 8, 1))
        self.black_team.append(Piece('B', 'Pawn', 1, 2))
        self.black_team.append(Piece('B', 'Pawn', 2, 2))
        self.black_team.append(Piece('B', 'Pawn', 3, 2))
        self.black_team.append(Piece('B', 'Pawn', 4, 2))
        self.black_team.append(Piece('B', 'Pawn', 5, 2))
        self.black_team.append(Piece('B', 'Pawn', 6, 2))
        self.black_team.append(Piece('B', 'Pawn', 7, 2))
        self.black_team.append(Piece('B', 'Pawn', 8, 2))

        if debug is True:
            for x in range(len(self.white_team)):
                print('White ' + str(self.white_team[x].type) + ' [' + str(x) + '] position = ' + str(
                    self.white_team[x].position))

        print("Teams created")

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

    # Check if the mouse click is on top of a piece
    def mouse_select(self, x, y):
        # Delete ols selection
        for piece in self.white_team:
            piece.isSelected = False

        for piece in self.black_team:
            piece.isSelected = False

        for piece in self.white_team:
            piece.check_if_clicked(x, y)

        for piece in self.black_team:
            piece.check_if_clicked(x, y)

    # A function to update  the map
    def update_board(self):
        self.board.clear()
        all_pieces = self.black_team + self.white_team
        for piece in all_pieces:
            cell = piece.get_cell()
            if piece.color is 'B':
                self.board.map[cell[1] - 1][cell[0] - 1] = 2
            else:
                self.board.map[cell[1] - 1][cell[0] - 1] = 1

        self.board.print()

