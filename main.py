from Ship.Offensive.Battleship import Battleship
from Ship.Offensive.Cruiser import Cruiser
from Ship.Offensive.Destroyer import Destroyer

from Ship.Support.Cargo import Cargo
from Ship.Support.Mecha import Mecha
from Ship.Support.Refuel import Refuel

from Grid.Grid import Grid

import random


def main():

	print("TOTETETE\n\n\n")
	assault_list = []
	for i in range (0, 3):
		randy = random.randint(0, 2)
		assault = None
		if randy == 0:
			assault = Battleship()
		elif randy == 1:
			assault = Cruiser()
		else:
			assault = Destroyer()
		assault_list.append(assault)

	support_list = []
	for i in range (0, 3):
		randy = random.randint(0, 2)
		support = None
		if randy == 0:
			support = Cargo()
		elif randy == 1:
			support = Mecha()
		else:
			support = Refuel()
		support = Refuel()
		support_list.append(support)


	map = Grid(4, 8)

	map.print()
	print('\n\n')
	print('---------------------------')
	print('POPULATE-------------------')
	print('---------------------------')
	
	map.populate(assault_list, support_list)
	map.print()

	print('\n\n')
	print('---------------------------')
	print('ALGO-----------------------')
	print('---------------------------')
	
	map.algo()
	map.print()

main()