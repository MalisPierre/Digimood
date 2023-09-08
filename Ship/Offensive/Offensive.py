from ..Ship import ShipBase

class OffensiveBase(ShipBase):

	_GunAmount = 0

	def Fire(self):
		return self._GunAmount

	def IsAttack(self):
		return True