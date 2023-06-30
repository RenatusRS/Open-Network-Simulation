import copy
import numpy as np
from generate import generate_performance_vector, generate_probability_matrix, generate_resource_list
from parameters import Variables


def analyze():
	print("Analysis started")
	
	results = dict()
	
	for number_of_disks in Variables.K.value:
		odnos_protoka = odredi_protok(number_of_disks)
		
		a_max, critical_resource = odredi_granicnu_vrednost(number_of_disks, odnos_protoka)
		
		parameters = odredi_parametre_jackson(number_of_disks, odnos_protoka, a_max)
		
		results[number_of_disks] = {
			"odnos_protoka": odnos_protoka,
			"a_max": a_max,
			"critical_resource": critical_resource,
			"parameters": parameters
		}	
		
	print("Analysis completed")
	
	return results
	

def odredi_protok(number_of_disks: int):
	probability_matrix = generate_probability_matrix(number_of_disks)
	
	probability_matrix = probability_matrix.transpose()
	
	identity = np.identity(probability_matrix.shape[0])
	
	probability_matrix = identity - probability_matrix
	
	probability_matrix = np.linalg.inv(probability_matrix)
	
	first_column = np.zeros(probability_matrix.shape[0])
	first_column[0] = 1
	
	first_column = np.dot(probability_matrix, first_column)
	
	return first_column


def odredi_granicnu_vrednost(number_of_disks: int, odnos_protoka: np.ndarray):
	performances = generate_performance_vector(number_of_disks)
	
	utilizations = odnos_protoka * performances
	
	critical_resource_index = np.argmax(utilizations)
	
	max_a = 1 / (performances[critical_resource_index] * odnos_protoka[critical_resource_index])
	
	critical_resource = "Processor" if critical_resource_index == 0 else f"System Disk {critical_resource_index}" if critical_resource_index <= 3 else f"User Disk {critical_resource_index - 3}"
	
	return max_a, critical_resource
	

def odredi_parametre_jackson(number_of_disks: int, odnosi_protoka: np.ndarray, a_max: float):
	results = dict()
	
	for r in Variables.r.value:
		X = copy.deepcopy(odnosi_protoka)
		
		X *= a_max * r
		
		performances = generate_performance_vector(number_of_disks)
		
		U = X * performances
		
		J = U / (1 - U)
		
		T = J / X
		
		T_OVERALL = np.sum(odnosi_protoka * T)
		
		resources = generate_resource_list()
		
		results[r] = {
			"X": {resource: X[index] for index, resource in enumerate(resources)},
			"U": {resource: U[index] for index, resource in enumerate(resources)},
			"J": {resource: J[index] for index, resource in enumerate(resources)},
			"T": {resource: T[index] for index, resource in enumerate(resources)},
			"T_OVERALL": T_OVERALL
		}
	
	return results
