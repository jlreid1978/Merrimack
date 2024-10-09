class TreeNode:
        
    def __init__(self, creature):
        self.creature = creature
        self.children = []

    def add_child(self, child_branch):
        self.children.append(child_branch)


    def _get_creatures(self):
        mythical = {self.creature: []}
        for child in self.children:
            mythical[self.creature].append(child.creature)
        for child in self.children:
            child_result = child._get_creatures()
            if child_result:
                mythical[self.creature].append(child_result)
            elif self.creature not in mythical:
                mythical[self.creature].append()
        
        return mythical
    

    def display(self):
        mythical = self._get_creatures()
        result = self.flatten_mythical(mythical)
        centered_result = self.centered_display(result)
        aligned_result = self.position_grandchildren(centered_result, mythical)
        if len(aligned_result) > 1:
            final_result = self.add_arrows(aligned_result)
        else:
            final_result = aligned_result


        for line in final_result:
            print(line)


    def find_branch(self, name):
        """Recursive method to find a node by name."""
        if self.creature == name:
            return self
        for child in self.children:
            result = child.find_branch(name)
            if result:
                return result
        return None


    def flatten_mythical(self, mythical):
        master_list = []

        # Function to handle the recursive flattening
        def recursive_flatten(key, values):
            # Append the parent key
            master_list.append(key)

            # List to hold direct children
            children = []
            nested_children = []
            # Iterate over values to process strings and dictionaries
            for value in values:
                
                if type(value) == str:
                    children.append(value)

            if children:
                children = ("    ".join(children))
                master_list.append(children)

            for value in values:
                
                if type(value) == dict:
                    for nested_key, nested_values in value.items():
                        nested_children.append(nested_key)  # Append the nested key
                        # Append grandchildren if they exist
                        for grandchild in nested_values:
                            if isinstance(grandchild, str):
                                master_list.append(grandchild)  # Append grandchildren


        # Process the main dictionary
        for creature, children in mythical.items():
            recursive_flatten(creature, children)

        return master_list


    def centered_display(self, result):
        max_length = max(len(line) for line in result)
        centered_result = []

        # Center-align each level and place grandchildren under their parent
        for i, line in enumerate(result):
            # Center-align each line based on max_length
            if i == 0:
                # Center the root
                centered_result.append(line.center(max_length))
            elif i == 1:
                # Center the children under the root
                centered_result.append(line.center(max_length))
            else:
                # Center grandchildren under the parent
                centered_result.append(line)

        return centered_result


    def position_grandchildren(self, centered_result, mythical):
        aligned_result = []
        index_map = {}  # To keep track of the index of each parent in centered_result

        # Create an index map for parents
        for index, line in enumerate(centered_result):
            if index == 0:  # The root
                index_map[0] = 0  # Root index
            elif index == 1:  # The children
                children = line.split()  # Split children by whitespace
                for child in children:
                    index_map[child] = index  # Map child to its line index

        # Add the root to the aligned result
        aligned_result.append(centered_result[0])

        # Add children and grandchildren, aligning them correctly
        for line_index in range(1, len(centered_result)):
            line = centered_result[line_index]
            if line_index == 1:  # Children
                aligned_result.append(line)  # Add children line
            else:  # Grandchildren
                # Extract grandchildren based on the mythical dictionary
                for parent, values in mythical.items():
                    for value in values:
                        if isinstance(value, dict):
                            for nested_key, nested_values in value.items():
                                for grandchild in nested_values:
                                    if isinstance(grandchild, str):
                                        # Find the parent line index
                                        parent_index = index_map.get(nested_key)
                                        if parent_index is not None:
                                            # Align grandchildren under their parent
                                            aligned_result.append(" " * (len(centered_result[parent_index]) // 2) + grandchild)

        return aligned_result


    def add_arrows(self, aligned_result):
        final_result = []
        children = []
        grandchildren = []
        slash = ["/", "|", "\\"]
        final_result.append(aligned_result[0])

        word = aligned_result[1].split(" ")
        counter = 0
        slasher = []
        for w in word:
            
            if len(w) > 1:
                wlen = len(w)
                slasher.append((counter + wlen) / 1.25)
            else:
                counter += 1

        counter = 0
        for numb in slasher:
            if counter < 2: 
                insert = " " * int(numb) + slash[counter]
            else:
                insert = " " * int(numb) + slash[2]

            children.append(insert)
            counter += 1

        children = "".join(children)
        final_result.append(children)
        final_result.append(aligned_result[1])

        print(aligned_result)
        if len(aligned_result) > 2:
            slasher = []
            
            word = aligned_result[2].split(" ")
            counter = 0

            for w in word:
                
                if len(w) > 1:
                    wlen = len(w)
                    slasher.append((counter + wlen) / 1)
                else:
                    counter += 1

            counter = 0
            for numb in slasher:
                if counter < 2: 
                    insert = " " * int(numb) + slash[counter]
                else:
                    insert = " " * int(numb) + slash[2]

                grandchildren.append(insert)
                counter += 1

            grandchildren = "".join(grandchildren)
            final_result.append(grandchildren)
            final_result.append(aligned_result[2])


            if len(aligned_result) > 3:
                i = 3
                while True:
                    try: 
                        final_result.append(aligned_result[i])
                        i =+ 1
                    except Exception:
                        break
            

        return final_result



def addChildren(root):
    print("\n====Creatures====")
    root.display()
    print("=================\n")

    # Add children to the root
    parent_name = input("Who is the parent? ")
    new_child = input("What is the name of the new child? ")

    # Find parent node
    parent_node = root.find_branch(parent_name)
    if parent_node:
        parent_node.add_child(TreeNode(new_child))
        print(f"\n\033[32mAdded {new_child} under {parent_name}.\033[0m\n")
    else:
        print(f"\n\033[31mParent '{parent_name}' not found in the tree.\033[0m\n")



def printAll(root):
    root.display()



def makeRoot():
    creature = input("Please input root creature. ")
    root = TreeNode(creature)
    return root


def printSelected(root):
    print(root.levels)

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
