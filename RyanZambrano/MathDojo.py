'''
class MathDojo(object):
	def __init__(self, total = 0):
		self.total = 0
	def add(self, *n):
		for m in n:
			self.total += m
		return self
	def subtract(self, *n):
		for m in n:
			self.total -= m
		return self
	def result(self):
		print self.total
		return self

MathDojo().add(3).subtract(1, 2, 3).add(5).result()
'''

class MathDojo(object):
	def __init__(self, total = 0):
		self.total = 0
	def add(self, *n):
		for m in n:
			self.total += m
		return self
	def subtract(self, *n):
		for m in n:
			self.total -= m
		return self
	def result(self):
		print self.total
		return self

MathDojo().add(3).subtract(1, 2, 3).add(7).result()