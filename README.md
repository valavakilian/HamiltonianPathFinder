# HamiltonianPathFinder
This Repository is a basis of using methods to find all hamiltonian paths between two nodes in a graph.

To run these examples run the runExample python function (it uses python 3 and some number of libraries ) using "python3 runExample.py" and follow the instructions please. All of this has only been tested on a linux machine.

Requirements can be installed with command "pip3 install -r requirements.txt" . Please use a virtual environment if you prefer to keep a seperate run environment.

Why Python? Well python is slow however it does have a series of great librares for making graphs nad printing them. 

Currently we use V2 HamiltonianSolver which is slightly faster than the previous version.

V3 HamiltonianPath uses dynamic programming to find the number of path and whether a path exists much faster. However, I have issues on how to actually retrieve the paths from this solution. However if there are n! paths, there isn't much of an enhancement that can be made.

Thank you