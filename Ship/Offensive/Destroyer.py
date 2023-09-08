from .Offensive import OffensiveBase

class Destroyer(OffensiveBase):

	_GunAmount = 6


	_MaxShield = 150
	_MaxHealth = 150

	def Icon(self):
		return 'D'