from parameters import Variables
from results.write import protoci_analiticki, rezultati_analiticki, rezultati_simulacija, rezultati_simulacija_usrednjeno
from simulate import simulate
from analyze import analyze


if __name__ == '__main__':
	analyze_results = analyze()
	
	protoci_analiticki(analyze_results)
	rezultati_analiticki(analyze_results)
	
	a_max_values = [analyze_results[K]['a_max'] for K in Variables.K.value]
	
	simulate_results = simulate(a_max_values)
	
	rezultati_simulacija(simulate_results)
	rezultati_simulacija_usrednjeno(simulate_results)
	