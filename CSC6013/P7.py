# Jesse Reid CSC6013 Coding Project #7 Quicksort

# recursive function to execute the Lomuto partition
def lomuto(A, left, right, swaps):
    p = A[right]
    i = left
    # itirate through A
    for j in range(left, right):
        # swap if j > p to achieve decending order
        if A[j] > p:
            A[i], A[j] = A[j], A[i]
            i += 1
            swaps[0] += 1
            
    # final swap for the pivot itself
    A[i], A[right] = A[right], A[i]
    swaps[0] += 1
    return i, swaps


# recursive function for quicksort
def quicksort(A, left, right, swaps, calls):
    # call counter
    calls[0] +=1
    if left < right:
        mid, swaps = lomuto(A, left, right, swaps)
        quicksort(A, left, mid - 1, swaps, calls)
        quicksort(A, mid + 1, right, swaps, calls)


def main():
    A_list = [
        [38, 21, 39, 60, -1, 10, 81, 23],
        [2, 97, 5, 88, 9, 72, 12, 64, 17, 56, 21],
        [100, 33, 22, 213, 65, 29, 153, 199, 47, 181, 85]
            ]
    for A in A_list:
        swaps = [0]
        calls = [0]
        # print starting array
        print(f"\nStarting Quicksort for {A}\n")
        # cal Quicksort
        quicksort(A, 0, len(A)-1, swaps, calls)
        # print the sorted array, number of swaps, and number of times that Quicksort was called
        print(f"Sorted array: {A}\nNumber of swaps: {swaps[0]}\nNumber of recursive calls {calls[0]}")
        print("-" * 50, "\n")



if __name__ == "__main__":
    main()