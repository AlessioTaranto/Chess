import pyglet
from board import board
from pieces import piece

# TODO: create pawn class and create the images


class Game_Window(pyglet.window.Window):
    def __init__(self):
        super(Game_Window, self).__init__()

        # Window setup
        self.frame_rate = 1 / 60.0
        self.set_size(500, 500)
        self.set_location(200, 50)
        self.set_caption('Chess')

        # Declare the board
        self.board = board()
        self.testpiece = piece('B', 'Pawn', 8, 'A')

    def on_draw(self):
        self.clear()
        self.board.draw()
        self.testpiece.draw()

    def update(self, dt):
        pass


if __name__ == "__main__":
    window = Game_Window()
    pyglet.clock.schedule_interval(window.update, window.frame_rate)
    pyglet.app.run()

