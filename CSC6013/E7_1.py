# Jesse Reid CSC6013 In Class Exercise E7 Array Sum

# recursive function to find the sum of an array
def arraySum(A, start, end, sos):
    # counter increment
    sos += 1 
    # print the current subarray being processed
    print(f"Recursive call with subarray: {A[start:end+1]}")
    
    if start == end:
        # print when a base case is returned
        print(f"Base case reached with single element {A[start]}.")
        return A[start], sos
    else:
        mid = (start + end) // 2
        # left half recursion
        left_sum, sos = arraySum(A, start, mid, sos)
        # right half recursion
        right_sum, sos = arraySum(A, mid + 1, end, sos)
        combined_sum = left_sum + right_sum
        # recursive status of the recursive call
        print(f"Returning from subarray {A[start:end+1]} with a sum of {combined_sum} and {sos} recursive sums as of now.")
        return combined_sum, sos
    
    


def main():
    A_list = [
        [38, 21, 39, 60, -1, 10, 81, 23],
        [2, 97, 5, 88, 9, 72, 12, 64, 17, 56, 21],
        [100, 33, 22, 213, 65, 29, 153, 199, 47, 181, 85]
    ]

    for A in A_list:
        # initialize the sum of sums counter
        sum_of_sums = 0 
        # call recursive function
        sum_of_array, sum_of_sums = arraySum(A, 0, len(A) - 1, sum_of_sums)
        # print the final sum and number of recursive calls
        print(f"\nThe sum is: {sum_of_array}\nThe total number of recursive sums: {sum_of_sums}\n{"-" * 40}\n\n")


if __name__ == "__main__":
    main()