import random

from simulate.components.Component import Component
from util import ifPrint


class Spreader(Component):
	def __init__(self, name: str):
		super().__init__(name)
		
		self._targets = []

		
	def addTarget(self, target: Component, weight: int):
		self._targets.append((target, weight))
		
	def add(self, job):
		target = random.choices(
				[target for target, _ in self._targets],
				[weight for _, weight in self._targets]
			)[0]
			
		ifPrint(f"{job} {self} -> {target}")
			
		target.add(job)
		