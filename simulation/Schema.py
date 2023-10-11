from typing import List
import numpy as np

from simulation.Server import Server
from simulation.Job import Job


class Schema:	
	def __init__(self):
		self.servers: List[Server] = []
		self.components = []
		
		self._entry_point: Server = Server("Entry Point", 0)
		self.add(self._entry_point)
		
		
	def add(self, component):
		if isinstance(component, Server):
			self.servers.append(component)
			
		self.components.append(component)


	def set_entry_point(self, component):
		self._entry_point.setTarget(component)
		
		
	def simulate(self, jobs):
		self.jobs: List[Job] = jobs
		
		for job in jobs:
			self._entry_point.add(job)
		
		while True:
			component = min(self.components, key=lambda component: component.get_next_event_time())
			
			if component.get_next_event_time() == float("inf"):
				break
			
			component.tick()
			
	
	def get_results(self, r, K):
		servers = [component for component in self.servers if component.name != "Entry Point"]
	
		total_runtime = max([job.current_time for job in self.jobs])
	
		utilization =     { server.name:  server.processed_time                        / total_runtime for server in servers }
		throughput =      { server.name:  server.processed_count                       / total_runtime for server in servers }
		processing_time = { server.name: (server.waiting_time + server.processed_time) / total_runtime for server in servers }
	
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
