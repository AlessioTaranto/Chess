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

    # A function to update  the map
    def update_board(self):
        for cell_x in range(1, 8):
            for cell_y in range(1, 8):
                for piece in self.white_team:
                    piece_cell = piece.get_cell()
                    if piece_cell[0] == cell_x:
                        if piece_cell[1] == cell_y:
                            self.board.map[cell_y][cell_x] = 1
                        else:
                            self.board.map[cell_y][cell_x] = 0
                    else:
                        self.board.map[cell_y][cell_x] = 0

                for piece in self.black_team:
                    piece_cell = piece.get_cell()
                    if piece_cell[0] == cell_x:
                        if piece_cell[1] == cell_y:
                            self.board.map[cell_y][cell_x] = 2
                        else:
                            self.board.map[cell_y][cell_x] = 0
                    else:
                        self.board.map[cell_y][cell_x] = 0

    def print_board(self):
        print('\nBoard: ')
        for cell in self.board.map:
            print(*cell)

    # Select a piece in the board
    @staticmethod
    def select(x, y):
        # cell selected = [x, y]
        cell_selected = [0, 0]

        # 'x' axis
        if 50 > x < 100:
            cell_selected.append(1)
        elif 100 > x < 150:
            cell_selected.append(2)
        elif 150 > x < 200:
            cell_selected.append(3)
        elif 200 > x < 250:
            cell_selected.append(4)
        elif 250 > x < 300:
            cell_selected.append(5)
        elif 300 > x < 350:
            cell_selected.append(6)
        elif 350 > x < 400:
            cell_selected.append(7)
        elif 400 > x < 450:
            cell_selected.append(8)

        # 'y' axis
        if 50 > y < 100:
            cell_selected.append('H')
        elif 100 > y < 150:
            cell_selected.append('G')
        elif 150 > y < 200:
            cell_selected.append('F')
        elif 200 > y < 250:
            cell_selected.append('E')
        elif 250 > y < 300:
            cell_selected.append('D')
        elif 300 > y < 350:
            cell_selected.append('C')
        elif 350 > y < 400:
            cell_selected.append('B')
        elif 400 > y < 450:
            cell_selected.append('A')

        return cell_selected
