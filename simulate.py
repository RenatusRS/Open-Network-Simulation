from multiprocessing import Pool, Value
import time

from generate import generate_jobs, generate_scheme
from parameters import SimulationParameters, Variables


def simulate(a_max_values):
	print("Simulation started")
	
	print(a_max_values)
	
	parameters = [(r, a_max_values[K - 2], K) for r in Variables.r.value for K in Variables.K.value] * SimulationParameters.NumberOfSimulations.value
	
	cnt = Value('i', len(parameters))
	
	start_time = time.time()
	
	with Pool(initializer=init_globals, initargs=(cnt,)) as pool:
		results = pool.starmap(simulation, parameters)
		
	end_time = time.time()
	
	print("Simulation completed - Elapsed time: {:.2f} seconds".format(end_time - start_time))
	
	return results


def init_globals(counter):
    global cnt
    cnt = counter

def simulation(r, alpha, K, time = SimulationParameters.SimulationTimeMinutes.value):
	time *= 60 * 1000 # minutes to milliseconds
	
	alpha /= 1000 # jobs/second to jobs/millisecond

	scheme = generate_scheme(K)
	jobs = generate_jobs(time, alpha * r)
	
	print(f"r = {r}, alpha = {alpha}, K = {K} | START")
	scheme.simulate(jobs)
	
	with cnt.get_lock():
		cnt.value -= 1
        
		print(f"r = {r}, alpha = {alpha}, K = {K} | DONE ({cnt.value} left)")
	
	return scheme.get_results(r, K)
