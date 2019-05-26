import pyglet


class Piece:
    def __init__(self, color, type, x, y):
        # Ask the type of the piece
        self.color = color
        self.type = type
        self.cell = [x, y]
        self.position = grid_to_pos(self.cell[0], self.cell[1])
        print('Piece created: ' + str(self.color + self.type) + ' // ' + str(self.position) + ' // ' + str(self.cell))

        # Selection Logic
        self.isSelected = False
        image = pyglet.image.load('C:/Users/aless/Documents/Python/2D_games/Chess/resources/selected.png')
        self.selected_sprite = pyglet.sprite.Sprite(image, x=self.position[0], y=self.position[1])

        # Danger image
        self.inDanger = False
        image = pyglet.image.load('C:/Users/aless/Documents/Python/2D_games/Chess/resources/selected.png')
        self.danger_sprite = pyglet.sprite.Sprite(image, x=self.position[0], y=self.position[1])

        # Create Sprite
        image = load_image(self.color, self.type)
        self.sprite = pyglet.sprite.Sprite(image, x=self.position[0], y=self.position[1])

    def draw(self):
        self.sprite.draw()
        if self.isSelected is True:
            self.selected_sprite.draw()
        elif self.inDanger is True:
            self.danger_sprite.draw()

    def update(self):
        debug = False
        # Update position
        if debug is True:
            print('Update: ' + str(self.position))

        # Set positions
        self.sprite.x = self.position[0]
        self.sprite.y = self.position[1]

        self.selected_sprite.x = self.position[0]
        self.selected_sprite.y = self.position[1]

    # Check the possible cells for the piece to move
    def check_movement(self):
        map = [[0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0]]

        # Get and update the position of the piece
        cell = self.get_cell()

        # Board start from 1
        cell[0] -= 1
        cell[1] -= 1
        map[cell[0]][cell[1]] = 2

        # Function params
        min_cell = 0
        max_cell = 7

        # Check the movement path
        if self.type is 'Tower':
            for i in range(min_cell, max_cell):
                # Top
                if not(cell[0] + i < min_cell or cell[0] + i > max_cell):
                    map[cell[0] + i][cell[1]] = 1
                # Down
                if not(cell[0] - i < min_cell or cell[0] - i > max_cell):
                    map[cell[0] - i][cell[1]] = 1
                # Right
                if not(cell[1] + i < min_cell or cell[1] + i > max_cell):
                    map[cell[0]][cell[1] + i] = 1
                # Left
                if not(cell[1] - i < min_cell or cell[1] - i > max_cell):
                    map[cell[0]][cell[1] - i] = 1

        elif self.type is 'Horse':
            # Top Right
            if not(cell[0] + 1 < min_cell or cell[0] + 1 > max_cell):
                if not(cell[1] + 2 < min_cell or cell[1] + 2 > max_cell):
                    map[cell[0] + 1][cell[1] + 2] = 1
            if not(cell[0] + 2 < min_cell or cell[0] + 2 > max_cell):
                if not(cell[1] + 1 < min_cell or cell[1] + 1 > max_cell):
                    map[cell[0] + 2][cell[1] + 1] = 1
            # Down Right
            if not(cell[0] + 2 < min_cell or cell[0] + 2 > max_cell):
                if not(cell[1] - 1 < min_cell or cell[1] - 1 > max_cell):
                    map[cell[0] + 2][cell[1] - 1] = 1
            if not(cell[0] + 1 < min_cell or cell[0] + 1 > max_cell):
                if not(cell[1]  - 2 < min_cell or cell[1] - 2 > max_cell):
                    map[cell[0] + 1][cell[1] - 2] = 1
            # Top Left
            if not(cell[0] -  1< min_cell or cell[0] - 1 > max_cell):
                if not(cell[1] + 2 < min_cell or cell[1] + 2 > max_cell):
                    map[cell[0] - 1][cell[1] + 2] = 1
            if not(cell[0] - 2 < min_cell or cell[0] - 2 > max_cell):
                if not(cell[1] + 1 < min_cell or cell[1] + 1 > max_cell):
                    map[cell[0] - 2][cell[1] + 1] = 1
            # Down Left
            if not(cell[0] - 1 < min_cell or cell[0] - 1 > max_cell):
                if not(cell[1] - 2 < min_cell or cell[1] - 2 > max_cell):
                    map[cell[0] - 1][cell[1] - 2] = 1
            if not(cell[0] - 2 < min_cell or cell[0] - 2 > max_cell):
                if not(cell[1] - 1 < min_cell or cell[1] - 1 > max_cell):
                    map[cell[0] - 2][cell[1] - 1] = 1

        elif self.type is 'Bishop':
            for i in range(min_cell, max_cell):
                # Top right
                if not(cell[0] + i < min_cell or cell[0] + i > max_cell):
                    if not(cell[1] + i < min_cell or cell[1] + i > max_cell):
                        map[cell[0] + i][cell[1] + i] = 1
                # Down Right
                if not(cell[0] - i < min_cell or cell[0] - i > max_cell):
                    if not(cell[1] + 1 + i < min_cell or cell[1] + i > max_cell):
                        map[cell[0] - i][cell[1] + i] = 1
                # Top Left
                if not(cell[0] + i < min_cell or cell[0] + i > max_cell):
                    if not(cell[1] - i < min_cell or cell[1] - i > max_cell):
                        map[cell[0] + i][cell[1] - i] = 1
                # Down Left
                if not(cell[0] - i < min_cell or cell[0] - i > max_cell):
                    if not(cell[1] - i < min_cell or cell[1] - i > max_cell):
                        map[cell[0] - i][cell[1] - i] = 1

        elif self.type is 'Queen':
            for i in range(min_cell, max_cell):
                # Top
                if not(cell[0] + i < min_cell or cell[0] + i > max_cell):
                    map[cell[0] + i][cell[1]] = 1
                # Down
                if not(cell[0] - i < min_cell or cell[0] - i > max_cell):
                    map[cell[0] - i][cell[1]] = 1
                # Right
                if not(cell[1] + i < min_cell or cell[1] + i > max_cell):
                    map[cell[0]][cell[1] + i] = 1
                # Left
                if not(cell[1] - i < min_cell or cell[1] - i > max_cell):
                    map[cell[0]][cell[1] - i] = 1

                # Top right
                if not(cell[0] + i < min_cell or cell[0] + i > max_cell):
                    if not(cell[1] + i < min_cell or cell[1] + i > max_cell):
                        map[cell[0] + i][cell[1] + i] = 1
                # Down Right
                if not(cell[0] - i < min_cell or cell[0] - i > max_cell):
                    if not(cell[1] + 1 + i < min_cell or cell[1] + i > max_cell):
                        map[cell[0] - i][cell[1] + i] = 1
                # Top Left
                if not(cell[0] + i < min_cell or cell[0] + i > max_cell):
                    if not(cell[1] - i < 0 or cell[1] - i > max_cell):
                        map[cell[0] + i][cell[1] - i] = 1
                # Down Left
                if not(cell[0] - i < min_cell or cell[0] - i > max_cell):
                    if not(cell[1] - i < 0 or cell[1] - i > max_cell):
                        map[cell[0] - i][cell[1] - i] = 1

        elif self.type is 'King':
            # Top
            if not (cell[1] + 1 > max_cell or cell[1] + 1 < min_cell):
                map[cell[0]][cell[1] + 1] = 1
            # Down
            if not(cell[1] > max_cell or cell[1] < min_cell):
                map[cell[0]][cell[1]] = 1
            # Right
            if not(cell[0] + 1 > max_cell or cell[0] + 1 < min_cell):
                map[cell[0] + 1][cell[1]] = 1
            # Left
            if not(cell[0] > max_cell or cell[0] < min_cell):
                map[cell[0]][cell[1]] = 1
            # Top Right
            if not(cell[0] > max_cell or cell[0] < min_cell):
                if not(cell[1] > max_cell or cell[1] < min_cell):
                    map[cell[0]][cell[1]] = 1
            # Top Left
            if not(cell[0] + 1 > max_cell or cell[0] + 1 < min_cell):
                if not(cell[1] > max_cell or cell[1] < min_cell):
                    map[cell[0] + 1][cell[1]] = 1
            # Down left
            if not(cell[0] > max_cell or cell[0] < min_cell):
                if not(cell[1] + 1 > max_cell or cell[1] + 1 < min_cell):
                    map[cell[0]][cell[1] + 1] = 1

            if not(cell[0] + 1 > max_cell or cell[0] + 1 < min_cell):
                if not(cell[1] + 1 > max_cell or cell[1] + 1 < min_cell):
                    map[cell[0] + 1][cell[1] + 1] = 1

        elif self.type is 'Pawn':
            if self.color is 'Black':
                if not(cell[1] < min_cell or cell[1] + 1 > max_cell):
                    map[cell[0]][cell[1] + 1] = 1
            if self.color is 'White':
                if not(cell[1] + 1 < min_cell or cell[1] > max_cell):
                    map[cell[0]][cell[1] - 1] = 1

        return map

    # Return a position [cell_x, cell_y] = es[5, 8]
    def move(self, x, y):
        new_pos = grid_to_pos(x, y)
        self.position = new_pos

    def get_cell(self):
        cell = pos_to_grid(self.position[0], self.position[1])
        return cell

    # Check if the click(x, y) in on top of the piece
    def check_if_clicked(self, x, y):
        if self.position[0] + 50 > x > self.position[0]:
            if self.position[1] + 50 > y > self.position[1]:
                self.isSelected = True


