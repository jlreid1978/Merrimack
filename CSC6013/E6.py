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



def main():
    values = {64:13, 60:13, 59:13}
    for n , m in values.items():
        print(f"Multiplying {n} and {m} using the Russian Peasant method")
        russian(n, m)

if __name__ == "__main__":
    main() 