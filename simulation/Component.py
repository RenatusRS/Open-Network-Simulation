from abc import ABC, abstractmethod


class Component(ABC):	
	
	def __init__(self, name: str):
		self.name = name


	@abstractmethod
	def add(self, job):
		pass
		
		
	def __repr__(self) -> str:
		return f"{self.name}"
