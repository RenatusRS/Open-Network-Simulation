from parameters import Variables
from results.graph import grafik_iskoriscenja, grafik_vremena_odziva, grafik_vremena_odziva_sistema, grafik_zavisnosti_a_max_K
from results.table import tabela_analitika_simulacija
from results.write import protoci_analiticki, rezultati_analiticki, rezultati_simulacija, rezultati_simulacija_usrednjeno
from simulate import simulate
from analyze import analyze


if __name__ == '__main__':
	analyze_results = analyze()
	
	protoci_analiticki(analyze_results)
	rezultati_analiticki(analyze_results)
	
	grafik_zavisnosti_a_max_K(analyze_results)
	
	grafik_iskoriscenja(analyze_results)
	grafik_vremena_odziva(analyze_results)
	grafik_vremena_odziva_sistema(analyze_results)
	
	a_values = [analyze_results[K]['a_max'] for K in Variables.K.value]
	
	simulate_results = simulate(a_values)
	
	rezultati_simulacija(simulate_results)
	
	rezultati_simulacija_usrednjeno(simulate_results)
	
	tabela_analitika_simulacija(analyze_results, simulate_results)
	

	