import pyglet

from pieces import piece


# Class were all the logic is executed
class Game:
    white_team = None

    def __init__(self):
        # Create pieces
        self.white_tower1 = piece('W', 'Tower', 1, 'H')
        self.white_horse1 = piece('W', 'Horse', 2, 'H')
        self.white_bishop1 = piece('W', 'Bishop', 3, 'H')
        self.white_queen = piece('W', 'Queen', 4, 'H')
        self.white_king = piece('W', 'King', 5, 'H')
        self.white_bishop2 = piece('W', 'Bishop', 6, 'H')
        self.white_horse2 = piece('W', 'Horse', 7, 'H')
        self.white_tower2 = piece('W', 'Tower', 8, 'H')
        self.white_pawn1 = piece('W', 'Pawn', 1, 'G')
        self.white_pawn2 = piece('W', 'Pawn', 2, 'G')
        self.white_pawn3 = piece('W', 'Pawn', 3, 'G')
        self.white_pawn4 = piece('W', 'Pawn', 4, 'G')
        self.white_pawn5 = piece('W', 'Pawn', 5, 'G')
        self.white_pawn6 = piece('W', 'Pawn', 6, 'G')
        self.white_pawn7 = piece('W', 'Pawn', 7, 'G')
        self.white_pawn8 = piece('W', 'Pawn', 8, 'G')

        self.black_tower1 = piece('B', 'Tower', 1, 'A')
        self.black_horse1 = piece('B', 'Horse', 2, 'A')
        self.black_bishop1 = piece('B', 'Bishop', 3, 'A')
        self.black_queen = piece('B', 'Queen', 4, 'A')
        self.black_king = piece('B', 'King', 5, 'A')
        self.black_bishop2 = piece('B', 'Bishop', 6, 'A')
        self.black_horse2 = piece('B', 'Horse', 7, 'A')
        self.black_tower2 = piece('B', 'Tower', 8, 'A')
        self.black_pawn1 = piece('B', 'Pawn', 1, 'B')
        self.black_pawn2 = piece('B', 'Pawn', 2, 'B')
        self.black_pawn3 = piece('B', 'Pawn', 3, 'B')
        self.black_pawn4 = piece('B', 'Pawn', 4, 'B')
        self.black_pawn5 = piece('B', 'Pawn', 5, 'B')
        self.black_pawn6 = piece('B', 'Pawn', 6, 'B')
        self.black_pawn7 = piece('B', 'Pawn', 7, 'B')
        self.black_pawn8 = piece('B', 'Pawn', 8, 'B')

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

    # Draw the pieces
    def draw(self):
        for x in range(len(self.white_team)):
            self.white_team[x].draw()

        for x in range(len(self.black_team)):
            self.black_team[x].draw()




