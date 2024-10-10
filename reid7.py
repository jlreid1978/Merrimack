# Set TreeNode class where all tree data is created and manipulated
class TreeNode:
    # creature is the root creature the children are the root creatures family    
    def __init__(self, creature):
        self.creature = creature
        self.children = []


    # method to add a child or grandchild
    def add_child(self, child_branch):
        self.children.append(child_branch)


    # method to create a dictionary from the stored family (I found a dictionary easiest to manipulate)
    def get_creatures(self):
        mythical = {self.creature: []}
        for child in self.children:
            mythical[self.creature].append(child.creature)
        for child in self.children:
            child_result = child.get_creatures()
            if child_result:
                mythical[self.creature].append(child_result)
            elif self.creature not in mythical:
                mythical[self.creature].append()
        
        return mythical
    

    # module to control the manipulation to print the tree
    def display(self):
        mythical = self.get_creatures()
        result = self._flatten_mythical(mythical)
        centered_result = self._centered_display(result)
        if len(centered_result) > 2:
            aligned_result = self._position_grandchildren(centered_result, mythical)
        else:
            aligned_result = centered_result
        if len(centered_result) > 1:
            final_result = self._add_arrows(aligned_result)
        else:
            final_result = centered_result

        for line in final_result:
            print(line)


    # used by the add children function to find the correct place in the tree
    def find_branch(self, name):
        if self.creature == name:
            return self
        for child in self.children:
            result = child.find_branch(name)
            if result:
                return result
        return None


    # method to take the mythical tree dictionary and turn it into a list for further manupilation
    def _flatten_mythical(self, mythical):
        master_list = []

        # Function to handle the recursive flattening key = root, values = children/grandchildren
        def recursive_flatten(key, values):
            # adds root creature to the list
            master_list.append(key)
            children = []
            grandchildren = []
            nested_children = []

            # Iterate over values to process values into children
            for value in values:
                
                if type(value) == str:
                    children.append(value)

            if children:
                # Sets spacing between children
                children = ("     ".join(children))
                master_list.append(children)

            # Iterate over values to process values into grandchildren
            for value in values:
                
                if type(value) == dict:
                    for nested_key, nested_values in value.items():
                        nested_children.append(nested_key)

                        # Append grandchildren if they exist
                        for grandchild in nested_values:
                            if type(grandchild) == str:
                                grandchildren.append(grandchild)
                        
                    if grandchildren:
                        # less spacing for grandchildren as to not skew the tree
                        grandchildren = (" ".join(grandchildren))
                        master_list.append(grandchildren)
                        break
                            
        # final processing of the main dictionary
        for creature, children in mythical.items():
            recursive_flatten(creature, children)

        return master_list


    # method to center the root above the children
    def _centered_display(self, result):
        max_length = max(len(line) for line in result)
        centered_result = []

        # Center-align each level and place grandchildren under their parent
        for i, line in enumerate(result):
            # Center-align each line based on max_length
            if i == 0:
                # center the root
                centered_result.append(line.center(max_length))
            elif i == 1:
                # center the children under the root
                centered_result.append(line.center(max_length))
            else:
                # adds grandchildren, which will be centered later
                centered_result.append(line)

        return centered_result


    # method to align the grandchildren under their parents
    def _position_grandchildren(self, centered_result, mythical):
        aligned_result = centered_result
        grandchildren = []
        aligned = []
        tree = list(mythical.values())[0]
        grandchildren = (centered_result[2]).split(" ")

        # itirate over each grandchild
        for grandchild in grandchildren:
            # locate the grandchild's parent
            for branch in tree:
                if type(branch) == dict:
                    branch_key = list(branch.values())
                    if grandchild in branch_key[0]:
                        daddy = list(branch.keys())[0]
                        break

            index = (centered_result[1].find(daddy))
            index = float(index) / 1.5
        grandchildren = " ".join(grandchildren)
        # adds the proper spacing to create the alignment
        aligned.append((" " * int(index) + grandchildren))
        # adds the alligned grandchildren to the list
        aligned_result[2] = " ".join(aligned)

        return aligned_result


    # adding the dreaded arrows (easily the most complex part of the script)
    def _add_arrows(self, aligned_result):
        final_result = []
        children = []
        grandchildren = []
        # choices for arrows
        slash = ["/", "|", "\\"]
        # do not touch the root creature
        final_result.append(aligned_result[0])
        # find the location of the children to position the arrows
        word = aligned_result[1].split(" ")
        counter = 0
        slasher = []
        for w in word:
            
            if len(w) > 1:
                wlen = len(w)
                slasher.append((counter + wlen) / 1.25)
            else:
                counter += 1
        # take the location and space the arrows
        counter = 0
        for numb in slasher:
            if counter < 2: 
                insert = " " * int(numb) + slash[counter]
            else:
                insert = " " * int(numb) + slash[2]

            children.append(insert)
            counter += 1
        # apply formatting for arrows going from the root creature to the children
        children = "".join(children)
        final_result.append(children)
        final_result.append(aligned_result[1])

        # create arrows for grandchildren, if any exist
        if len(aligned_result) > 2 :
            slasher = []
            # find the location of the words
            word = aligned_result[2].split(" ")
            counter = 0

            for w in word:
                
                if len(w) > 1:
                    wlen = len(w)
                    slasher.append((counter + wlen) / 1)
                else:
                    counter += 1
            # properly space the arrows
            counter = 0
            for numb in slasher:
                if counter == 0: 
                    insert = " " * int(numb) + slash[counter]
                elif counter == 1:
                    insert = " " * int(int(numb) / 5 ) + slash[counter]
                else:
                    insert = " " * int(numb) + slash[2]

                grandchildren.append(insert)
                counter += 1
            # add the arrows from children to grandchildren to the final list
            grandchildren = "".join(grandchildren)
            final_result.append(grandchildren)
            final_result.append(aligned_result[2])

            # attempt at adding great grand children (needs more development)
            if len(aligned_result) > 3:
            
                try: 
                    final_result.append(aligned_result[3])
                except Exception:
                    pass
                    
        return final_result


    # Function to add a new child by creating a new instance of TreeNode
