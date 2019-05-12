import pyglet

# Dependencies
from pyglet.window import  key, mouse

# External classes
from game import Game

print('Chess game by Alessio Taranto\n')

class Game_Window(pyglet.window.Window):
    def __init__(self):
        super(Game_Window, self).__init__()

        # Window setup
        self.frame_rate = 1 / 60.0
        self.set_size(500, 500)
        self.set_location(200, 50)
        self.set_caption('Chess')

        # Declare the board
        self.game = Game()

    def on_draw(self):
        self.clear()

        # Draw board and pieces
        self.game.draw()

    def update(self, dt):
        self.game.update()

    def on_key_press(self, symbol, modifiers):
        if symbol is key.U:
            self.game.update_board()

    def on_mouse_press(self, x, y, button, modifiers):
        if button is mouse.LEFT:
            self.game.mouse_select(x, y)


if __name__ == "__main__":
    window = Game_Window()
    pyglet.clock.schedule_interval(window.update, window.frame_rate)
    pyglet.app.run()

