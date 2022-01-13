## This program is written to solve sudoku puzzles
import sys

# Sudoku class encapsulates the neccesary methods needed 
# to solve the sudoku puzzle.

class Sudoku:
    
    # Represents the none of the cells are empty
    NONE_EMPTY = -1   

    # Represents the empty element
    EMPTY_ELEM = 0

    # Represents the value of the smallest element
    MIN_NUM = 1
    
    # Constructor creates am instance of Sudoku
    def __init__(self, arr, n):
        self.arr = arr
        self.col_num = n
        self.row_num = n
        self.max_num = n
        self.box_limit = int(n ** 0.5)

    # Returns the index of first empty cell in the row if present;
    # otherwise returns NONE_EMPTY.
    def find_empty_col_idx(self, row_idx):
        col_idx = Sudoku.NONE_EMPTY
        for idx in range(self.col_num):
            if self.arr[row_idx][idx] == Sudoku.EMPTY_ELEM:
                col_idx = idx
                break
        return col_idx

    # Returns a tuple of (row_index, col_idx) if an empty element is present;
    # otherwise return NONE_EMPTY tuple.
    def find_empty_elem(self):
        
        for row_idx in range(self.row_num):
            col_idx = self.find_empty_col_idx(row_idx)
            if col_idx != Sudoku.NONE_EMPTY:
                return (row_idx, col_idx)
        return (Sudoku.NONE_EMPTY, Sudoku.NONE_EMPTY)

    # Checks if the row has "num" in any of its cell.
    def row_has_num(self, row_idx, num):
        for each in self.arr[row_idx]: 
            if each == num:
                return True
        return False

    # Checks if the col has "num" in any of its cell.
    def col_has_num(self, col_idx, num):
        for row_idx in range(self.row_num):
            if self.arr[row_idx][col_idx] == num:
                return True
        return False

    # Checks if the box has "num" in any of its cell.
    def box_has_num(self, row, col, num):
        box_init_row = (row - (row % self.box_limit))
        box_init_col = (col - (col % self.box_limit))

        for row_idx in range(self.box_limit):
            for col_idx in range(self.box_limit):
                if self.arr[box_init_row + row_idx][box_init_col + col_idx] == num:
                    return True
        return False
    
    # Checks if the num can be inserted into that cell.
    def is_suitable_num(self, row_idx, col_idx, num):
        not_in_row = not self.row_has_num(row_idx, num)
        not_in_col = not self.col_has_num(col_idx, num)
        not_in_box = not self.box_has_num(row_idx, col_idx, num)
        return not_in_box and not_in_col and not_in_row

    # Checks if the sudoku instance is solved.
    def is_solved(self):
        
        if self.find_empty_elem == (Sudoku.NONE_EMPTY, Sudoku.NONE_EMPTY):
            for row_idx in range(self.row_num):
                for col_idx in range(self.col_num):
                    num = self.arr[row_idx][col_idx]
                    if not self.is_suitable_num(row_idx, col_idx, num):
                        return False
        else:
            return False
        return True

    # return true if the puzzle can be solved.
    def solve(self):
        # find an empty space place a suitable number and check
        row_idx, col_idx = self.find_empty_elem() 
        if (row_idx, col_idx) != (Sudoku.NONE_EMPTY, Sudoku.NONE_EMPTY):
            for num in range(Sudoku.MIN_NUM, self.max_num + 1):
                if self.is_suitable_num(row_idx, col_idx, num):
                    self.arr[row_idx][col_idx] = num
                    if self.solve():
                        return True
                    else:
                        self.arr[row_idx][col_idx] = Sudoku.EMPTY_ELEM
            return False
        else: 
            return True
        
    # Prints the solved sudoku puzzle if it is solvable;
    # otherwise print not solvable.
    def print_solved(self):
        if self.solve():
            print("\nThis is the Solved Puzzle")
            for row in self.arr:
                each_row = ""
                for elem in row:
                    each_row += str(elem) + " "
                print(each_row)
            
            print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
        else:
            print("Sorry, this puzzle could not be solved  :(\n")

##############################################################
        
# Gets Sudoku puzzle input from user .
def get_user_input(n):

    rows = sys.stdin.readlines()
    arr = []

    if len(rows) != n:
        print("\nThere seems to be more or less number of rows in the puzzle, please check again...")
        return 
    
    for row in rows:
        each_row = row.split(' ')
        if len(each_row) != n:
            print("\nThere seems to be more or less elems in row " + str(rows.index(row)))
        num = []
        for each in each_row:
            num.append(int(each))   
        arr.append(num)
    
    Sudoku(arr, n).print_solved()


if __name__ == "__main__":

    user_name = input("Hi! Let's get to know each other. Please tell me your your name: \n")

    print("Hello " + user_name + "! \nNow before we start, let me tell you a bit more about this game....\n")
    print("You can choose and specify if you want to solve a 2X2 or 3X3 or 4X4 Sudoku puzzle!\n")
    print("Isn\'t that exicting, " + user_name + "?\n")
    print("You can enter the numbers in each row by leaving a space between them.")
    print("The unknown or empty slots can be filled with a 0.\n")
    print("After typing the puzzle, please press ctrl + d to start solving.")
    start = input("Type in Yes to start or No to exit\n")

    if start.upper() == "NO":
        print("Thank you! Hope you come back later with puzzles to solve!")
        sys.exit()

    print("If you want to solve a 2X2 puzzle type 2, or 3 if you want to solve 3X3, and 4 if you want \nto solve 4X4.")
    n = int(input("Enter the size of puzzle you want to solve:"))

    print("Please Enter Your Puzzle below, with each row in each line!")
    get_user_input(n * n)

    next_puzzle = input("Would you like to solve another puzzle? Type Yes. \nType No if you want to exit\n")

    while next_puzzle.upper() == "YES":
        n = int(input("Enter the size of puzzle you want to solve:"))
        print("Please Enter Your Puzzle below, with each row in each line!")
        get_user_input(n * n)
        next_puzzle = input("Would you like to solve another puzzle? Type Yes. \nType No if you want to exit")

    print("Thank you! Hope to see you again!")

