# Jesse Reid CSC6013 In Class Exercise E7 Mergesort

# 2. Trace the Merge sort algorithm for the following arrays.
# Show to each recursive call the two input and output arrays.


# mergesort recursive function
def mergesort(A):
    print(f"Splitting array: {A}")
    if len(A) <= 1:
        return A
    else:
        mid = len(A) // 2
        left = mergesort(A[:mid])
        print(f"Returned left sorted array: {left}")
        right = mergesort(A[mid:])
        print(f"Returned right sorted array: {right}")
        return merge(left, right)


# function to merge the sorted arrays
def merge(left, right):
    print(f"Merging left array {left} and right array {right}")
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    print(f"Merged array: {result}")
    return result


def main():
    A_list = [
        [38,21,39,60,-1,10,81,23], 
        [2,97,5,88,9,72,12,64,17,56,21], 
        [100, 33, 22, 213, 65, 29, 153, 199, 47, 181, 85]
        ]
    for A in A_list:
        print(f"Sorting {A}\n")
        # call recursive function
        A = mergesort(A)
        # print sorted array
        print(f"\nSorted array: {A} \n{"-" * 50}\n\n")


if __name__ == "__main__":
    main()