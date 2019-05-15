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

    # A function to get a cell position for the pieces movements
    def find_cell(self, mouse_x, mouse_y):
        debug = False
        pos = [mouse_x, mouse_y]
        cell = [0, 0]
        if debug is True:
            print('-Initial value' + str(pos))

        # x axis
        for x in range(2):
            if pos[x] == 400:
                cell[x] = 8
            elif pos[x] == 350:
                cell[x] = 7
            elif pos[x] == 300:
                cell[x] = 6
            elif pos[x] == 250:
                cell[x] = 5
            elif pos[x] == 200:
                cell[x] = 4
            elif pos[x] == 150:
                cell[x] = 3
            elif pos[x] == 100:
                cell[x] = 2
            elif pos[x] == 50:
                cell[x] = 1
            else:
                print('Wrong position')

        if debug is True:
            print('-Final value:' + str(cell))
        return cell

    def print(self):
        print('\nBoard: ')
        for cell in self.map:
            print(*cell)

    def draw(self):
        self.board_sprite.draw()

    def update(self):
        pass
