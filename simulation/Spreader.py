from collections import deque
import random
from typing import Deque

from simulation.Component import Component
from simulation.Job import Job

class Spreader(Component):
	def tick(self):
		job = self.queue.popleft()
		self.process(job)
		
		
	def get_next_event_time(self):
		if not self.queue:
			return float("inf")
		
		return self.queue[0].current_time
	
	
	def __init__(self, name: str):
		super().__init__(name)
		
		self._targets = []
		self._weights = []
		
		self.queue: Deque[Job] = deque()

		
	def addTarget(self, target: Component, weight: int):
		self._targets.append(target)
		self._weights.append(weight)
		
		
	def add(self, job: Job):
		self.queue.append(job)
		
		
	def process(self, job: Job):
		target: Component = random.choices(
				self._targets,
				weights=self._weights
			)[0]
			
		target.add(job)
		