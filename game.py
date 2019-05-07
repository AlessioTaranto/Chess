import pyglet

from pieces import Piece
from board import Board


# Class were all the logic is executed
class Game:
    white_team = None

    def __init__(self):
        # Create board
        self.board = Board()


        # Create pieces
        self.white_tower1 = Piece('W', 'Tower', 1, 'H')
        self.white_horse1 = Piece('W', 'Horse', 2, 'H')
        self.white_bishop1 = Piece('W', 'Bishop', 3, 'H')
        self.white_queen = Piece('W', 'Queen', 4, 'H')
        self.white_king = Piece('W', 'King', 5, 'H')
        self.white_bishop2 = Piece('W', 'Bishop', 6, 'H')
        self.white_horse2 = Piece('W', 'Horse', 7, 'H')
        self.white_tower2 = Piece('W', 'Tower', 8, 'H')
        self.white_pawn1 = Piece('W', 'Pawn', 1, 'G')
        self.white_pawn2 = Piece('W', 'Pawn', 2, 'G')
        self.white_pawn3 = Piece('W', 'Pawn', 3, 'G')
        self.white_pawn4 = Piece('W', 'Pawn', 4, 'G')
        self.white_pawn5 = Piece('W', 'Pawn', 5, 'G')
        self.white_pawn6 = Piece('W', 'Pawn', 6, 'G')
        self.white_pawn7 = Piece('W', 'Pawn', 7, 'G')
        self.white_pawn8 = Piece('W', 'Pawn', 8, 'G')

        self.black_tower1 = Piece('B', 'Tower', 1, 'A')
        self.black_horse1 = Piece('B', 'Horse', 2, 'A')
        self.black_bishop1 = Piece('B', 'Bishop', 3, 'A')
        self.black_queen = Piece('B', 'Queen', 4, 'A')
        self.black_king = Piece('B', 'King', 5, 'A')
        self.black_bishop2 = Piece('B', 'Bishop', 6, 'A')
        self.black_horse2 = Piece('B', 'Horse', 7, 'A')
        self.black_tower2 = Piece('B', 'Tower', 8, 'A')
        self.black_pawn1 = Piece('B', 'Pawn', 1, 'B')
        self.black_pawn2 = Piece('B', 'Pawn', 2, 'B')
        self.black_pawn3 = Piece('B', 'Pawn', 3, 'B')
        self.black_pawn4 = Piece('B', 'Pawn', 4, 'B')
        self.black_pawn5 = Piece('B', 'Pawn', 5, 'B')
        self.black_pawn6 = Piece('B', 'Pawn', 6, 'B')
        self.black_pawn7 = Piece('B', 'Pawn', 7, 'B')
        self.black_pawn8 = Piece('B', 'Pawn', 8, 'B')

        # Create teams
        self.white_team = []
        self.white_team.append(self.white_tower1)
        self.white_team.append(self.white_horse1)
        self.white_team.append(self.white_bishop1)
        self.white_team.append(self.white_queen)
        self.white_team.append(self.white_king)
        self.white_team.append(self.white_bishop2)
        self.white_team.append(self.white_horse2)
        self.white_team.append(self.white_tower2)
        self.white_team.append(self.white_pawn1)
        self.white_team.append(self.white_pawn2)
        self.white_team.append(self.white_pawn3)
        self.white_team.append(self.white_pawn4)
        self.white_team.append(self.white_pawn5)
        self.white_team.append(self.white_pawn6)
        self.white_team.append(self.white_pawn7)
        self.white_team.append(self.white_pawn8)

        # Create teams
        self.black_team = []
        self.black_team.append(self.black_tower1)
        self.black_team.append(self.black_horse1)
        self.black_team.append(self.black_bishop1)
        self.black_team.append(self.black_queen)
        self.black_team.append(self.black_king)
        self.black_team.append(self.black_bishop2)
        self.black_team.append(self.black_horse2)
        self.black_team.append(self.black_tower2)
        self.black_team.append(self.black_pawn1)
        self.black_team.append(self.black_pawn2)
        self.black_team.append(self.black_pawn3)
        self.black_team.append(self.black_pawn4)
        self.black_team.append(self.black_pawn5)
        self.black_team.append(self.black_pawn6)
        self.black_team.append(self.black_pawn7)
        self.black_team.append(self.black_pawn8)

        # TEst
        self.black_king.isSelected = True

        print("Teams created")

    # Draw the pieces
    def draw(self):
        self.board.draw()
        for x in range(len(self.white_team)):
            self.white_team[x].draw()

        for x in range(len(self.black_team)):
            self.black_team[x].draw()

    def update(self):
        pass

    # Select a piece in the board
    def select(self, x, y):
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
        if 50 > x < 100:
            cell_selected.append('H')
        elif 100 > x < 150:
            cell_selected.append('G')
        elif 150 > x < 200:
            cell_selected.append('F')
        elif 200 > x < 250:
            cell_selected.append('E')
        elif 250 > x < 300:
            cell_selected.append('D')
        elif 300 > x < 350:
            cell_selected.append('C')
        elif 350 > x < 400:
            cell_selected.append('B')
        elif 400 > x < 450:
            cell_selected.append('A')

        return cell_selected




