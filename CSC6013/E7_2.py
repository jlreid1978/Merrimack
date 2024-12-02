# Mergesort
# 2. TracetheMergesortalgorithmforthefollowingarrays.Showtoeachrecursive call the two input and output arrays.
# a. A=[38,21,39,60,-1,10,81,23]
# b. B=[2,97,5,88,9,72,12,64,17,56,21]
# c. C = [100, 33, 22, 213, 65, 29, 153, 199, 47, 181, 85]


def mergesort(A):
    if len(A) <= 1:
        return A
    else:
        mid = len(A) // 2
        left = mergesort(A[:mid])
        right = mergesort(A[mid:])
        return merge(left, right)

def merge(left, right):
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
    return result

A = [3, 1, 6, 8, 4, 5, 7, 2]
A = mergesort(A)
print(A)




def main():
    return True


if __name__ == "__main__":
    main()