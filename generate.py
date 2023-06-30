import numpy as np
from parameters import DiscProbabiltiy, ProcessingSpeed, ProcessorProbability
from simulation.Active import Active
from simulation.Job import Job
from simulation.Schema import Schema
from simulation.Spreader import Spreader


def generate_jobs(total_time, throughput):
	job_num = np.random.poisson(throughput * total_time)
	event_times = np.cumsum(np.random.exponential(1 / throughput, job_num))
		
	jobs = [Job(event, f"Job {ind}") for ind, event in enumerate(event_times)]
	
	return jobs


def generate_scheme(number_of_disks) -> Schema:
	processor     = Active("Processor", ProcessingSpeed.Processor.value)
	
	system_disk_1 = Active("System Disk 1", ProcessingSpeed.SystemDisk1.value)
	system_disk_2 = Active("System Disk 2", ProcessingSpeed.SystemDisk2.value)
	system_disk_3 = Active("System Disk 3", ProcessingSpeed.SystemDisk3.value)
	
	user_disks   = [Active(f"User Disk {index + 1}", ProcessingSpeed.UserDisk.value) for index in range(number_of_disks)]
	
	user_disks_spreader = Spreader("User Disk Spreader")
	
	for user_disk in user_disks:
		user_disks_spreader.addTarget(user_disk, ProcessorProbability.UserDisk.value)
	
	processor_spreader = Spreader("Processor Spreader")
	processor_spreader.addTarget(processor, ProcessorProbability.Processor.value)
	processor_spreader.addTarget(system_disk_1, ProcessorProbability.SystemDisk1.value)
	processor_spreader.addTarget(system_disk_2, ProcessorProbability.SystemDisk2.value)
	processor_spreader.addTarget(system_disk_3, ProcessorProbability.SystemDisk3.value)
	processor_spreader.addTarget(user_disks_spreader, ProcessorProbability.UserDisk.value)
	
	processor.setTarget(processor_spreader)
	
	system_disk_spreader = Spreader("System Disk Spreader")
	system_disk_spreader.addTarget(processor, DiscProbabiltiy.Processor.value)
	system_disk_spreader.addTarget(user_disks_spreader, DiscProbabiltiy.UserDisk.value)
	
	system_disk_1_spreader = Spreader("System Disk 1 Spreader")
	system_disk_1_spreader.addTarget(system_disk_spreader, DiscProbabiltiy.UserDisk.value + DiscProbabiltiy.Processor.value)
	system_disk_1_spreader.addTarget(system_disk_1, DiscProbabiltiy.Self.value)
	
	system_disk_1.setTarget(system_disk_1_spreader)
	
	system_disk_2_spreader = Spreader("System Disk 2 Spreader")
	system_disk_2_spreader.addTarget(system_disk_spreader, DiscProbabiltiy.UserDisk.value + DiscProbabiltiy.Processor.value)
	system_disk_2_spreader.addTarget(system_disk_2, DiscProbabiltiy.Self.value)
	
	system_disk_2.setTarget(system_disk_2_spreader)
	
	system_disk_3_spreader = Spreader("System Disk 3 Spreader")
	system_disk_3_spreader.addTarget(system_disk_spreader, DiscProbabiltiy.UserDisk.value + DiscProbabiltiy.Processor.value)
	system_disk_3_spreader.addTarget(system_disk_3, DiscProbabiltiy.Self.value)
	
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


def generate_probability_matrix(number_of_disks):
	probability_matrix = np.array([
		[ProcessorProbability.Processor.value, ProcessorProbability.SystemDisk1.value, ProcessorProbability.SystemDisk2.value, ProcessorProbability.SystemDisk3.value],
		[DiscProbabiltiy.Processor.value     , DiscProbabiltiy.Self.value            , 0                                     , 0                                     ],
		[DiscProbabiltiy.Processor.value     , 0                                     , DiscProbabiltiy.Self.value            , 0                                     ],
		[DiscProbabiltiy.Processor.value     , 0                                     , 0                                     , DiscProbabiltiy.Self.value            ],
	])
	
	disk_probability = DiscProbabiltiy.UserDisk.value / number_of_disks
	
	disk_probability_column = np.array([[disk_probability] * number_of_disks] * 4)
	probability_matrix = np.append(probability_matrix, disk_probability_column, axis=1)
	
	zero_rows = np.array([[0] * (4 + number_of_disks)] * number_of_disks)
	probability_matrix = np.append(probability_matrix, zero_rows, axis=0)
	
	return probability_matrix
	

def generate_performance_vector(number_of_disks):
	performance_vector = np.array(
			[
				ProcessingSpeed.Processor.value,
				ProcessingSpeed.SystemDisk1.value,
				ProcessingSpeed.SystemDisk2.value,
				ProcessingSpeed.SystemDisk3.value
			] + [ProcessingSpeed.UserDisk.value] * number_of_disks
		)
	
	return performance_vector

def generate_resource_list():
	return ["Processor", "System Disk 1", "System Disk 2", "System Disk 3", "User Disk"]