# Jesse Reid CSC6013 Coding Project #1 P1.py

from linkedlist import LinkedList

# counter for the previous value and current value
def changing_history(history, L):
    if len(history) < 2:
        history.append(L.getCurrent())
    elif len(history) == 2:
        del history[0]
        history.append(L.getCurrent())
    
    return history


def main():
    history = []
    next = None
    current = None
    # LinkedList structure "L"
    L = LinkedList()
    # create an array "a"
    a = []
    # opens data.txt and saves it to the array "a"
    with open("data.txt", "r") as data:
        for line in data:
            a.append(int(line.strip()))
    # sorts the array
    a.sort()
    # stores the ordered elements into "L"
    for num in a:
        L.insertBeginning(num)
    L.resetCurrent()

    # ask the user for an integer value "x"
    while True:
        try:
            x = int(input("Please provide an integer value "))
            break
        except ValueError:
            pass

    # itirate through L to either find x or find the value > and < x
    while x != L.getCurrent() or (next is not None and x < next):
        current = L.getCurrent()
        L.nextCurrent()
        next = L.getCurrent()
        # puts the next value in history
        history = changing_history(history, L)

        # break if next went too far and reset current to the previous value
        if next is not None and x > next:
            while L.getCurrent() != current:
                now = L.getCurrent()
                if x == now:
                    break
                L.nextCurrent()
            current = L.getCurrent()
            break

        # if x is in the linked list current must be set to the value preceeding x
        elif x == L.getCurrent():
            while L.getCurrent() != history[0]:
                now = L.getCurrent()
                if history[0] == now:
                    break
                L.nextCurrent()
            current = history[1]
            break

        # ensures the linked list is only ran once and reset current to the last value
        elif next is not None and current is not None and next > current:
            while L.getCurrent() != current:
                now = L.getCurrent()
                if x == now:
                    break
                L.nextCurrent()
            current = L.getCurrent()
            break
       
    L.printList("Original linked list")

    # removes x from linked list
    if len(history) == 2 and x == history[1]:
        L.removeCurrentNext()
        L.printList(f"{x} removed")

    # inserts x at the end of a linked list
    elif current < next:
        L.insertCurrentNext(x)
        L.printList(f"{x} inserted at the end")

    # inserts x at the beginning of the linked list
    elif x > current:
        L.insertBeginning(x)
        L.printList(f"{x} inserted at the beginning")

    # inserts between two numbers of the linked list
    else:
        L.insertCurrentNext(x)
        L.printList(f"{x} inserted after {current} and before {next}")


if __name__ == "__main__":
    main()            