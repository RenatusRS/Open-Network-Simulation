class Job:
	def __init__(self, time, name: str):
		self.name = name
		self.start_time = time
		self.current_time = time
	
	def __repr__(self) -> str:
		return f"[{self.current_time:.16f}] ({self.name})"
	