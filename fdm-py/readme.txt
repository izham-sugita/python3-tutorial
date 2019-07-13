This folder is for Python based FDM for 1D heat equation.

The code demonstrates three-steps typical in any numerical simulation setting.

1. Pre-processing
Setting up array for initial value.

2. Solver
Loop for time marching solver.

3. Post-processing
Visualization of the results.


4. Comparisons for C++/plain Python/ numba compiled Python

sugita@sugita-GT70-2OC-2OD:~/research/python3/codes/tutorial/fdm-py$ ./1Dheatcpp 
Iteration: 5000 steps
Time 0.000369372 secs
100

sugita@sugita-GT70-2OC-2OD:~/research/python3/codes/tutorial/fdm-py$ python3 1D-heat.py 
Elapsed time after 5000 steps: 0.369135

sugita@sugita-GT70-2OC-2OD:~/research/python3/codes/tutorial/fdm-py$ python3 1D-heat-numba.py 
Elapsed time after 5000 steps: 0.003016

C++ version is still the fastest; but numba-compiled is ... not bad?.. the difference is of an
order of magnitude! But, that is because of -O3 optimization. How about non-optimized compilation?

sugita@sugita-GT70-2OC-2OD:~/research/python3/codes/tutorial/fdm-py$ ./1Dheatcpp
Iteration: 5000 steps
Time 0.00593755 secs
100

Python-numba C++(non-optimized) C++(-O3)
0.003016      0.005937          0.000369

Clearly compiler optimization plays a very big role!
