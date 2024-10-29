# Jesse Reid CSC6013 Coding Project 2 #2
from math import inf

# function finds the lowest distance between all numbers in an array
def distance(nums):
    least = inf
    # if there are not two numbers, return an error
    if len(nums) < 2:
        raise ValueError
    else:
        # check the distance between every number in the array and see if it is smaller than the previous value
        for cur_num in nums:
            for i in range(len(nums)):
                if nums[i] != cur_num:
                    value = abs(nums[i] - cur_num)
                    if value < least:
                        least = value

    # return the smallest distance found from comparison
    return least


# function initializes the number arrays and prints the lowest distance found
def main():
    nums = []
    while True:
        try:
            # ask for a float, but if value is an int, display as an int
            num = float(input("Please input a value for the array. Press enter when finished filling array. "))
            if num == int(num):
                num = int(num)
            nums.append(num)
            print(f"Array = {nums}")

        except ValueError:
            print(f"Complete array = {nums}")
            break

    try:
        print(f"The smallest distance between any two numbers in {nums} is {distance(nums)}\n")
    except ValueError:
        print("Unable to compare an array with less than two numbers")


if __name__ == "__main__":
    main() 