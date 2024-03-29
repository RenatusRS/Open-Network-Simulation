from multiprocessing import Pool, Value
import time

from generate import generate_jobs, generate_schema
from parameters import SimulationParameters, Variables


def simulate(a_values):
	print("\nSimulation started\n")
	
	parameters = [(r, a_values[K - min(Variables.K.value)], K) for r in Variables.r.value for K in Variables.K.value] * SimulationParameters.NumberOfSimulations.value
	
	cnt = Value('i', len(parameters))
	
	start_time = time.time()
	
	with Pool(initializer=init_globals, initargs=(cnt,)) as pool:
		results = pool.starmap(simulation, parameters)
		
	end_time = time.time()
	
	print("\nSimulation completed - Elapsed time: {:.2f} seconds\n".format(end_time - start_time))
	
	return results


def init_globals(counter):
    global cnt
    cnt = counter


def simulation(r, a, K, time = SimulationParameters.SimulationTimeSeconds.value):
	schema = generate_schema(K)
	jobs = generate_jobs(time, a * r)
	
	print(f"r = {r}, a = {a}, K = {K} | START")
	schema.simulate(jobs)
	
	with cnt.get_lock():
		cnt.value -= 1
        
		print(f"r = {r}, a = {a}, K = {K} | DONE ({cnt.value} left)")
	
	return schema.get_results(r, K)
