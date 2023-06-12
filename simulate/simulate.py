from simulate.Job import Job
from simulate.components.Active import Active
from simulate.components.Component import Component
from parameters import UserInput, Variables
from simulate.generate import generate_scheme, generate_jobs



def simulate():
	for K in Variables.K.value:
		for r in Variables.r.value:
			for simulation_number in range(UserInput.NumberOfSimulations.value):
				print(f"Simulation [r = {r}, K = {K}] {simulation_number + 1} / {UserInput.NumberOfSimulations.value}")
				
				simulation(r, K, 5)


def simulation(r, K, time = UserInput.SimulationTime.value):
	time *= 60 * 1000
	
	Active.reset()
	Job.reset()

	entry_point = generate_scheme(K)
	jobs = generate_jobs(time, 1.0 / r)
	
	for job in jobs:
		entry_point.add(job)
		
	Active.simulate()