# Open Network Simulation

> Project for **Computer Systems Performance** / **Performanse Računarskih Sistema** class.

## Introduction

This project, implemented in Python, models a multiprogramming computer system via an open network operating in a steady-state regime. The simulated system consists of a processor, three system disks, and 𝐾 user disks, with jobs arriving at the processor following a Poisson process with intensity 𝛼. The system operates on exponential processing and service times with respective averages of 𝑆𝑝 = 6.25𝑚𝑠 for the processor, 𝑆𝑑1 = 10𝑚𝑠 for the first system disk, 𝑆𝑑2 = 𝑆𝑑3 = 15𝑚𝑠 for the second and third system disks, and 𝑆𝑑𝑘 = 25𝑚𝑠 for user disks.

The project facilitates the analytical evaluation and simulation of the system, determining the utilization of resources, flows through resources, average number of jobs at each resource, and the system's response time with a central server for varying numbers of user disks (𝐾) and input flow intensities (𝑟 ⋅ 𝛼𝑚𝑎𝑥, 𝑟 ∈ {0.25,0.50,0.77, 0.99}). It identifies the critical resource in the system and provides a detailed comparison between the analytical and simulated results.

## Features

- **Analytical Evaluation:** The project offers a robust analytical evaluation method to determine the flows through servers based on the defined system input parameters. It calculates the limiting values of input flow intensity for which the system remains in a steady state and identifies the critical resource in the system for each value of 𝐾 and 𝑟.
  
- **Simulation:** A comprehensive simulation functionality is provided to emulate the system's operation. It generates and averages the results of 100 simulations for each combination of parameters 𝑟 and 𝐾, thereby offering a detailed insight into the system's behavior under different conditions.

- **Documentation and Analysis:** An in-depth analysis and documentation of the simulation method, analytical problem solving, and comparative analysis of the results obtained are encapsulated in this project. It provides tabular reports of relative deviations and constructs various diagrams depicting different dependencies and critical resources, enhancing the understanding of the system's performance.

## Configuration

**Parameters Configuration:** The `parameters.py` file contains configurable parameters essential for the simulation such as processing speeds, probabilities, and simulation parameters.

**System Schema Generation:** The `generate.py` file houses the function `generate_schema(number_of_disks)` crucial for generating a schema of the system, which can be modified to alter the system's schema.

## How-To Run

Install the required dependencies with:
```bash
pip install -r requirements.txt
```
Execute the program by running:
```bash
python main.py
```
