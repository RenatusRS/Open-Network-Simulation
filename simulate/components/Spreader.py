import random

from simulate.components.Component import Component
from util import ifPrint


class Spreader(Component):
	def __init__(self, name: str):
		super().__init__(name)
		
		self._targets = []
		self._weights = []

		
	def addTarget(self, target: Component, weight: int):
		self._targets.append(target)
		self._weights.append(weight)
		
	def add(self, job):
		target = random.choices(
				self._targets,
				weights=self._weights
			)[0]
			
		ifPrint(f"{job} {self} -> {target}")
			
		target.add(job)
		