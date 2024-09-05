from random import randint

# Sets up random ship locations returning as a set of five
def ships(height, width):
    ships = set()
    while len(ships) != 5:
        shiph = randint(1, height - 1)
        shipw = randint(1, width - 1)
        ships.add((str(shiph) + ":" + str(shipw)))

    return ships


# Initially creates the cell by adding the location of the ships then replace the remaining values with a punctuation mark
def cellMod(cell, location):
    for l in location:
        l_key = int(l.split(":")[0])
        l_value = int(l.split(":")[1])
        for c in cell:
            if l_key == c:
                for i in range(len(cell[c])):
                    if l_value == (cell[c][i]):
                        cell[c][i] = "S"  
    for c in cell:  
        for i in range(len(cell[c])):
                if cell[c][i] != "S":
                    cell[c][i] = "."

    return cell              


# Prints the grid
def grid(height, width, cell):
    border = "+ーーー" * width + "+"
    print((" " * round(len(border) / 2 + 10)), "BATTLE SHIP")
    for i in range(height + 1):
        print(border)
        if i < height and i > 0:
            for k, v in cell.items():
                if k == i:
                    print(("| " + str(i - 1) + "   |  "), ("   |  ".join(str(l) for l in cell[i]) + "  |"))
        elif (i - 1) < 0:
            print("|      |  " + "   |  ".join(str(i - 1) for i in range(1, width)) + "   |")


# Requests a guess of where to fire a shot and evaluates the value against a playable space or already guessed location
def guess(cell):
    try:
        column_guess = int(input("What column would you like to fire upon? (X) "))
        if (column_guess + 1) not in cell:
            raise(ValueError)
        row_guess = int(input("What row would you like to fire upon? (Y) "))
        if (row_guess) not in range(0, len(cell)):
            raise(ValueError)
    except Exception:
        print("\n\n\033[31mInvalid coordinants (0 - 9)\033[0m\n")

    return column_guess, row_guess


# Checks the status of the user's guess and updates board accordingly
def statusCheck(cell, column_guess, row_guess):
    for c in cell:
        if row_guess == (c - 1):
            for i in range(len(cell[c])):
                if i == column_guess:
                    if cell[c][i] == "S":
                        print("\n\033[32mDirect hit\033[0m\n")
                        cell[c][i] = "X"
                    elif cell[c][i] == "O" or cell[c][i] == "X":
                        print("\n\033[31mYou have already guessed this location\033[0m\n")
                    else:
                        print("\n\033[31mYou missed\033[0m\n")
                        cell[c][i] = "O"


# Function for gameplay loop. Checks status of the board, coordinates user request, then validates
def game(height, width, cell):
    while True:
        hit = 0
        miss = 0
        ships = 0
        for c in cell:
            for i in range(len(cell[c])):
                    if cell[c][i] == "S":
                        ships += 1
                    elif cell[c][i] == "O":
                        miss += 1
                    elif cell[c][i] == "X":
                        hit += 1

        grid(height, width, cell)
        print(f"{ships} ships still afloat, with {hit} hits and {miss} misses.")
        if ships != 0:
            try:
                column_guess, row_guess = guess(cell)
                statusCheck(cell, column_guess, row_guess)
            except Exception:
                pass
        else:
            total = (hit + miss)
            print(f"\n\033[32mGAME OVER\033[0m \nYou won in {total} tries.\n")
            break


def main():
    height = 11
    width = 11
    cell_start = {i: list(range(1, width)) for i in range(1, height)}
    location = ships(height, width)
    cell = cellMod(cell_start, location)
    game(height, width, cell)


if __name__ == "__main__":
    main()