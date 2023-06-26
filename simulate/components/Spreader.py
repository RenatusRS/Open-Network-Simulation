import random

from simulate.components.Component import Component
from util import ifPrint


class Spreader(Component):
	def __init__(self, name: str):
		super().__init__(name)
		
		self._targets = []
		self._weights = []
		
		self._spreads = {}

		
	def addTarget(self, target: Component, weight: int):
		self._targets.append(target)
		self._weights.append(weight)
		self._spreads[target] = 0
		
	def add(self, job):
		target = random.choices(
				self._targets,
				weights=self._weights
			)[0]
		
		self._spreads[target] += 1
			
		ifPrint(f"{job} {self} -> {target}")
			
		target.add(job)
		
	def print(self):
		print(f"{self.name} -> [Total: {sum(self._spreads.values())}] {self._spreads}")
		