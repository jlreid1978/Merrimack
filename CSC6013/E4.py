
def DFS(V, E):
    index_to_letter = list(V)
    print(V)

    def __visit(i, count):
        V[i], count = count, count+1
        for e in E:
            if "A" in e:
                print(f"Vertex A visited and received the stamp {count}\n{V}")
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
