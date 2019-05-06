import pyglet


# TODO: finish to work on the piece class
# TODO: Get the mouse click
# TODO: Create a movement system

class piece:
    def __init__(self, color, type, x, y):
        # Ask the type of the piece
        self.type = type
        self.position = get_position(x, y)    # y = letter es. 'A'
        self.color = color

        # Create Sprite
        image = load_image(self.color, self.type)
        self.sprite = pyglet.sprite.Sprite(image, x=self.position[0], y=self.position[1])

    def draw(self):
        self.sprite.draw()

    def update(self):
        pass


# Get relative position
def get_position(x, y):
    # position = [x, y]
    position = []

    # 'x' axis
    if x is 1:
        position.append(50)
    elif x is 2:
        position.append(100)
    elif x is 3:
        position.append(150)
    elif x is 4:
        position.append(200)
    elif x is 5:
        position.append(250)
    elif x is 6:
        position.append(300)
    elif x is 7:
        position.append(350)
    elif x is 8:
        position.append(400)

    # 'y' axis

    if y is 'A':
        position.append(400)
    elif y is 'B':
        position.append(350)
    elif y is 'C':
        position.append(300)
    elif y is 'D':
        position.append(250)
    elif y is 'E':
        position.append(200)
    elif y is 'F':
        position.append(150)
    elif y is 'G':
        position.append(100)
    elif y is 'H':
        position.append(50)

    return position


# Function that return the right image for the type and color
def load_image(color, type):
    image: pyglet.image

    # White
    if color is 'W':
        if type is 'Bishop':
            image = pyglet.image.load("C:/Users/aless/Documents/Python/2D_games/Chess/resources/icons8-alfiere-50.png")
            return image
        elif type is 'Horse':
            image = pyglet.image.load("C:/Users/aless/Documents/Python/2D_games/Chess/resources/icons8-cavalllo-50.png")
        elif type is 'Pawn':
            image = pyglet.image.load("C:/Users/aless/Documents/Python/2D_games/Chess/resources/icons8-pedone-50.png")
        elif type is 'King':
            image = pyglet.image.load("C:/Users/aless/Documents/Python/2D_games/Chess/resources/icons8-re-50.png")
        elif type is 'Queen':
            image = pyglet.image.load("C:/Users/aless/Documents/Python/2D_games/Chess/resources/icons8-regina-50.png")
        elif type is 'Tower':
            image = pyglet.image.load("C:/Users/aless/Documents/Python/2D_games/Chess/resources/icons8-torre-50.png")
        else:
            print("Wrong type")

    # Black
    elif color is 'B':
        if type is 'Bishop':
            image = pyglet.image.load("C:/Users/aless/Documents/Python/2D_games/Chess/resources/icons8-alfiere-filled-50.png")
            return image
        elif type is 'Horse':
            image = pyglet.image.load("C:/Users/aless/Documents/Python/2D_games/Chess/resources/icons8-cavalllo-filled-50.png")
        elif type is 'Pawn':
            image = pyglet.image.load("C:/Users/aless/Documents/Python/2D_games/Chess/resources/icons8-pedone-filled-50.png")
        elif type is 'King':
            image = pyglet.image.load("C:/Users/aless/Documents/Python/2D_games/Chess/resources/icons8-re-filled-50.png")
        elif type is 'Queen':
            image = pyglet.image.load("C:/Users/aless/Documents/Python/2D_games/Chess/resources/icons8-regina-filled-50.png")
        elif type is 'Tower':
            image = pyglet.image.load("C:/Users/aless/Documents/Python/2D_games/Chess/resources/icons8-torre-filled-50.png")
        else:
            print("Wrong type")

    # Error Check
    else:
        print("Wrong color")

    return image
