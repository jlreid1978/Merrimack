from linkedlist import LinkedList

def main():
    e_list = [76, 88, 11, 34, 56, 91]
    jrlist = LinkedList()
    jrlist.printList("List created")

    for num in e_list:
        jrlist.insertBeginning(num)
        jrlist.printList(f"Inserting {num} at Beginning")

    jrlist.resetCurrent()
    for i in range(2):
        jrlist.nextCurrent()
    jrlist.printList("Moving Current to the third element of the list")

    jrlist.removeCurrentNext()
    jrlist.printList("Removing the next to current element")  

    jrlist.insertCurrentNext(23)
    jrlist.printList("Inserting 23 next to the current element")

if __name__ == "__main__":
    main()