import array

def matrix():
    matrix = [ ["a", "b", "c"],
                ["d", "e", "f"],
                ["g", "h", "i"]]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j])


def main():
    gridArray = ["1", "2", "3", "4"], ["5", "6", "7", "8"]
    for i in range(len(gridArray)):
        print(gridArray[i][0])

if __name__ == "__main__":
    main()