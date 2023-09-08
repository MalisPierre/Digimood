import random


class Cell():
	_ship = None

	def Add_Ship(self, Ship):
		self._ship = Ship

	def value(self):
		if self._ship == None:
			return '.'
		else:
			return self._ship.Icon()

class Pair():
	_offensive = None
	_defensive = None

class Grid():

	_data = []#[][] of Cells
	_width = 0
	_heigth = 0
	_offensive_ship = []
	_support_ship = []
	_ship_list = []

	def __init__(self, width=100, heigth=100):
		print("CREATING GRID [" + str(width) + "][" + str(heigth) + ']')
		self._width = width
		self._heigth = heigth

		self._data = []
		for i in range (0, self._width):
			line = []
			for j in range(0, self._heigth):
				new_cell = Cell()
				line.append(new_cell)
			self._data.append(line)

	def print(self):
		counter1 = 0
		while counter1 < self._width:
			counter2 = 0
			print('\n')
			while counter2 < self._heigth:
				print(self._data[counter1][counter2].value(), end="")
				counter2 = counter2 + 1
			counter1 = counter1 + 1


	def populate(self, offensive_ship, support_ship):
		available = self._width * self._heigth


		ship_list = offensive_ship + support_ship
		for i in range (0, len(ship_list)):
			target = random.randint(0, available - 1)
			target_counter = 0
			for a in range (0, self._width):
				for b in range(0, self._heigth):
					if self._data[a][b]._ship == None:
						if target_counter == target:
							line_offset = a
							modulo = b
						target_counter = target_counter + 1
						# PAS OPTIMISE DU TOUT MAIS EVITE DE TOMBER PLUSIEURS FOIS SUR LA MEME CASE, VOIR LE COMPORTEMENT DE BREAK ect POUR PLUS OPTI
			

			self._data[line_offset][modulo].Add_Ship(ship_list[i])
			ship_list[i].coordinates(line_offset, modulo)
			available = available - 1

		self._offensive_ship = offensive_ship
		self._support_ship = support_ship
		self._ship_list = ship_list


	# INT DISTANCE BETWEEN 2 COORDZ
	def get_distance(self, x1, y1, x2, y2):
		x_offset = 0
		y_offset = 0
		if x1 >= x2:
			x_offset = x1 - x2
		else:
			x_offset = x2 - x1

		if y1 >= y2:
			y_offset = y1 - y2
		else:
			y_offset = y2 - y1

		return x_offset + y_offset

	def find_closest_support(self, x1, y1):
		# NOT OPTIMIZED BUT SEEMS TO WORK
		min_distance_value = self._width * self._heigth + 1
		min_distance_idx = 0

		for i in range (0, len(self._support_ship)):

			current_distance = 0
			x2 = self._support_ship[i]._width
			y2 = self._support_ship[i]._heigth
			current_distance = self.get_distance(x1, y1, x2, y2)
			if current_distance < min_distance_value:
				min_distance_value = current_distance
				min_distance_idx = i

		return self._support_ship[min_distance_idx]


	def algo(self):
		pairs = []
		#BUILDING PAIRS
		for i in range (0, len(self._offensive_ship)):
			x = self._offensive_ship[i]._width
			y = self._offensive_ship[i]._heigth
			support = self.find_closest_support(x, y)
			paire = Pair()
			paire._offensive = self._offensive_ship[i]
			paire._support = support
			pairs.append(paire)

		for a in range (0, self._width):
			for b in range(0, self._heigth):
				if self._data[a][b]._ship != None and self._data[a][b]._ship.IsSupport() == True:
					self._data[a][b]._ship = None
		#MOVING PAIRS TOGETHER
		for i in range (0, len(pairs)):
			#MOVING SUPPORT CLOSE TO ATTACK
			x = pairs[i]._offensive._width
			y = pairs[i]._offensive._heigth
			if y+1 < self._heigth and self._data[x][y+1]._ship == None:
				self._data[x][y+1].Add_Ship(pairs[i]._support) 
				pairs[i]._support.coordinates(x, y+1)
			elif y > 0 and self._data[x][y-1]._ship == None:
				self._data[x][y-1].Add_Ship(pairs[i]._support) 
				pairs[i]._support.coordinates(x, y-1)
			elif x+1 < self._width and self._data[x+1][y]._ship == None:
				self._data[x+1][y].Add_Ship(pairs[i]._support) 
				pairs[i]._support.coordinates(x+1, y)
			elif  x > 0 and self._data[x-1][y]._ship == None:
				self._data[x-1][y].Add_Ship(pairs[i]._support) 
				pairs[i]._support.coordinates(x-1, y)
