
def DFS(V, E):
    # initialize counter to prevent duplicate tags for stamp printing
    a_count = None
    # initialize a list to convert V to when it is changed to int instead of str
    index_to_letter = list(V)

    def __visit(i, count):
        nonlocal a_count
        V[i], count = count, count+1
        for e in E:

            # Every time A is visited, what the count is, and V array is at the time
            if "A" in e and a_count != count:
                a_count = count
                print(f"Vertex A visited and received the stamp {count}\nV array: {V}")
            l = 0
            check = None
            for letter in index_to_letter:
                
                if letter == e[1]:
                    check = l
                l += 1

            if (e[0] == index_to_letter[i]) and (V[check] == -1):
                count = __visit(check, count)

        return count


    for i in range(len(V)):
        V[i] = -1
    count = 0
    for i in range(len(V)):
        if (V[i] == -1):
            
            count = __visit(i, count)
            # DFS call using Vertex A
            if index_to_letter[i] == "A":
                print("DFS called for vertex A")
                  

# an array with all verticies holding information if they are visited or not
V = ["A", "B", "C", "D", "E", "F", "G", "H"]
# an adjacency list of edges with triplets
E = [
    ["A", "E", 1], ["A", "H", 1],
    ["B", "A", 1],
    ["C", "F", 1], ["C", "G", 1],
    ["D", "A", 1], ["D", "E", 1],
    ["E", "C", 1],
    ["F", "D", 1], ["F", "E", 1],
    ["G", "B", 1], ["G", "E", 1],
    ["H", "D", 1]
]

#
DFS(V, E)
#print(V)
