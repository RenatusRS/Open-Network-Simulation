from typing import List
import numpy as np
import generate as gen

from simulation.Active import Active
from simulation.Job import Job


class Schema:	
	
	def __init__(self):
		self.active_components: List[Active] = []
		self.passive_components = []
		self.components = []
		
		self._entry_point: Active = Active("Entry Point", 0)
		self.add(self._entry_point)
		
		
	def add(self, component):
		component_list = self.active_components if isinstance(component, Active) else self.passive_components
		
		component_list.append(component)
		self.components.append(component)


	def set_entry_point(self, component):
		self._entry_point.setTarget(component)
		
		
	def simulate(self, jobs):
		self.jobs: List[Job] = jobs
		
		for job in jobs:
			self._entry_point.add(job)
		
		while True:
			component_passive = min(self.passive_components, key=lambda component: component.get_next_event_time())
			component_active: Active = min(self.active_components, key=lambda component: component.get_next_event_time())
			
			component = component_passive if component_passive.get_next_event_time() <= component_active.get_next_event_time() else component_active
			
			if component.get_next_event_time() == float("inf"):
				break
			
			component.tick()
			
	
	def get_results(self, r, K):
		resources = [component for component in self.active_components if component.name != "Entry Point"]
	
		total_runtime = max([job.current_time for job in self.jobs])
	
		utilization =     { resource.name:  resource.processed_time                          / total_runtime for resource in resources }
		throughput =      { resource.name:  resource.processed_count                         / total_runtime for resource in resources }
		processing_time = { resource.name: (resource.waiting_time + resource.processed_time) / total_runtime for resource in resources }
	
		response_time = np.mean([job.current_time - job.start_time for job in self.jobs])
		
		result = {
			"response_time": response_time,
			
			"utilization": utilization,
			"throughput": throughput,
			"processing_time": processing_time,
			
			"r": r,
			"K": K
		}
		
		return result
	