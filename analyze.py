from parameters import Variables


def analyze():
	protoci = [odredi_protok(K) for K in Variables.K]
	granicne_vrednosti = [odredi_granicne_vrednost(K) for K in Variables.K]
	parametri_jackson = [odredi_parametre_jackson(K) for K in Variables.K]


def odredi_protok(K):
    pass

def odredi_granicne_vrednost(K):
	pass

def odredi_parametre_jackson(K):
	pass