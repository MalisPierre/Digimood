from .Offensive import OffensiveBase

class Battleship(OffensiveBase):

	_GunAmount = 24

	_MaxShield = 600
	_MaxHealth = 600

	def Icon(self):
		return 'B'