def pos_to_grid(x, y):
    debug = False
    pos = [x, y]
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


def grid_to_pos(x, y):
    pos = [0, 0]
    cell = [x, y]

    for x in range(2):
        if cell[x] == 1:
            pos[x] = 50
        elif cell[x] == 2:
            pos[x] = 100
        elif cell[x] == 3:
            pos[x] = 150
        elif cell[x] == 4:
            pos[x] = 200
        elif cell[x] == 5:
            pos[x] = 250
        elif cell[x] == 6:
            pos[x] = 300
        elif cell[x] == 7:
            pos[x] = 350
        elif cell[x] == 8:
            pos[x] = 400

    return pos


# Function that return the right image for the type and color
def load_image(color, type):
    image: pyglet.image

    # White
    if color is 'White':
        if type is 'Bishop':
            image = pyglet.image.load("C:/Users/aless/Documents/Python/2D_games/Chess/resources/white_bishop.png")
            return image
        elif type is 'Horse':
            image = pyglet.image.load("C:/Users/aless/Documents/Python/2D_games/Chess/resources/white_horse.png")
        elif type is 'Pawn':
            image = pyglet.image.load("C:/Users/aless/Documents/Python/2D_games/Chess/resources/white_pawn.png")
        elif type is 'King':
            image = pyglet.image.load("C:/Users/aless/Documents/Python/2D_games/Chess/resources/white_king.png")
        elif type is 'Queen':
            image = pyglet.image.load("C:/Users/aless/Documents/Python/2D_games/Chess/resources/white_queen.png")
        elif type is 'Tower':
            image = pyglet.image.load("C:/Users/aless/Documents/Python/2D_games/Chess/resources/white_tower.png")
        else:
            print("Wrong type")

    # Black
    elif color is 'Black':
        if type is 'Bishop':
            image = pyglet.image.load("C:/Users/aless/Documents/Python/2D_games/Chess/resources/black_bishop.png")
            return image
        elif type is 'Horse':
            image = pyglet.image.load("C:/Users/aless/Documents/Python/2D_games/Chess/resources/black_horse.png")
        elif type is 'Pawn':
            image = pyglet.image.load("C:/Users/aless/Documents/Python/2D_games/Chess/resources/black_pawn.png")
        elif type is 'King':
            image = pyglet.image.load("C:/Users/aless/Documents/Python/2D_games/Chess/resources/black_king.png")
        elif type is 'Queen':
            image = pyglet.image.load("C:/Users/aless/Documents/Python/2D_games/Chess/resources/black_queen.png")
        elif type is 'Tower':
            image = pyglet.image.load("C:/Users/aless/Documents/Python/2D_games/Chess/resources/black_tower.png")
        else:
            print("Wrong type")

    # Error Check
    else:
        print("Wrong color")

    return image
