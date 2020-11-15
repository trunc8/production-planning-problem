# CS218M_Assignment
CS218M [Design and Analysis of Algorithms], Autumn 2020

*Note: The evaluation code has been designed to run on \*nix systems. It has not been tested on Windows environment*

### Steps to evaluate the time taken by the two methods
1. *(Optional)* Enter your python3 virtual environment if you like.
2. `pip3 install pulp`
3. *(Optional)* Modify the ranges of randint function in the `generate_random_testcases.py` script
4. `python3 generate_random_testcases.py`  
	The earlier testcase files in the `random_testcase\` directory have now been deleted and replaced by newly generated files.
5. `python3 evaluate_testcases.py`  
  The order is shuffled owing to multiprocessing

### Steps to run the two methods on problem statement test cases
1. For linear_programming code
	1. `pip3 install pulp`
	2. `time python3 linear_programming.py < dataset1.txt`
	3. `time python3 linear_programming.py < dataset2.txt`
2. For dynamic_programming code
	1. `g++ -O2 dynamic_programming.cpp`
	2. `time ./a.out < dataset1.txt`
	3. `time ./a.out < dataset2.txt`
