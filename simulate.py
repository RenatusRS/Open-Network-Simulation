from multiprocessing import Pool, Value
import time

from generate import generate_jobs, generate_scheme
from parameters import SimulationParameters, Variables


def simulate(α_values):
	print("Simulation started")
	
	print(α_values)
	
	parameters = [(r, α_values[K - min(Variables.K.value)], K) for r in Variables.r.value for K in Variables.K.value] * SimulationParameters.NumberOfSimulations.value
	
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

def simulation(r, α, K, time = SimulationParameters.SimulationTimeSeconds.value):
	scheme = generate_scheme(K)
	jobs = generate_jobs(time, α * r)
	
	print(f"r = {r}, α = {α}, K = {K} | START")
	scheme.simulate(jobs)
	
	with cnt.get_lock():
		cnt.value -= 1
        
		print(f"r = {r}, α = {α}, K = {K} | DONE ({cnt.value} left)")
	
	return scheme.get_results(r, K)
