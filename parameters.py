from enum import Enum

class ProcessingSpeed(Enum):
    Processor   = 0.00625
	
    SystemDisk1 = 0.010
    SystemDisk2 = 0.015
    SystemDisk3 = 0.015
    
    UserDisk    = 0.025
    
	
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
	r = [0.25, 0.50, 0.77, 0.99] # arrival rate modification
	K = range(2, 6) # number of user disks
        
		
class SimulationParameters(Enum):
	SimulationTimeSeconds = 30 * 60 # 30 minutes
	NumberOfSimulations = 100
	