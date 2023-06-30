import multiprocessing


class Counter(object):
	
	def __init__(self, initval=0):
		self.val = multiprocessing.Value('i', initval)


	def increment(self, n=1):
		with self.val.get_lock():
			self.val.value += n
			return self.val.value
			
			
	def decrement(self, n=1):
		with self.val.get_lock():
			self.val.value -= n
			return self.val.value


	@property
	def value(self):
		return self.val.value
	