from enum import Enum

class Perforamcnes(Enum):
    Sp  = 6.25 # Processor speed
	
    Sd1 = 10 # System disk 1
    Sd2 = 15 # System disk 2
    Sd3 = 15 # System disk 3
    
    SdK = 25 # User disk
    
	
class DiscProbability(Enum):
	Sd1 = 0.15
	Sd2 = 0.10
	Sd3 = 0.05
        
	SdK = 0.50
        
	Pass = 0.20
        
		
class WorkProbabiltiy(Enum):
    Done = 0.30
    Repeat = 0.20
    SdK = 0.50
    

class Variables(Enum):
	r = [0.25, 0.50, 0.77, 0.99]
	K = range(2, 6)
        
		
class UserInput(Enum):
	SimulationTime = 30
	NumberOfSimulations = 100