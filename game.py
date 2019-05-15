
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

        self.cell = [-1, -1]
        self.mouse_raw = [0, 0]

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
                        print(str(self.cell) + '  ' + str(cell))
                        if self.cell[0] is not cell[0] or self.cell[1] is not cell[1]:
                                piece = self.black_team[piece_number - len(self.white_team)]
                                print('Move: ' + str(piece.color) + ' - ' + str(piece.type) + ' ' + str(piece.get_cell()) + ' --> ' + str(self.cell))
                                self.black_team[piece_number - len(self.white_team)].move(self.cell[0], self.cell[1])
                                self.cell = [-1, -1]
                                cell = [-1, -1]
                                self.mouse_raw = [-1, -1]

                    # White team
                    if piece_number <= len(self.white_team):
                        cell = self.white_team[piece_number].get_cell()
                        print(str(self.cell) + '  ' + str(cell))
                        if self.cell[0] is not cell[0] or self.cell[1] is not cell[1]:
                                piece = self.white_team[piece_number]
                                print('Move: ' + str(piece.color) + ' - ' + str(piece.type) + ' ' + str(piece.get_cell()) + ' --> ' + str(self.cell))
                                self.white_team[piece_number].move(self.cell[0], self.cell[1])
                                self.cell = [-1, -1]
                                cell = [-1, -1]
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
            if piece.color is 'B':
                self.board.map[cell[1] - 1][cell[0] - 1] = 2
            else:
                self.board.map[cell[1] - 1][cell[0] - 1] = 1

        self.board.print()