def addChildren(root):
    # display the existing tree
    print("\n====Creatures====")
    printAll(root)
    print("=================\n")

    # ask tree info
    parent_name = input("Who is the parent? ")
    new_child = input("What is the name of the new child? ")

    # find parent
    parent_node = root.find_branch(parent_name)
    if parent_node:
        # add child below parent
        parent_node.add_child(TreeNode(new_child))
        print(f"\n\033[32mAdded {new_child} under {parent_name}.\033[0m\n")
    else:
        print(f"\n\033[31mParent '{parent_name}' not found in the tree.\033[0m\n")


# function to print complete tree
def printAll(root):
    root.display()


# function to create the root creature
def makeRoot():
    creature = input("Please input root creature. ")
    root = TreeNode(creature)
    return root


# function to print out a lineage of a requested name
def printSelected(root):
    # get the master dictionary
    mythical = root.get_creatures()
    lineage = []
    daddy = ""
    tree = list(mythical.values())[0]
    root = list(mythical.keys())[0]
    # ask for a specific name
    select = input("Who do you want to research? ")
    lineage.append(select)
    # search for the name, creating a trail of how deep in the tree it is
    i = 0
    while True:
        # check if name is the root creature
        if select in mythical:
            break
        # check if the name has already been found
        elif select == daddy:
                lineage.append(root)
                break
        # search the tree for the name
        else:
            # check if the name is a child
            for branch in tree:
                if type(branch) == str:
                    if branch == select:
                        daddy = branch
                        break
                # check if the name is a grandchild
                elif type(branch) == dict:
                    for node in branch.values():                 
                        if select in node:
                            daddy = list(branch.keys())[0]
                            lineage.append(daddy)
                            select = daddy
                            break
        # give up after five attempts
        i += 1
        if i == 5:
            break

    # select the appropriate comment for where the name was found in the tree
    if select == root:
        print(f"\n{root} is the first of its kind")
    elif len(lineage) > 1:
        history = "\nThe "
        phrase = " is descended from the "
        for line in lineage:
            history = history + line + phrase
        
        index = history.rfind(phrase)
        history = history[:index]
        print(history)
    else:
        print(f"\n\033[31m{select} is not found.\033[0m\n")


# function to create the main menu based on if a root creature exists or not
def makeMenu(root):
    menu = [
        "\n====Menu====",
        "============\n"
    ]
    if not root:
        menu.insert(1, "1. Add Root Creature")

    else:
        extended = [
            "1. Add Creature",
            "2. Print All", 
            "3. Print Specific",
            "4. Exit"
        ]
        menu[1:1] = extended

    return menu  


# main function to create menu and call requested script functions
def main():
    root = None
    while True:
        menu = makeMenu(root)
        menu_len = len(menu) - 1
        
        while True:
            try:
                for line in menu:
                    print(line)
                selection = int(input("Please make a selection. "))

                if selection not in range(1, menu_len):
                    raise ValueError
                else:
                    break

            except ValueError:
                print("\n\033[31mInvalid selection.\033[0m\n")

        
        if menu_len == 2 and selection == 1:
            root = makeRoot()

        elif menu_len > 2 and selection == 1:
            addChildren(root)
        
        elif selection == 2:
            printAll(root)

        elif selection == 3:
            printSelected(root)

        elif selection == 4:
            print("\n\033[32mGoodbye\033[0m\n")
            break


if __name__ == "__main__":
    main()
