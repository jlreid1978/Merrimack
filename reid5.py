
class Folder:
    # Class variable - dictionary to contain all file-tree structures
    __file_tree = {}

    # Initialize the active instance as well as the file_tree dictionary
    def __init__(self, active=None):
        self.active = active if active else "Start Folder"
        # Initialize the file tree if it's empty
        if not Folder.__file_tree:
            Folder.__file_tree["Start Folder"] = {"files": [], "folders": []}
        
           
    # Method to add a file to the active folder
    def add_file(self, file):
        print(f"\n\033[32mAdding file '{file}' to {self.active}.\033[0m\n")
        if file not in Folder.__file_tree[self.active]["files"]:
            Folder.__file_tree[self.active]["files"].append(file)

        else:
            print(f"\n\033[31mFile '{file}' already exists in {self.active}.\033[0m\n")


    # Method to add a new subfolder to the active folder if the folder does not already exist
    # In addition to the subfolder, it is initialized with an empty set of files and folders.
    def add_subfolder(self, new_folder):
        if new_folder not in self.get_folders():
            Folder.__file_tree[self.active]["folders"].append(new_folder)
            Folder.__file_tree[new_folder] = {"files": [], "folders": []}
            print(f"\n\033[32mFolder '{new_folder}' added successfully.\033[0m\n")

        else:
            print(f"\n\033[31mSubfolder '{new_folder}' already exists in {self.active}.\033[0m\n")


    # Method to move to a new active folder, provided that folder has already been created
    def select_folder(self, new_folder):
        if new_folder in self.get_folders():
            # Additional check to make sure that the user is not already in the folder they are trying to switch to
            if self.__eq__(new_folder):
                print(f"\n\033[31mAlready in folder {new_folder}.\033[0m\n")

            else:
                print(f"\n\033[32mSwitching to folder: {new_folder}.\033[0m\n")
                self.active = new_folder
                
        else:
            print(f"\n\033[31mFolder '{new_folder}' does not exist.\033[0m\n")
    

    # Method to display the current folder's contents, as well as that of the subfolders
    def __str__(self, folder_name=None, depth=0):
        if folder_name is None:
            folder_name = self.active
        
        # Set up indentations for each subfolder 
        indent = "----" * depth
        # Prints current folder as well as a count of files in the active folder and all subfolders
        folder_info = f"{indent}-Folder: {folder_name} (Total Files: {self.__len__()})\n"
        
        # Add files in the current folder
        folder_info += f"{indent}----Files:\n"
        for file in Folder.__file_tree[folder_name]["files"]:
            folder_info += f"{indent}------File: {file}\n"

        # Add subfolders and their contents
        folder_info += f"{indent}----Subfolders:\n"
        for folder in Folder.__file_tree[folder_name]["folders"]:
            folder_info += self.__str__(folder, depth + 1)  # Recursive call to __str__

        return folder_info


    # Recursively counts the total number of files in the folder and all its subfolders.
    def __count_files(self):
        total_files = len(Folder.__file_tree[self.active]["files"])
        for folder in Folder.__file_tree[self.active]["folders"]:
            total_files += Folder(folder).__count_files()  # Recursively count files in subfolders
        return total_files


    # Compares a folder and a string. They are equal if they have the same folder name.
    def __eq__(self, other):
        if isinstance(other, str):
            return self.active == other
        return False


    # Returns the total number of files in the folder and all its subfolders.
    def __len__(self):
        return self.__count_files()


    # Returns a list of folders from the master file_tree dictionary
    @classmethod
    def get_folders(cls):
        return list(cls.__file_tree.keys())


# Creates the menu and sets up ability to select functions
def menu(tree):
    master_list = {
        0: [f"\n---Menu---\n--Current Folder: {tree.active}--", "null"],
        1: ["1. Add File", addFile], 
        2: ["2. Add Folder", addFolder],
        3: ["3. SelectFolder", selectFolder],
        4: ["4. Print Folder", printFolder],
        5: ["5. Exit", exitProgram]
    }

    # Split the master list (dictionary) into multiple lists for easier handling by Main.
    numbers = list(master_list.keys())
    to_do = []
    choices = []

    for m in master_list.values():
        to_do.append(m[1])
        choices.append(m[0])

    return numbers, choices, to_do


# Function to ask for a filename and add it using the add_file module
def addFile(tree, run=True):
    file = input(f"Please input a file name to add to {tree.active}.  ")
    tree.add_file(file)
    return run

# Function to ask for a folder name and add it using the add_subfolder module
def addFolder(tree, run=True):
    new_folder = input(f"Please input a subfolder name to add to {tree.active}.  ")
    tree.add_subfolder(new_folder)
    return run


# Function to ask which folder to make active and switch using the select_folder module
def selectFolder(tree, run=True):
    new_folder = input(f"Please input a folder to switch to.  ")
    tree.select_folder(new_folder)
    return run


# Function to call the __str__ module that will allow printing of the active folder including files and subfolders
def printFolder(tree, run=True):
    print(tree)
    return run


# Function to exit the program
def exitProgram(tree, run=False):            
    print("\n\033[32mShutting Down.\nHave a nice day.\033[0m\n")
    return run


# Main function to run the program
def main():
    tree = Folder()
    run = True

    while run is True:
        active_tree = tree.active
        numbers, choices, to_do = menu(tree)
    
        for n in numbers:
            print(choices[n])

        try:
            user_choice = int(input("\nPlease make a selection. "))
            if user_choice not in numbers[1:]:
                raise ValueError
        except ValueError:
            print("\n\033[31mInvalid selection, please try again.\033[0m\n")
            continue
        try:
            selection = to_do[user_choice]
            run = selection(tree)
        except (KeyError, ValueError) as e:
            print(f"\n\033[31mThere was an error with that selection.\n{e}\nPlease try again.\033[0m\n")


if __name__ == "__main__":
    main()