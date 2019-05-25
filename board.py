import pyglet
from cell import Cell


# This Class manges the board function so the game has a map
class Board:
    def __init__(self):
        # Loading the image of the board and creating a sprite
        board_image = pyglet.image.load("C:/Users/aless/Documents/Python/2D_games/Chess/resources/board.png")
        self.board_sprite = pyglet.sprite.Sprite(board_image, x=0, y=0)

        # Logic map.data (0 = empty, 1 = white, 2 = black)
        self.map = [[Cell(1, 1), Cell(1, 2), Cell(1, 3), Cell(1, 4), Cell(1, 5), Cell(1, 6), Cell(1, 7), Cell(1, 8)],
                    [Cell(2, 1), Cell(2, 2), Cell(2, 3), Cell(2, 4), Cell(2, 5), Cell(2, 6), Cell(2, 7), Cell(2, 8)],
                    [Cell(3, 1), Cell(3, 2), Cell(3, 3), Cell(3, 4), Cell(3, 5), Cell(3, 6), Cell(3, 7), Cell(3, 8)],
                    [Cell(4, 1), Cell(4, 2), Cell(4, 3), Cell(4, 4), Cell(4, 5), Cell(4, 6), Cell(4, 7), Cell(4, 8)],
                    [Cell(5, 1), Cell(5, 2), Cell(5, 3), Cell(5, 4), Cell(5, 5), Cell(5, 6), Cell(5, 7), Cell(5, 8)],
                    [Cell(6, 1), Cell(6, 2), Cell(6, 3), Cell(6, 4), Cell(6, 5), Cell(6, 6), Cell(6, 7), Cell(6, 8)],
                    [Cell(7, 1), Cell(7, 2), Cell(7, 3), Cell(7, 4), Cell(7, 5), Cell(7, 6), Cell(7, 7), Cell(7, 8)],
                    [Cell(8, 1), Cell(8, 2), Cell(8, 3), Cell(8, 4), Cell(8, 5), Cell(8, 6), Cell(8, 7), Cell(8, 8)]]

    def draw(self):
        self.board_sprite.draw()
        for x in range(8):
            for y in range(8):
                if self.map[y][x].isSelected is True:
                    self.map[y][x].draw()

    def clear(self):
        for x in range(8):
            for y in range(8):
                self.map[y][x].data = 0
                self.map[y][x].isSelected = False

    # Function used to highlight a cell
    def highlight_cell(self, x, y):
        pass

    # A function to get a cell position for the pieces movements
    @staticmethod
    def find_cell(mouse_x, mouse_y):
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

    # Print the map on the terminal using 'U'
    def print(self):
        print('\Board map: ')
        data = get_data(self.map)
        text = ' '
        for x in range(8):
            for y in range(8):
                i = x + (y * 8)
                text += (str(data[i]) + ' ')
            print(text)
            text = ' '


# Function used to get all data from the map in a single list, used
def get_data(map):
    data = []
    for x in range(8):
        for y in range(8):
            data.append(map[7 - y][ x].data)
    return data


