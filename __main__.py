import pyglet
from board import board
from pieces import piece
from logic import Game


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
        self.game = Game()

    def on_draw(self):
        self.clear()

        # Draw board and pieces
        self.board.draw()
        self.game.draw()

    def update(self, dt):
        pass


if __name__ == "__main__":
    window = Game_Window()
    pyglet.clock.schedule_interval(window.update, window.frame_rate)
    pyglet.app.run()

