
class ShipBase():

	_CurrentShield = 0
	_MaxShield = 100

	_CurrentHealth = 0
	_MaxHealth = 100

	def __init__(self):
		self.RegenerateHealth()
		self.RegenerateShield()

	def RegenerateHealth(self):
		self._CurrentHealth = self._MaxHealth

	def RegenerateShield(self):
		self._CurrentShield = self._MaxShield

	def TakeDamage(self, DamageAmount):
		Total_Damage = DamageAmount
		self._CurrentShield = self._CurrentShield - DamageAmount
		if self._CurrentShield <= 0:
			Total_Damage = self._CurrentShield = self._CurrentShield - DamageAmount * -1
			self._CurrentHealth = self._CurrentHealth - Total_Damage
			if self._CurrentHealth <= 0:
				self.Die()

	def Die(self):
		print("I DIE !!!!")

	def Icon(self):
		return '°'#**raise NotImplementedError()

	def IsSupport(self):
		return False

	def IsAttack(self):
		return False

	_width = 0
	_heigth = 0

	def coordinates(self, width, heigth):
		self._width = width
		self._heigth = heigth