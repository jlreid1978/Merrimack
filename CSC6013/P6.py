import random

# Jesse Reid CSC6013 Coding Project P6
# recursive function to execute the Lomuto partition
def lomuto(A, left, right):
    p = A[right]
    i = left
    # itirate through A
    for j in range(left, right):
        if A[j] < p:
            A[i], A[j] = A[j], A[i]
            i += 1
    # final swap for the pivot itself
    A[i], A[right] = A[right], A[i]
    return i


# QuickSelect recursive function that receives an array and the element the user wants to find (k-th smallest)
def QuickSelect(A, left, right, k):
    pvt = lomuto(A, left, right)

    # index of the k-th smallest element
    if pvt == k:
        return A[pvt]
    elif pvt > k:
        # search left part
        return QuickSelect(A, left, pvt - 1, k)
    else:
        # search right part
        return QuickSelect(A, pvt + 1, right, k)


def main():
    A = []
    # generate a random array of 1000 elements to be searched
    for _ in range(1000):
        A.append(random.randint(-2**31, 2**31 - 1))
    
    # ask user for the k-th smallest value
    while True:
        try:
            k = int(input("Please enter the k-th smallest value to search for between 1 - 1000. "))

            if k not in range(1, 1001):
                raise ValueError("Value must be an integer between 1 - 1000.")
            else:
                break

        except ValueError as e:
            print(e)

    # call QuickSelect to search for k-th smallest value
    k_value = QuickSelect(A, 0, len(A) - 1, k - 1)
    # display the searched element
    print(f"The {k}-th smallest value is {k_value}")


if __name__ == "__main__":
    main() 