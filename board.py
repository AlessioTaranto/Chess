import pyglet


class Board:
    def __init__(self):
        # Loading the image of the board and creating a sprite
        board_image = pyglet.image.load("C:/Users/aless/Documents/Python/2D_games/Chess/resources/board.png")
        self.board_sprite = pyglet.sprite.Sprite(board_image, x=0, y=0)

        # Logic (0 = empty, 1 = white, 2 = black)
        self.map = []
        self.clear()

    def clear(self):
        self.map = [[0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0]]

    def print(self):
        print('\nBoard: ')
        for cell in self.map:
            print(*cell)

    def draw(self):
        self.board_sprite.draw()

    def update(self):
        pass
