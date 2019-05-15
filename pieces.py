import pyglet


class Piece:
    def __init__(self, color, type, x, y):
        # Ask the type of the piece
        self.type = type
        self.cell = [x, y]
        self.position = grid_to_pos(self.cell[0], self.cell[1])
        print('Piece created: ' + str(self.position) + ' // ' + str(self.cell))
        self.color = color

        # Selection Logic
        self.isSelected = False
        image = pyglet.image.load('C:/Users/aless/Documents/Python/2D_games/Chess/resources/selected.png')
        self.selected_sprite = pyglet.sprite.Sprite(image, x=self.position[0], y=self.position[1])

        # Create Sprite
        image = load_image(self.color, self.type)
        self.sprite = pyglet.sprite.Sprite(image, x=self.position[0], y=self.position[1])

    def draw(self):
        self.sprite.draw()
        if self.isSelected is True:
            self.selected_sprite.draw()

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
    if color is 'W':
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
    elif color is 'B':
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
