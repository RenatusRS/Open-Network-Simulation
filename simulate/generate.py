import numpy as np
from parameters import DiscProbabiltiy, Perforamcnes, ProcessorProbability
from simulate.Job import Job
from simulate.components.Active import Active
from simulate.components.Component import Component
from simulate.components.Schema import Schema
from simulate.components.Spreader import Spreader


def generate_jobs(total_time, average_time):
	event_times = []
	time = 0.0

	while time < total_time:
		time_interval = np.random.exponential(scale=average_time)
		
		time += time_interval
		
		event_times.append(time)    

	if event_times[-1] > total_time:
		event_times.pop()
		
	jobs = [Job(event, f"Job {ind}") for ind, event in enumerate(event_times)]
	
	return jobs

def generate_scheme(number_of_disks) -> Schema:
	processor = Active("Processor", Perforamcnes.Sp.value)
	
	system_disk_1 = Active("System Disk 1", Perforamcnes.Sd1.value)
	system_disk_2 = Active("System Disk 2", Perforamcnes.Sd2.value)
	system_disk_3 = Active("System Disk 3", Perforamcnes.Sd3.value)
	
	user_disks = [Active(f"User Disk {index + 1}", Perforamcnes.SdK.value) for index in range(number_of_disks)]
	
	user_disks_spreader = Spreader("User Disk Spreader")
	
	for user_disk in user_disks:
		user_disks_spreader.addTarget(user_disk, ProcessorProbability.SdK.value)
	
	processor_spreader = Spreader("Processor Spreader")
	processor_spreader.addTarget(processor, ProcessorProbability.Processor.value)
	processor_spreader.addTarget(system_disk_1, ProcessorProbability.Sd1.value)
	processor_spreader.addTarget(system_disk_2, ProcessorProbability.Sd2.value)
	processor_spreader.addTarget(system_disk_3, ProcessorProbability.Sd3.value)
	processor_spreader.addTarget(user_disks_spreader, ProcessorProbability.SdK.value)
	
	processor.setTarget(processor_spreader)
	
	system_disk_spreader = Spreader("System Disk Spreader")
	system_disk_spreader.addTarget(processor, DiscProbabiltiy.Processor.value)
	system_disk_spreader.addTarget(user_disks_spreader, DiscProbabiltiy.SdK.value)
	
	system_disk_1_spreader = Spreader("System Disk 1 Spreader")
	system_disk_1_spreader.addTarget(system_disk_spreader, DiscProbabiltiy.SdK.value + DiscProbabiltiy.Processor.value)
	system_disk_1_spreader.addTarget(system_disk_1, DiscProbabiltiy.Repeat.value)
	
	system_disk_1.setTarget(system_disk_1_spreader)
	
	system_disk_2_spreader = Spreader("System Disk 2 Spreader")
	system_disk_2_spreader.addTarget(system_disk_spreader, DiscProbabiltiy.SdK.value + DiscProbabiltiy.Processor.value)
	system_disk_2_spreader.addTarget(system_disk_2, DiscProbabiltiy.Repeat.value)
	
	system_disk_2.setTarget(system_disk_2_spreader)
	
	system_disk_3_spreader = Spreader("System Disk 3 Spreader")
	system_disk_3_spreader.addTarget(system_disk_spreader, DiscProbabiltiy.SdK.value + DiscProbabiltiy.Processor.value)
	system_disk_3_spreader.addTarget(system_disk_3, DiscProbabiltiy.Repeat.value)
	
	system_disk_3.setTarget(system_disk_3_spreader)
	
	
	scheme = Schema()
	
	scheme.add(processor)
	scheme.add(system_disk_1)
	scheme.add(system_disk_2)
	scheme.add(system_disk_3)
	scheme.add(user_disks_spreader)
	scheme.add(processor_spreader)
	scheme.add(system_disk_spreader)
	scheme.add(system_disk_1_spreader)
	scheme.add(system_disk_2_spreader)
	scheme.add(system_disk_3_spreader)
	
	for user_disk in user_disks:
		scheme.add(user_disk)
		
	scheme.set_entry_point(processor)
	
	return scheme
