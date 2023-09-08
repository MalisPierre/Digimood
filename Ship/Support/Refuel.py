from .Support import SupportBase

class Refuel(SupportBase):

	def ProvideSupport(self):
		print("MOVING FUEL ...")

	def Icon(self):
		return 'R'