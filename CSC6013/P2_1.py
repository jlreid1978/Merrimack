# Jesse Reid CSC6013 Coding Project 2 #1

# function takes the input array as well as the input int 
# then checks each number in the array to see if it is divisible by the int
def mathy(nums, by):
    count = 0
    for num in nums:
        if num %by == 0:
            count += 1
    # returns the count of numbers divisible by the int back to main
    return count


# main function that initializes the array variables as well as the int variables
def main():
    nums = [[20, 21, 25, 28, 33, 34, 35, 36, 41, 42], [18, 54, 76, 81, 36, 48, 99]]
    denoms = [7, 9]
    index = 0
    for n in nums:
        # print statement that calls the function to process the result
        print(f"The number of entries in {n} divisible by {denoms[index]} is {mathy(n, denoms[index])}.\n")
        index += 1
        

if __name__ == "__main__":
    main() 