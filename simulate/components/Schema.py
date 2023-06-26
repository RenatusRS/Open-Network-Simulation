import numpy as np
from simulate.components.Active import Active
from simulate.components.Component import Component


class Schema:	
	def __init__(self):
		self.active_components = []
		self.passive_components = []
		
		self._entry_point: Active = Active("Entry Point", 0)
		self.add(self._entry_point)
		
	def add(self, component):
		if isinstance(component, Active):
			self.active_components.append(component)
		else:
			self.passive_components.append(component)

	def set_entry_point(self, component):
		self._entry_point.setTarget(component)
		
	def simulate(self, jobs):
		self.jobs = jobs
		
		for job in jobs:
			self._entry_point.add(job)
		
		while True:
			component: Active = min(self.active_components, key=lambda component: component.get_next_time())
			
			if component.get_next_time() == float("inf"):
				break
			
			component.next()
			
	
	def get_results(self, r, K):
		resources = [component for component in self.active_components]
	
		total_runtime = max([job.current_time for job in self.jobs])
	
		utilization = [{ resource, resource.processing_time / total_runtime } for resource in resources]
	
		utilization_average = np.mean([resource.processing_time / total_runtime for resource in resources])
	
		job_time_average = np.mean([job.current_time - job.start_time for job in self.jobs])
		
		
		return {
			"total_runtime": total_runtime,
			"utilization": utilization,
			"utilization_average": utilization_average,
			"job_time_average": job_time_average,
			"r": r,
			"K": K
		}