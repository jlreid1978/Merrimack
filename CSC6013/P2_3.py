# Jesse Reid CSC6013 Coding Project 2 #3

import numpy as np

# function to build a square matrix based on the given size
def buildMatrix(size, name):
    matrix = []
    while len(matrix) != size:
        row = []
        while len(row) != size:
            try:
                row.append(float(input(f"Please input a matrix value for matrix {name}: ")))
            except ValueError:
                print("Value must be a number.")
        matrix.append(row)
        print("Row complete")
    return np.array(matrix)    


 # function to convert matrix to integer type if all elements of the matrix are integers (looks better)
def formatMatrix(matrix):
    if np.all(np.mod(matrix, 1) == 0):
        matrix = matrix.astype(int)
    
    return matrix
    

# function to gather the size of a matrix, create it, then multiply the values
def multiplyMatrix():
    # obtain the matrix size
    while True:
        try:
            size = int(input("What is the size of the square matrix? "))
            if size < 1:
                raise ValueError
            else:
                break
        except ValueError:
            print("Value must be a integer > 1.")

    # create the matrix
    A = buildMatrix(size, "A")
    B = buildMatrix(size, "B")
    print(f"Array A:\n{formatMatrix(A)} \nmultiplied by Array B:\n{formatMatrix(B)}")

    # multiply the matrices
    C = A @ B

    return formatMatrix(C)


# main function to print the result
def main():
    print(f"Result:\n{multiplyMatrix()}")


if __name__ == "__main__":
    main() 