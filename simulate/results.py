from simulate.Job import Job
from simulate.components.Active import Active
from simulate.components.Component import Component

import numpy as np


def get_results():
	jobs = Job.jobs
	resources = [component for component in Component.components if isinstance(component, Active)]
	
	total_runtime = max([job.current_time for job in jobs])
	
	utilization = [{ resource, resource.processing_time / total_runtime } for resource in resources]
	
	utilization_average = np.mean([resource.processing_time / total_runtime for resource in resources])
	
	job_time_average = np.mean([job.current_time - job.start_time for job in jobs])
	
	