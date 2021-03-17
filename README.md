# Production Planning Problem
This repository contains the solution to the production planning using two methods --- dynamic programming based approach in C++ and linear optimization based approach in Python3 (using `PuLP` solver)

### Note
- This problem was undertaken as part of the course CS218M [Design and Analysis of Algorithms], Autumn 2020
- The problem statement and I/O format are contained in the `hwk5_problem_statement.pdf` document
- *The evaluation code has been tested to run on \*nix systems. It has not been tested on Windows environment*

### Steps to Run Locally on your System
1. `git clone https://github.com/trunc8/production-planning-problem.git`
2. `pip3 install pulp`

## Usage: Obtain solution from the two methods on default test cases
1. For linear_programming code
	1. `time python3 linear_programming.py < dataset1.txt`
	2. `time python3 linear_programming.py < dataset2.txt`
2. For dynamic_programming code
	1. `g++ -O2 dynamic_programming.cpp`
	2. `time ./a.out < dataset1.txt`
	3. `time ./a.out < dataset2.txt`

## Usage: Generate random testcases with tunable parameters and Compare the time taken by the two methods
1. *(Optional)* Modify the ranges of randint function in the *generate_random_testcases.py* script using a text editor
2. *(Optional)* `python3 generate_random_testcases.py`  
	The existing testcase files in the *random_testcase*\ directory will be overwritten by newly generated testcases.
3. `python3 evaluate_testcases.py`  
	This obtains solutions for each of the testcases in the *random_testcase*\ directory. The order of output is shuffled owing to **multiprocessing** as the objective here is to run over large datasets and compare time taken.

## Authors

* **Siddharth Saha** - [trunc8](https://github.com/trunc8)
* **Titas Chakraborty** - [titas0602](https://github.com/titas0602)
* **Parth Shettiwar** - [parth-shettiwar](https://github.com/parth-shettiwar)
* **Koustav Jana** - [koustavjana](https://github.com/koustavjana)


<p align='center'>Created with :heart: by <a href="https://www.linkedin.com/in/sahasiddharth611/">Siddharth</a></p>
