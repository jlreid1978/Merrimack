# Jesse Reid CSC6013 coding project P4 #1

def binSearch(A, start, end, k):
    mid = (end+start)//2
    # print the mid value based on mid index
    print(f"Mid: {A[mid]}")
    if (start > end):
        return None
    elif (A[mid] == k):
        return mid
    elif (A[mid] > k):
        # if the value is in the second half, split the array to the end
        print(f"Subarray: {A[(mid+1):end+1]}")
        return binSearch(A, mid+1, end, k)

    else:
        # if the value is in the first half, split the array to the beginning
        print(f"Subarray: {A[start:mid]}")
        return binSearch(A, start, mid-1, k)
    

A1 = [99, 67, 56, 51, 44, 39, 38, 23, 21, 17, 11, 2]
# print the original array
print(f"\nOriginal Array: {A1}")
# search for the requested numbers in the array
for i in [44, 56, 42]:
    print("{} is at index {}\n".format(i, binSearch(A1, 0, len(A1)-1, i)))

A2 = [9, 7, 6, 4, 2, 0, -1, -3, -5, -8, -9]
# print the original array
print(f"\nOriginal Array: {A2}")
#search for the requeste numbers in the array
for i in [-1, -7]:
    print("{} is at index {}\n".format(i, binSearch(A2, 0, len(A2)-1, i)))
