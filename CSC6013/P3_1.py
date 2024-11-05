# Jesse Reid CSC6013 Coding Project 3 #1

# Selection Sort
def selection_sort(A):
    # print the original list
    print(A)
    # count backwards from the last element to the second element. 
    # At the time of reaching the second element the first has already been sorted.
    for i in range(len(A)-1, 0, -1):
        compare = 0
        swap = 0
        # set the value that was originally in the "i" position
        startIndex = A[i]
        # initially sets the max index to the position being evaluated
        maxIndex = i

        # evaluates the remaining elements against the max value
        for j in range(0, i):
            # comparison counter
            compare += 1
            if (A[j] > A[maxIndex]):
                # counts the times that a new value has been swapped for max index
                swap += 1
                maxIndex = j

        # if there has been a change, swap in the list
        if A[i] != A[maxIndex]:
            A[i], A[maxIndex] = A[maxIndex], A[i]
        
        # print the details after the outer loop iteration
        print(f"\"{startIndex}\" was compared {compare} times and swapped as max {swap} times.\n{A}")
    print("\n")


def main():
    A1 = [63, 44, 17, 77, 20, 6, 99, 84, 52, 39]
    A2 = [84, 52, 39, 6, 20, 17, 77, 99, 63, 44]
    A3 = [99, 84, 77, 63, 52, 44, 39, 20, 17, 6]
    
    selection_sort(A1)
    selection_sort(A2)
    selection_sort(A3)


if __name__ == "__main__":
    main() 