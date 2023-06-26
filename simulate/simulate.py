import json
from multiprocessing import Pool, Value
import time
from simulate.Job import Job
from simulate.components.Active import Active
from simulate.components.Component import Component
from parameters import UserInput, Variables
from simulate.components.Counter import Counter
from simulate.generate import generate_scheme, generate_jobs


def init_globals(counter):
    global cnt
    cnt = counter
	
def simulate():
	parameters = [(r, K, i + 1) for r in Variables.r.value for K in Variables.K.value for i in range(UserInput.NumberOfSimulations.value)]
	
	cnt = Value('i', len(parameters))
	
	start_time = time.time()
	
	with Pool(initializer=init_globals, initargs=(cnt,)) as pool:
		results = pool.starmap(simulation, parameters)
		
	end_time = time.time()
	
	print("Elapsed time: {:.2f} seconds".format(end_time - start_time))
	
	averaged_results = {
		K : {
			r : {
				"total_runtime": sum([result["total_runtime"] for result in results if result["K"] == K and result["r"] == r]) / UserInput.NumberOfSimulations.value,
				"utilization_average": sum([result["utilization_average"] for result in results if result["K"] == K and result["r"] == r]) / UserInput.NumberOfSimulations.value,
				"job_time_average": sum([result["job_time_average"] for result in results if result["K"] == K and result["r"] == r]) / UserInput.NumberOfSimulations.value
				
			} for r in Variables.r.value
		} for K in Variables.K.value
	}
	
	print(json.dumps(averaged_results, indent=4))
	
	return averaged_results


def simulation(r, K, i, time = UserInput.SimulationTime.value):
	time *= 60 * 1000

	scheme = generate_scheme(K)
	jobs = generate_jobs(time, 1.0 / r)
	print(len(jobs))
	
	print(f"r = {r}, K = {K}, i = {i} | START")
	scheme.simulate(jobs)
	
	with cnt.get_lock():
		cnt.value -= 1
        
		print(f"r = {r}, K = {K}, i = {i} | DONE ({cnt.value} left)")
	
	return scheme.get_results(r, K)

#			"total_runtime": total_runtime,
#			"utilization": utilization,
#			"utilization_average": utilization_average,
#			"job_time_average": job_time_average
