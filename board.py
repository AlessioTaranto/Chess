import pyglet

# TODO: make the board as [x][y]


class board:
    def __init__(self):
        # Loading the image of the board and creating a sprite
        board_image = pyglet.image.load("C:/Users/aless/Documents/Python/2D_games/Chess/resources/board.png")
        self.board_sprite = pyglet.sprite.Sprite(board_image, x=0, y=0)

    def draw(self):
        self.board_sprite.draw()

    def update(self):
        pass
