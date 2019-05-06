import pyglet

class piece:
    def __init__(self, color, type, x, y):
        # Ask the type of the piece
        self.type = type
        self.x = x
        self.y = y
        self.color = color

# Function that return the right image for the type and color
def load_image(color, type):
    image: None
    if color is 'W':
        if type is 'Bishop':
            image = pyglet.image.load("C:/Users/aless/Documents/Python/2D_games/Chess/resources/icons8-alfiere-50.png")
            return image
        elif type is 'Horse':
            image = pyglet.image.load("C:/Users/aless/Documents/Python/2D_games/Chess/resources/icons8-cavalllo-50.png")