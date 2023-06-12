import random

from simulate.Job import Job
from parameters import UserInput
from simulate.components.Component import Component
from util import ifPrint


class Active(Component):
	def next(self):
		job = self.queue.pop(0)
		job.current_time = max(job.current_time, self.cooldown)
		self.process(job)
		
	def get_next_time(self):
		if len(self.queue) == 0:
			return float("inf")
		
		return max(self.queue[0].current_time, self.cooldown)
	
	def __init__(self, name: str, service_time: int):
		super().__init__(name)
		
		self.queue = []
		self._service_time = service_time
		self._target = None
		self.cooldown = 0
		
		self.processing_time = 0
		
	def add(self, job: Job):
		self.queue.append(job)
		
		
	def setTarget(self, target: Component):
		self._target = target
		
		
	def process(self, job: Job):
		added_time = random.uniform(1 - UserInput.Offset.value, 1 + UserInput.Offset.value) * self._service_time
		
		ifPrint(f"{job} {self} | +{added_time} = [{job.current_time + added_time}]")
		
		job.add_time(added_time)
		self.processing_time += added_time
		
		self.cooldown = job.current_time
		
		if self._target:
			self._target.add(job)
		else:
			job.finished = True
