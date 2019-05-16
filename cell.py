import pyglet


class Cell:
	def __init__(self, x, y):
		self.cell = [x, y]
		self.data = 0
		self.position = grid_to_pos(self.cell[0], self.cell[1])
		self.isSelected = False

		# Create Sprite
		image = pyglet.image.load('C:/Users/aless/Documents/Python/2D_games/Chess/resources/selected_green.png')
		self.selected = pyglet.sprite.Sprite(image, x=self.position[0], y=self.position[1])

	def highlight(self):
		self.isSelected = True

	def draw(self):
		if self.isSelected is True:
			self.selected.draw()


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
