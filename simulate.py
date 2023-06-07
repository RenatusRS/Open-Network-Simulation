from parameters import UserInput, Variables

from statistics import mean


def simulate():
	results = {
		r: {
			K: mean([simulation(r, K) for _ in range(UserInput.NumberOfSimulations)]) for K in Variables.K
		} for r in Variables.r
	}

def simulation(r, K, time = UserInput.SimulationTime):
	pass