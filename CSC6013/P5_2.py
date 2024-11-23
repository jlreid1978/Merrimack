# Jesse Reid CSC6013 coding project P5 #2

# function to calculate the sum of the squares of the positive Integers 12 + 22 + 32 + … + n2, given the value of n
def squares(n, square_value=0):
    # verify a positive integer
    if n <= 0:
        raise ValueError("Integer must be positive")
    
    # stop condition - if n is 1 the answer is 1
    elif n == 1:
        square_value += 1
        return square_value
    
    # if n > 1, the answer is n ** 2 plus the sum of the squares up to (n-1) ** 2  
    else:
        square_value += n ** 2
        return squares((n - 1), square_value)


def main():
    # solve for 12 and 20
    instances = [12, 20]
    for i in instances:
        try:
            square_value = squares(i)
            print(f"The sum of the squares of {i} is {square_value}.")
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main() 