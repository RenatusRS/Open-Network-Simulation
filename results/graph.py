from matplotlib import pyplot as plt
from generate import generate_resource_list
from parameters import Variables


def grafik_zavisnosti_a_max_K(results: dict):
	K = results.keys()
	a_max = [results[k]['a_max'] for k in K]
	
	plt.plot(K, a_max)
	
	plt.title("Zavisnost α max od K")
	plt.xlabel("K")
	plt.ylabel("α max")
	
	plt.xticks([i for i in K], [f"{i}" for i in K])
	
	plt.savefig("results/graphs/zavisnost_a_max_K.png")



def grafik_iskoriscenja(results: dict):
	figure, plots = plt.subplots(4, 1, figsize=(6, 15))
	
	servers = generate_resource_list()
	
	for r, plot in zip(Variables.r.value, plots):
		plot: plt.Axes = plot
		
		plot.set_title(f"r = {r}")
		plot.set_xlabel("K")
		plot.set_ylabel("U", rotation=0, labelpad=10)
		plot.set_xticks([i for i in Variables.K.value])
		plot.set_ylim(0, 1.2)
		
		for server in servers:
			plot.plot(Variables.K.value, [results[k]['parameters'][r]['U'][server] for k in Variables.K.value])
			
	plt.subplots_adjust(hspace=0.5)
	plt.subplots_adjust(bottom=0.05)
			
	figure.suptitle("Iskorišćenje resursa")
	figure.legend([f"{server}" for server in servers])
	figure.savefig("results/graphs/iskoriscenje.png")

def grafik_vremena_odziva(results: dict):
	figure, plots = plt.subplots(4, 1, figsize=(6, 15))
	
	servers = generate_resource_list()
	
	for r, plot in zip(Variables.r.value, plots):
		plot: plt.Axes = plot
		
		plot.set_title(f"r = {r}")
		plot.set_xlabel("K")
		plot.set_ylabel("T", rotation=0, labelpad=10)
		plot.set_xticks([i for i in Variables.K.value])
		
		for server in servers:
			plot.plot(Variables.K.value, [results[k]['parameters'][r]['T'][server] for k in Variables.K.value])
			
	plt.subplots_adjust(hspace=0.5)
	plt.subplots_adjust(bottom=0.05)
	
	figure.suptitle("Vreme odziva")
	figure.legend([f"{server}" for server in servers])
	figure.savefig("results/graphs/vreme_odziva.png")

def grafik_vremena_odziva_sistema(results):
	figure, plots = plt.subplots(4, 1, figsize=(6, 15))
	
	for r, plot in zip(Variables.r.value, plots):
		plot: plt.Axes = plot
		
		plot.set_title(f"r = {r}")
		plot.set_xlabel("K")
		plot.set_ylabel("T", rotation=0, labelpad=10)
		plot.set_xticks([i for i in Variables.K.value])
		
		plot.plot(Variables.K.value, [results[k]['parameters'][r]['T_OVERALL'] for k in Variables.K.value])
		
	plt.subplots_adjust(hspace=0.5)
	plt.subplots_adjust(bottom=0.05)
	
	figure.suptitle("Vreme odziva sistema")
	figure.savefig("results/graphs/vreme_odziva_sistema.png")
	