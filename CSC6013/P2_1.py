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
    nums = []
    # obtain integers to add to the array
    while True:
        try:
            num = int(input("Please input an integer value for the array. Press enter when finished filling array. "))
            nums.append(num)
            print(f"Array = {nums}")

        except ValueError:
            print(f"Complete array = {nums}")
            break
    # obtain the denomenator 
    while True:
        try:
            denom = int(input("Please input an integer to divide by. "))
            if denom <= 0:
                raise ValueError
            else:
                break
        except ValueError:
            print("Value must be an integer > 0")
    
    # print statement that calls the function to process the result
    print(f"The number of entries in {nums} divisible by {denom} is {mathy(nums, denom)}.\n")
        
        

if __name__ == "__main__":
    main() 