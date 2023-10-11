import numpy as np
from parameters import Variables


def average_dictionary(list_of_dicts):
	averaged_dict = dict()
	
	for key in list_of_dicts[0]:
		if isinstance(list_of_dicts[0][key], dict):
			averaged_dict[key] = average_dictionary([dict_[key] for dict_ in list_of_dicts])
		elif isinstance(list_of_dicts[0][key], list):
			averaged_dict[key] = np.mean([dict_[key] for dict_ in list_of_dicts], axis=0)
		else:
			averaged_dict[key] = np.mean([dict_[key] for dict_ in list_of_dicts])
			
	return averaged_dict
	
	
def average_results(results):
	results = {
		K : {
			r : [result for result in results if result["K"] == K and result["r"] == r] for r in Variables.r.value
		} for K in Variables.K.value
	}
	
	results = {
		K : {
			r : average_dictionary(results[K][r]) for r in Variables.r.value
		} for K in Variables.K.value
	}
	
	return results
