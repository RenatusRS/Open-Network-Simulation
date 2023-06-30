import random

from simulation.Component import Component

class Spreader(Component):
	def __init__(self, name: str):
		super().__init__(name)
		
		self._targets = []
		self._weights = []

		
	def addTarget(self, target: Component, weight: int):
		self._targets.append(target)
		self._weights.append(weight)
		
	def add(self, job):
		target: Component = random.choices(
				self._targets,
				weights=self._weights
			)[0]
			
		target.add(job)
		
		