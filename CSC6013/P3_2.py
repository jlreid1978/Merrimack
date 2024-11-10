# Jesse Reid CSC6013 Coding Project 3 #2

# Bubble Sort
def bubble_sort(A):
    print(A)
    for i in range(len(A)-1):
        compare = 0
        swapCount = 0
        swap = False
        for j in range(len(A)-i-1):
            compare += 1
            if (A[j] > A[j+1]):
                swapCount += 1
                A[j], A[j+1] = A[j+1], A[j]
                swap = True
        
        # print a report of how many elements were conpared and how many were swapped during the iteration
        print(f"\"{compare}\" elements were compared and {swapCount} elements were swapped.\n{A}")

        # if no swap was done, then the sort is complete
        if swap == False:
            break
    print("\n")


def main():
    A4 = [44, 63, 77, 17, 20, 99, 84, 6, 39, 52]
    A5 = [52, 84, 6, 39, 20, 77, 17, 99, 44, 63]
    A6 = [6, 17, 20, 39, 44, 52, 63, 77, 84, 99]
    
    bubble_sort(A4)
    bubble_sort(A5)
    bubble_sort(A6)


if __name__ == "__main__":
    main() 