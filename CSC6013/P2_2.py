# Jesse Reid CSC6013 Coding Project 2 #2
from math import inf

# function finds the lowest distance between all numbers in an array
def distance(nums):
    least = inf

    # check the distance between every number in the array and see if it is smaller than the previous value
    for num in nums:
        for i in range(len(nums)):
            if nums[i] != num:
                value = abs(nums[i] - num)
                if value < least:
                    least = value

    # return the smallest distance found from comparison
    return least


# function initializes the number arrays and prints the lowest distance found
def main():
    num_arrays = [[50, 120, 250, 100, 20, 300, 200], [12.4, 45.9, 8.1, 79.8, -13.64, 5.09]]
    for nums in num_arrays:
        print(f"The smallest distance between any two numbers in {nums} is {distance(nums)}.\n")


if __name__ == "__main__":
    main() 