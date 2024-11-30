# Jesse Reid CSC6013 In Class Exercise E6

# 1. TracetheRussianPeasantsMultiplicationalgorithmforthefollowingproducts. Show each recursive call and the final result, as shown in the live session (table).
# a. 64*13 b. 60*13 c. 59*13

# function to recursivly obtain the values needed for Russian Peasant multiplication
def russian(n, m):
    div = []
    mul = []
    peasant_sum = 0
    dcount = 0
    ecount = 0

    print(f"\nRecursivly dividing by {n} and multiplying by {m}")
    # recursivly divide all "n" values by 2
    def division(n):
        if n == 1:
            return div
        else:
            n = int(n/2)
            div.append(n)
            return division(n)
            
    # recursivly multiply all "m" values by 2
    def multiply(m, count):
        if count == 0:
            return mul
        else:
            count -= 1
            m = int(m * 2)
            mul.append(m)
            return multiply(m, count)

    # call the recursive functions
    div = division(n)
    count = len(div)
    mul = multiply(m, count)

    # create the first table
    print(f"\n| {n} | {m} |\n___________\n| /2 | *2 |\n___________\n")
    for i in div:
        
        print(f"| {i} | {mul[dcount]} |")
        dcount += 1
    print("___________\n")


    print("\nChecking the odd numbers in the division list")
    
    # create the second table, checking all odd numbers and adding them
    if n % 2 != 0:
        print(f"\n| {n} | {m} | √ |\n_______________\n| /2 | *2 |\n_______________\n")
        peasant_sum += m
    else:
        print(f"\n| {n} | {m} |   |\n_______________\n| /2 | *2 |\n_______________\n")

    for e in div:
        if e % 2 != 0:
            print(f"| {e} | {mul[ecount]} | √ |")
            peasant_sum += mul[ecount]
        else:
            print(f"| {e} | {mul[ecount]} |   |")
        
        ecount += 1
    print("___________\n")

    print(f"After adding the checked values\n{n} x {m} is {peasant_sum}\n\n")


# Lomuto partition
# 2. Trace the Lomuto partition with the array:
# a. A=[100,33,22,213,65,29,153,199,47,181,85]
# Using A[10] = 85 as pivot the final array will be:
# ● A = [33, 22, 65, 29, 47, 85, 153, 199, 100, 181, 213]
# In your trace, write down to each change in either i or j, stating: the values of i and j, swaps made, 
# and elements divided into lesser than the pivot, greater than the pivot, and yet to compare.

# recursive function to execute the Lomuto partition
def lomuto(A, left, right):
    pivot = A[10]
    # print the stating array and pivot
    print(f"Starting array = {A} with {pivot} as the pivot.\n")
    p = A[right]
    i = left
    # itirate through A
    for j in range(left, right):
        # print the current status of the array and visited values
        print(f"Current array {A}")
        print(f"Elements less than pivot {A[:i]}")
        print(f"Elements greater than pivot {A[i:j]}")
        print(f"Elements not visited {A[j:]}\n")

        # print the current values for j and i
        print(f"j = {A[j]}, i = {A[i]}")
        
        if A[j] < p:
            # indicate that a swap was made
            print(f"{A[j]} < {p}; swapping {A[j]} with {A[i]}")
            A[i], A[j] = A[j], A[i]

            i += 1
            
        else:
            # indicate that no swap was made
            print(f"{A[j]} > {p}; no swap")

    # final swap for the pivot itself
    A[i], A[right] = A[right], A[i]
    print(f"Final swap {A[right]} for {A[i]}\n")

    return i


def main():
    print("Jesse Reid CSC6013 In Class Exercise E6\n\n")
    print("________________________________\nRussian Peasants Multiplication:\n________________________________\n")
    values = {64:13, 60:13, 59:13}
    for n , m in values.items():
        print(f"Multiplying {n} and {m} using the Russian Peasant method")
        russian(n, m)

    print("_________________\nLomuto partition:\n_________________\n")
    A = [100, 33, 22, 213, 65, 29, 153, 199, 47, 181, 85]
    pvt = lomuto(A, 0, len(A)-1)
    print("Lomuto with pivot at", pvt, ":", A[pvt])
    print(f"Final array {A}")
    print(f"\nItems less than pivot {A[:pvt]}")
    print(f"Items greater than pivot {A[pvt+1:]}")

if __name__ == "__main__":
    main() 