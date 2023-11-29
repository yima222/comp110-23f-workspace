from __future__ import annotations

class Icecream:
	"""Creates Icecream objects."""
	count: int
	info: str
    
	def __init__(self, count_val: int, info_val: str):
		""""Constructor."""
		self.count = count_val
		self.info = info_val
    
	def __mul__(self, factor: int) -> Icecream:
		count = self.count * factor
		new_info = self.info
		return Icecream(count, new_info)
	
	def rename(self, new_name) -> None:
		self.info = new_name

x: Icecream = Icecream(5, "Praline")
print(x.count)
y: Icecream = x * 3
print(y.count)