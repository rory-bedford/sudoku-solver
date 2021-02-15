# sudoku-solver
My implementation of a backtracking algorithm to solve any sudoku

## How to use:

First you need to make a .txt file with the sudoku in it. This should be only 9 lines with 9 characters on each line. Zeros represent blank spaces. See the examples folder if this is unclear. Any other type of file will result in an error.

Activate the environment, run the script 'solver.py', which will prompt you for the sudoku filename. It will then solve the sudoku (you can watch it solving in the terminal) and will then create a file called filename_solved.txt (with your original filename) containing the solved sudokus.

I have not implemented error messages for all possible errors. If the sudoku is unsolveable (for example if there are initially two 1s in the same row), the algorithm will run forever. Ctrl+C to stop this. If you give a sudoku with multiple possible solutions (such as zeros.txt in examples) it will spit out the first complete solution it finds.

If the sudoku is taking ages to solve, go into solver.py, and change the time.sleep() variable near the bottom to something smaller, or just comment it out completely. It's fun to watch simple sudokus solve but harder ones can take forever.

I didn't want to read up on how backtracking algorithms work at all so I could try and figure it out for myself. This means my algorithm is definitely sub-optimal and rather slow.
