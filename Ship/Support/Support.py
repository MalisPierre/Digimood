from ..Ship import ShipBase

class SupportBase(ShipBase):


	def ProvideSupport(self):
		raise NotImplementedError()


	def IsSupport(self):
		return True