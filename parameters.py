from enum import Enum

class ProcessingSpeed(Enum):
    Processor   = 6.25
	
    SystemDisk1 = 10
    SystemDisk2 = 15
    SystemDisk3 = 15
    
    UserDisk    = 25
    
	
class ProcessorProbability(Enum):
	SystemDisk1 = 0.15
	SystemDisk2 = 0.10
	SystemDisk3 = 0.05
        
	UserDisk    = 0.50
        
	Processor   = 0.20
        
		
class DiscProbabiltiy(Enum):
    Processor = 0.30
    Self = 0.20
    UserDisk = 0.50
    

class Variables(Enum):
	#r = [0.25, 0.50, 0.77, 0.99] # arrival rate modification
	#K = range(2, 6) # number of user disks
	r = [0.25, 0.50] # arrival rate modification
	K = range(2, 6) # number of user disks
        
		
class SimulationParameters(Enum):
	SimulationTimeMinutes = 30
	NumberOfSimulations = 5
	