# SudokuSolver

This Repo includes a code for Sudoku Solver. It is inspired from [Sudoku | Backtracking 7](https://www.geeksforgeeks.org/sudoku-backtracking-7/) article written in GeeksForGeeks website. <br/>
The Sudoku Solver program can be used to solve 2X2, 3X3, 4X4, and so on... Sudoku puzzles. 


## Userguide

**Note**: It is assumed that the user has python3 program installed in their local device.<br/>

Please run the file SudokuSolver.py, on Command Line. The instructions to solve is explicitly stated as instructions, once the program is run. <br/>


### Input Errors

The program can recognise some basic user errors : <br/>
+ If any of the rows have more or less number of elements.
+ If the puzzle has more or less number of rows than expected. <br/>
do take note that this is an basic program, and as such cannot anticipate all possible user errors. <br/>

## Example

*Example taken from [Sudoku | Backtracking 7](https://www.geeksforgeeks.org/sudoku-backtracking-7/) article written in GeeksForGeeks website.* <br/>
Lets suppose that you have a 3X3 Sudoku puzzle that you want to solve.<br/>
Fill the value of empty cells as 0.<br/>
Leave a space between each cell value, as show below.<br/>

> 3 0 6 5 0 8 4 0 0 <br/>
> 5 2 0 0 0 0 0 0 0 <br/>
> 0 8 7 0 0 0 0 3 1 <br/>
> 0 0 3 0 1 0 0 8 0 <br/>
> 9 0 0 8 6 3 0 0 5 <br/>
> 0 5 0 0 9 0 6 0 0 <br/>
> 1 3 0 0 0 0 2 5 0 <br/>
> 0 0 0 0 0 0 0 7 4 <br/>
> 0 0 5 2 0 6 3 0 0 <br/>


After Finishing the whole typing please enter **CTRL + D**, to solve the puzzle.<br/>

The following Solution will be displayed: <br/>

> 3 1 6 5 7 8 4 9 2<br/>
> 5 2 9 1 3 4 7 6 8<br/>
> 4 8 7 6 2 9 5 3 1<br/>
> 2 6 3 4 1 5 9 8 7<br/>
> 9 7 4 8 6 3 1 2 5<br/>
> 8 5 1 7 9 2 6 4 3<br/>
> 1 3 8 9 4 7 2 5 6<br/>
> 6 9 2 3 5 1 8 7 4<br/>
> 7 4 5 2 8 6 3 1 9<br/>

However, if the Sudoku puzzle received is not solvable, the following will be printed to the output: <br/>

> Sorry, this puzzle could not be solved  :(

## Scope for Future Improvement

The program written can be updated with the following features: <br/>
+ Improvement in User Interface 
+ Can be developed into an app for mobile devices


