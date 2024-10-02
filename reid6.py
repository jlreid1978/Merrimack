# Create an animal parent class with "default" values
class Animal:
    animals = ["Bear", "Elephant", "Penguin", "Big Cat"]
    zoo = {}
    def __init__(self, beast=None):
        self.species = "one of thousands"
        self.name = "who's in the zoo"
        self.make_sound = "chatter"
        self.info = "is alive somewhere on Earth"
    

# Create a bear child class with specific values
class Bear(Animal):
    def __init__(self, beast):
        super().__init__()
        self.name = input(f"What is the {beast}'s name? ")
        self.species = input(f"What species of {beast} is {self.name}?")
        self.intake = input(f"What color fur does {self.name} have? ")
        self.info = f"have {self.intake} color fur."
        self.make_sound = self.bearSound(self.species)


    # Module to apply specific sounds to bears that do not typically "roar"
    def bearSound(self, species):
        if species.lower() == "american black bear":
            sound = "snort"
        elif species.lower() == "giant panda":
            sound = "bleating"
        elif species.lower() == "sloth bear":
            sound = "huffing"
        elif species.lower() == "sun bear":
            sound = "whine"
        else:
            sound = "roar"
        
        return sound


# Create an elephant child class with specific values
class Elephant(Animal):
    def __init__(self, beast):
        super().__init__()
        self.make_sound = "trumpet"
        self.name = input(f"What is the {beast}'s name? ")
        self.species = input(f"What species of {beast} is {self.name}?")
        while True:
            try:
                self.intake = int(input(f"How much does {self.name} weigh (in kg)? "))
                if self.intake < 0:
                    raise ValueError
                else:
                    break
            except ValueError:
                print("\n\033[31mPlease enter a valid weight in kg (numerically).\033[0m\n")
        self.info = f"weigh {self.intake} kg."


# Create a penguin child class with specific values
class Penguin(Animal):
    def __init__(self, beast):
        super().__init__()
        self.make_sound = "squawk"
        self.name = input(f"What is the {beast}'s name? ")
        self.species = input(f"What species of {beast} is {self.name}?")
        while True:
            try:
                self.intake = float(input(f"How tall is {self.name} (in ft)? "))
                
                if self.intake < 0:
                    raise ValueError
                else:
                    break
            except ValueError:
                print("\n\033[31mPlease enter a valid height in feet (numerically).\033[0m\n")

        self.info = f"is {self.intake} feet tall."
        

# Create a big cat child class with specific values
class BigCat(Animal):
    def __init__(self, beast):
        super().__init__()
        self.name = input(f"What is the {beast}'s name? ")
        self.species = input(f"What species of {beast} is {self.name}?")
        self.intake = self.catClaws(self.species)
        self.info = f"have {self.intake} claws."
        self.make_sound = self.catSound(self.species)

    
    # Module to apply special values for cats that do not "roar"
    def catSound(self, species):
        if species.lower() == "cheetah":
            sound = "chirp"
        # Added house cat as mild humor to the "big cat" category
        elif species.lower() == "house cat":
            sound = "meow"
        else:
            sound = "roar"

        return sound
    

    # Module to apply special values for cats that do not have fully retractable claws
    def catClaws(self, species):
        semi = ["cheetah", "bobcat", "lynx"]
        if species.lower() in semi:
            claws = "semi-retractable"
        else:
            claws = "fully-retractable"
        
        return claws
    

# Function to add animals to the zoo
def addAnimal(beast):
    # Dictionary of animal classes
    animal_classes = {
        "Bear": Bear,
        "Elephant": Elephant,
        "Penguin": Penguin,
        "Big Cat": BigCat
    }
    
    # Create an animal instance and add its details to the zoo
    animal_class = animal_classes.get(beast)
    if animal_class:
        animal = animal_class(beast)

        if beast not in Animal.zoo:
            Animal.zoo[beast] = []

        Animal.zoo[beast].append((animal.name, animal.species, animal.info, animal.make_sound))
    

# Function to print all details for all animals in the zoo
def fullPrint(zoo):
    for animal_type, animals in zoo.items():
        print(f"Type: {animal_type}")
        for animal in animals:
            name, species, info, sound = animal
            details = f"{name} is a {animal_type} of the {species} species. They make a {sound} sound and {info}"
            print(details)
        print("")


# Function to print all details for a specified animal in the zoo
def specificPrint(zoo, beast):
    for animal_type, animals in zoo.items():
        if animal_type == beast:
            print(f"Type: {animal_type}")
            for animal in animals:
                name, species, info, sound = animal
                details = f"{name} is a {animal_type} of the {species} species. They make a {sound} sound and {info}"
                print(details)
            print("")


# Function to create the menu displays based on selection or default value
def menu(item):
    animal = Animal()
    zoo = animal.zoo
    numb = 0
    display = ["\n===Zoo Menu===", "1. Add animals", "2. Print all", "3. Print specific"]
    
    if item == None:
        display = display

    elif item == display[1]:
        display = ["\n===Zoo Menu==="]
        for a in animal.animals:
            numb += 1
            display.append(f"{len(display)}. Add {a}")

    elif item == display[2]:
        fullPrint(zoo)

    elif item == display[3]:
        print("\n===Print Menu===")
        for a in animal.animals:
            numb += 1
            print(f"{numb}. {a}")
        print("==============\n")

        try:
            creature = int(input("Please make a selection. "))
            if creature in range(1, (len(animal.animals) + 1)):
                beast = animal.animals[creature - 1]
                specificPrint(zoo, beast)
            else:
                raise ValueError
        except ValueError:  
            print("\n\033[31mInvalid Entry\033[0m\n")

    else:
        beast = item.split(" ")[2:]
        beast = " ".join(beast)
        addAnimal(beast)
                           
    display.append(f"{len(display)}. Exit")
    display.append("==============")

    return display


# Main function to run the script
def main():
    item = None
    
    while True:
        display = menu(item)
        for d in display:
            print(d)
        
        try:
            selection = int(input("Please make a selection. "))
            if selection == (len(display) - 2):
                print("\n\033[32mGoodbye\033[0m\n")
                break
            elif selection in range(1, (len(display) - 2)):
                item = display[selection]
            else:    
                raise ValueError
  
        except ValueError: 
            selection = None   
            print("\n\033[31mInvalid Entry\033[0m\n")
        
        
if __name__ == "__main__":
    main()