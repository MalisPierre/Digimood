from Ship.Offensive.Battleship import Battleship
from Ship.Offensive.Cruiser import Cruiser
from Ship.Offensive.Destroyer import Destroyer

from Ship.Support.Cargo import Cargo
from Ship.Support.Mecha import Mecha
from Ship.Support.Refuel import Refuel

from Grid.Grid import Grid

import random


def main():

	ship_number = input("Enter the number of ships (min:1, max:100, default:3)") or (3)
	ship_number_int = int(ship_number)

	Xgrid_size = input("Enter the X grid size (min:3, max:100, default:8)") or (8)
	Xgrid_size_int = int(Xgrid_size)

	Ygrid_size = input("Enter the Y grid size (min:3, max:100, default:5)") or (5)
	Ygrid_size_int = int(Ygrid_size)

	assault_list = []
	for i in range (0, ship_number_int):
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
	for i in range (0, ship_number_int):
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


	map = Grid(Ygrid_size_int, Xgrid_size_int)

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