# QKP.0.0.2-28032022

> Quantum algorithm to solve Knapsack Problem

## Solve optimization problems using quantum computing through the Adiabatic Quantum Computing AQC approach. 
The binary knapsack problem is solved by using the Ising model and its implementation in the Python programming language on the Qiskit library. Specifically, the MinimunEigenOptimizer algorithm developed by the IBM team is used to solve quantum problems.


## Requirements

* Python >= 3.6
* Pipenv `pip install pipenv`
* conda


## Setup

> [rootDirectory]/ pipenv install --dev
> [rootDirectory]/ conda create --name qiskit
> [rootDirectory]/ conda activate qiskit
> [rootDirectory]/ pip install -r requirements.txt


## Development

### Run 

Ubication program is /Algorithm_BKP_Quantum_Solution

#### Custom run

> [rootDirectory]/pyhton main.py [-h] [-i ITERATIONS] [-d] [-fl FILE | -fd FOLDER] {generate}

> [rootDirectory]/pyhton main.py generate [-h] -t TYPE [TYPE ...] -d DIFFICULT [DIFFICULT ...] -n NITEMS [NITEMS ...] -r RANGE [RANGE ...]

#### Default run

> [rootDirectory]/pyhton main.py
