# Jesse Reid CSC6013 coding project P4 #2

def Min(A, start, end):
    print(f"Start value: {A[start]}, end value: {A[end]}")
    if (start == end):
        return end
    else:
        mid = (end + start) // 2
        fst = Min(A, start, mid)
        lst = Min(A, mid + 1, end)
        
        if A[fst] < A[lst]:
            print(f"Returning value {A[fst]} from left slice")
            return fst
        else:
            print(f"Returning value {A[lst]} from right slice")
            return lst


A3 = [44, 63, 77, 17, 20, 99, 84, 6, 39, 52]
print(f"\nOriginal array: {A3}")
i = Min(A3, 0, len(A3) - 1)
print("The minimum number is", A3[i], "at index", i)

A4 = [52, 84, 6, 39, 20, 77, 17, 99, 44, 63]
print(f"\nOriginal array: {A4}")
i = Min(A4, 0, len(A4) - 1)
print("The minimum number is", A4[i], "at index", i)

A5 = [6, 17, 20, 39, 44, 52, 63, 77, 84, 99]
print(f"\nOriginal array: {A5}")
i = Min(A5, 0, len(A5) - 1)
print("The minimum number is", A5[i], "at index", i)
