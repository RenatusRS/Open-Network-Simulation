# Open Network Simulation

> Project for **Computer Systems Performance** / **Performanse Računarskih Sistema** class.

Python-based application that performs analytical calculations on the specified parameters.

Following the analytical calculations, it simulates an open network system, generating jobs that enter the system in accordance with a Poisson distribution. The user-configurable schema determines how these jobs are transferred between the system's components.

Finally, the findings are presented in Excel tables, text, and visual graphs.

## Features
- **Analytical Solution**: Uses input parameters to compute server flows and identifies the bottleneck system resource. Applies Jackson's theorem in calculation for other parameters. Provides expected values for the given system.
  
- **Simulation**: Examines system behavior, showing dynamics for different configurations and job intensities. Provides simulated values for the given system.

- **Analysis & Documentation**: Compares results from the analytical method with simulation outcomes and averages from several runs. The data is presented visually for clarity.

## Configuration
### parameters.py
This file hosts the adjustable parameters for the simulation.

#### Default Values

**Processing Speed**
| Parameter                        | Default Value |
|----------------------------------|---------------|
| Processor                        | 6.25ms        |
| System Disk 1                    | 10ms          |
| System Disk 2                    | 15ms          |
| System Disk 3                    | 15ms          |
| User Disk                        | 25ms          |

**Processor Transfer Probability**
| Parameter                        | Default Value |
|----------------------------------|---------------|
| System Disk 1                    | 15%           |
| System Disk 2                    | 10%           |
| System Disk 3                    | 5%            |
| User Disk                        | 50%           |
| Processor                        | 20%           |

**System Disk Transfer Probability**
| Parameter                        | Default Value |
|----------------------------------|---------------|
| Processor                        | 30%           |
| Self                             | 20%           |
| User Disk                        | 50%           |

**Variables**
| Parameter                                    | Default Value            |
|----------------------------------------------|--------------------------|
| r (job arrival rate modification)            | [0.25, 0.50, 0.77, 0.99] |
| K (num. of user disks)                       | [2, 3, 4, 5]             |

**Simulation Parameters**
| Parameter                        | Default Value   |
|----------------------------------|-----------------|
| Simulation Time                  | 30 minutes      |
| Number of Simulations            | 100             |

> **Note:** The specified simulation time pertains to simulated durations, not the real-time operation of the program.

### generate.py
This file contains the `generate_schema(number_of_disks)` function that molds the system's schema. For those looking to modify the system's architecture, tweaking this function will be essential. To grasp the role and functionality of each class, please delve into the "simulation" folder.

#### Default Schema
![image](https://github.com/RenatusRS/Open-Network-Simulation/assets/19864929/597c1e93-71b4-4fe7-b3d0-f18006c35847)

## How-To Run
1. Ensure you have the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Execute the program by running `main.py`:
   ```
   python main.py
   ```
