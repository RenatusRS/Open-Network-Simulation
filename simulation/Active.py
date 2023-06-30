from collections import deque
from queue import PriorityQueue
from typing import Deque

import numpy as np

from simulation.Component import Component
from simulation.Job import Job


class Active(Component):
	def tick(self):
		job = self.queue.popleft()
		job.current_time = max(job.current_time, self.cooldown)
		self.process(job)
		
	def get_next_event_time(self):
		if not self.queue:
			return float("inf")
		
		return max(self.queue[0].current_time, self.cooldown)
	
	def __init__(self, name: str, service_time: int):
		super().__init__(name)
		
		self.queue: Deque[Job] = deque()
		self._service_time = service_time
		self._target = None
		
		self.cooldown = 0
		self.previous_proccesing_time = 0
		
		self.processed_time = 0
		self.processed_count = 0
		self.average_jobs_in_queue = 0
		
	def add(self, job: Job):
		self.queue.append(job)
		
		
	def setTarget(self, target: Component):
		self._target = target
		
		
	def process(self, job: Job):
		added_time = np.random.exponential(scale=self._service_time) if self._service_time != 0 else 0
		
		self.average_jobs_in_queue += len(self.queue) * (job.current_time - self.previous_proccesing_time)
		
		self.processed_time += added_time
		self.processed_count += 1
		self.previous_proccesing_time = job.current_time
		
		job.current_time += added_time
		
		self.cooldown = job.current_time
		
		if self._target:
			self._target.add(job)
