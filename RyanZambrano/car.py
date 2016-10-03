class Car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		if price > 10000:
			self.tax = '0.15'
		else:
			self.tax = '0.12'
		self.display_all()
	def display_all(self):
		print 'Price:', self.price
		print 'Speed:', self.speed
		print 'Fuel:', self.fuel
		print 'Mileage:', self.mileage
		print 'Tax:', self.tax

car1 = Car(10001, '200mph', 'Full', '20mpg')
car1 = Car(200, '65mph', 'Empty', '10mpg')
car1 = Car(60000, '200mph', 'Full', '27mpg')
car1 = Car(70000, '150mph', 'Full', '50mpg')
car1 = Car(1000, '100mph', 'Kinda Full', '15mpg')
car1 = Car(35000, '135mph', 'Full', '35mpg')