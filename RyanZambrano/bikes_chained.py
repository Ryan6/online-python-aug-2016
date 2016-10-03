class Bike(object):
	def __init__(self, price, max_speed, miles):
		self.price = price
		self.max_speed = max_speed
		self.miles = miles
	def displayInfo(self):
		print 'Price:    ', self.price
		print 'Max Speed:', self.max_speed
		print 'Miles:    ', self.miles
		return self
	def ride(self):
		print 'riding...'
	 	self.miles += 10
	 	return self
	def reverse(self):
		if(self.miles >= 5):
			print 'reversing...'
			self.miles -=5
		return self

bike1 = Bike(200, "25mph", 0)
bike2 = Bike(300, "35mph", 0)
bike3 = Bike(400, "45mph", 0)

print 'Bike 1'
print '------'
bike1.ride().ride().ride().reverse().displayInfo()

print '\nBike 2'
print '------'
bike2.ride().ride().reverse().reverse().displayInfo()

print '\nBike 3'
print '------'
bike3.reverse().reverse().displayInfo()