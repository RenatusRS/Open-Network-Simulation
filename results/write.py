import copy
import pprint
import numpy as np

from parameters import Variables

np.set_printoptions(threshold=np.inf)
np.set_printoptions(linewidth=np.inf)

def protoci_analiticki(results: dict):
	columns = [
		"Proccesor",
		"System Disk 1",
		"System Disk 2",
		"System Disk 3",
	] + [f"User Disk {i}" for i in range(1, max(Variables.K.value) + 1)]
	
	column_width = [len(column) for column in columns]
	
	column_width_index = max([len(str(K)) for K in Variables.K.value])
	
	for i in range(len(column_width)):
		mx = column_width[i]
		
		for k, data in results.items():
			mx = max(mx, len(str(data["odnos_protoka"][i]))) if i < len(data["odnos_protoka"]) else mx
		
		column_width[i] = max(column_width[i], mx)
	
	with open("results/protoci_analiticki.txt", "w") as file:
		row = f"{'K':>{column_width_index}} " + " ".join([f"{column:>{column_width[i]}}" for i, column in enumerate(columns)])
		
		file.write(row + "\n")
		
		for K in Variables.K.value:
			row = f"{K:>{column_width_index}} "
			
			for i in range(len(results[K]["odnos_protoka"])):
				row += f"{results[K]['odnos_protoka'][i]:>{column_width[i]}.8f} "
			
			file.write(row + "\n")
			
	print("Generated protoci_analiticki.txt")
		
		
strings = ["Processor", "System Disk 1", "System Disk 2", "System Disk 3", "User Disk 1", "User Disk 2", "User Disk 3", "User Disk 4", "User Disk 5"]
		
def convert_numpy_to_list(data):
	if isinstance(data, np.ndarray):
		data = data.tolist()
		
		data = [f"{string}: {value}" for string, value in zip(strings, data)]
	
		return data
	elif isinstance(data, dict):
		return {key: convert_numpy_to_list(value) for key, value in data.items()}
	else:
		return data
		
def rezultati_analiticki(results: dict):
	with open("results/rezultati_analiticki.txt", "w") as file:
		for k, data in results.items():
			file.write(f"K = {k}\n")
			
			data = copy.deepcopy(data)
			data = convert_numpy_to_list(data)
			
			file.write(f"Odnos protoka: {data['odnos_protoka']}\n")
			file.write(f"Critical Resource: {data['critical_resource']}\n")
			file.write(f"a: {data['a_max']}\n")
			
			pprint.pprint(data['parameters'], stream=file)
			
			file.write("\n")
			
	print("Generated rezultati_analiticki.txt")


def rezultati_simulacija(results: list):
	with open("results/rezultati_simulacija.txt", "w") as file:
		for result in results:
			file.write(f"K = {result['K']}, r = {result['r']}\n")
			
			file.write(f"Response Time: {result['response_time']}\n")
			
			file.write(f"\nUtilization: \n")
			pprint.pprint(result['utilization'], stream=file)
			
			file.write(f"\nThroughput: \n")
			pprint.pprint(result['throughput'], stream=file)
			
			file.write(f"\nProcessing Time: \n")
			pprint.pprint(result['processing_time'], stream=file)
			
			file.write("\n")
			
		
	print("Generated rezultati_simulacija.txt")
	
def averaged_dictionary(list_of_dicts):
	averaged_dict = dict()
	
	for key in list_of_dicts[0]:
		if isinstance(list_of_dicts[0][key], dict):
			averaged_dict[key] = averaged_dictionary([dict_[key] for dict_ in list_of_dicts])
		elif isinstance(list_of_dicts[0][key], list):
			averaged_dict[key] = np.mean([dict_[key] for dict_ in list_of_dicts], axis=0)
		else:
			averaged_dict[key] = np.mean([dict_[key] for dict_ in list_of_dicts])
			
	return averaged_dict
		
def rezultati_simulacija_usrednjeno(results: list):
	results = {
		K : {
			r : [result for result in results if result["K"] == K and result["r"] == r] for r in Variables.r.value
		} for K in Variables.K.value
	}
	
	results = {
		K : {
			r : averaged_dictionary(results[K][r]) for r in Variables.r.value
		} for K in Variables.K.value
	}
	
	with open("results/rezultati_simulacija_usrednjeno.txt", "w") as file:
		for K in Variables.K.value:
			for r in Variables.r.value:
				file.write(f"K = {K}, r = {r}\n")
				
				file.write(f"Response Time: {results[K][r]['response_time']}\n")
				
				file.write(f"\nUtilization: \n")
				pprint.pprint(results[K][r]['utilization'], stream=file)
				
				file.write(f"\nThroughput: \n")
				pprint.pprint(results[K][r]['throughput'], stream=file)
				
				file.write(f"\nProcessing Time: \n")
				pprint.pprint(results[K][r]['processing_time'], stream=file)
				
				file.write("\n")

	print("Generated rezultati_simulacija_usrednjeno.txt")
	