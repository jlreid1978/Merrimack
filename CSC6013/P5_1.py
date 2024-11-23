# Jesse Reid CSC6013 coding project P5 #1


# function to calculate the number of digits in the binary expansion/representation of a positive integer n
def binary(n, bin_value=0):
    # verify a positive integer
    if n <= 0:
        raise ValueError("Integer must be positive")
    
    # stop condition - if n is 1 the answer is 1
    elif n == 1:
        bin_value += 1
        return bin_value
    
    # calculate the number of digits by recursion
    else:
        bin_value += 1
        return binary(int(n / 2), bin_value)
        

def main():
    # solve for 256 and 750
    instances = [256, 750]
    for i in instances:
        try:
            bin_value = binary(i)
            print(f"The binary expansion/representation of {i} has {bin_value} digits.")
        except ValueError as e:
            print(e)
   
if __name__ == "__main__":
    main() 