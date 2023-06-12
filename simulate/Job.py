class Job:
	jobs = []
	
	@staticmethod
	def reset():
		Job.jobs = []
    
	def __init__(self, time, name: str):
		self.name = name
		self.start_time = time
		self.current_time = time
		self.finished = False
		
		self.processed_time = 0
		self.processed_count = 0
		
		self.jobs.append(self)
	
	def set_time(self, time):
		self.current_time = time
	
	def add_time(self, time):
		self.current_time += time
		
		self.processed_time += time
		self.processed_count += 1
	
	def __repr__(self) -> str:
		return f"[{self.current_time:.16f}] ({self.name})"