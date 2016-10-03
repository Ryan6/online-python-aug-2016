class Animal(object):
	def __init__(self, name, health = 100):
		self.name = name
		self.health = 100
	def walk(self):
		self.health -= 1
		return self
	def run(self):
		self.health -= 5
		return self
	def displayHealth(self):
		if 'Dragon object' in str(self): # probably not the most straightforward way of doing this...
			print 'this is a dragon!'
		print 'Name:', self.name
		print 'Health:', self.health
		return self

Animal('animal').walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
	def __init__(self, name, health = 150):
		super(Dog, self).__init__(self)
		self.name = name
		self.health = 150
	def pet(self):
		self.health += 5
		return self

Dog('dog').walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
	def __init__(self, name, health = 170):
		super(Dragon, self).__init__(self)
		self.name = name
		self.health = 170
	def fly(self):
		self.health += 10
		return self

Dragon('dragon').walk().walk().walk().run().run().fly().fly().displayHealth()