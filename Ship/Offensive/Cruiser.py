from .Offensive import OffensiveBase

class Cruiser(OffensiveBase):

	_GunAmount = 12

	_MaxShield = 300
	_MaxHealth = 300

	def Icon(self):
		return 'C'