class Folder:
    def __init__(self, parent=None):
        self.parent = parent
        self.folders = {}

    def add_file(self, active, file):
        print(f"\nAdding file {file} to {active}.\n")
        if file not in self.folders[active]:
            self.folders[active].append(file)
        else:
            print(f"\n\033[31mFile {file} already exists in {active}.\033[0m\n")
        print(self.folders)    
    

    def add_subfolder(self, active, new_folder):
        print(f"\nAdding folder {new_folder} to {active}.\n")
        if new_folder not in self.folders[active]:
            self.folders[active].append({new_folder: []})
        else:
            print(f"\n\033[31mSubfolder {new_folder} already exists in {active}.\033[0m\n")
        print(self.folders) 
    
    def select_folder(self):
        print("selecting folder")


    def __count_files(self):
        print("counting files")

    
    def __eq__(self, other):
        if instance(other, Folder):
            return self.parent == other.parent
        return False

    
    def __len__(self):
        return len(self.folders)

    
    def __str__(self):
        return str(self.folders)



def menu(tree, active):
    master_list = {
        0: [f"\n---Menu---\n--Current Folder: {active}--", "null"],
        1: ["1. Add File", addFile], 
        2: ["2. Add Folder", addFolder],
        3: ["3. SelectFolder", selectFolder],
        4: ["4. Print Folder", printFolder],
        5: ["5. Exit", exit]
    }

    # Split the master list (dictionary) into multiple lists for easier handling by Main.
    numbers = list(master_list.keys())
    to_do = []
    choices = []

    for m in master_list.values():
        to_do.append(m[1])
        choices.append(m[0])

    return numbers, choices, to_do


def addFile(tree, active, run= True):
    file = input(f"Please input a file name to add to {active}.  ")
    tree.add_file(active, file)
    return run, active


def addFolder(tree, active, run= True):
    new_folder = input(f"Please input a subfolder name to add to {active}.  ")
    tree.add_subfolder(active, new_folder)
    return run, active


def selectFolder(tree, active, run= True):
    print("selecting a folder")
    return run, active


def printFolder(tree, active, run= True):
    print("printing directory")
    return run, active


# Function to exit the program
def exit(player, active="", run=False):            
    print("\n\033[32mShutting Down.\nHave a nice day.\033[0m\n")
    return run, active


def main():
    tree = Folder()
    tree.folders.update({"Start Folder": []})
    active, = tree.folders
    run = True

    while run is True:
        numbers, choices, to_do = menu(tree, active)
    
        for n in numbers:
            print(choices[n], end="\n")

        try:
            user_choice = int(input("\nPlease make a selection. "))
            if user_choice not in numbers[1:]:
                raise ValueError
        except ValueError:
            print("\n\033[31mInvalid selection, please try again.\033[0m\n")
            continue

        try:
            selection = to_do[user_choice]
            run, active = selection(tree, active)
        except (KeyError, ValueError) as e:
            print(f"\n\033[31mThere was an error with that selection.\n{e}\nPlease try again.\033[0m\n")


if __name__ == "__main__":
    main()