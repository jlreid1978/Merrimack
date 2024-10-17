import random

# Bank Utility class to provide some small assisting methods  
class BankUtility:
    # method to prompt user for name strings
    def promptUserForString(self):
        first = str(input("Please enter your first name. "))
        last = str(input("Please enter your last name. "))
        return first, last
    
    
    # method to check for a positive number
    def promptUserForPositiveNumber(self, prompt):
        if prompt < 0:
            print("\n\033[31mAmount cannot be negative\033[0m\n")
            raise ValueError
                
        return prompt
    
    
    # method to generate a random int
    def generateRandomInteger(self, min, max):
        new_account = random.randint(min, max)
        return new_account
    
    
    # method to convert FROM dollars TO cents
    def convertFromDollarsToCents(self, cash):
        cash = f"{cash:.2f}"
        change = str(cash).split(".")
        change = int("".join(change))
        return change
    

    # method to convert TO dollars FROM cents
    def cashFromCents(self, change):
        if len(str(change)) > 2:
            cash = str(change)[:-2] + "." + str(change)[-2:]
        else:
            cash = "0." + str(change).zfill(2)

        return cash
    
    '''
    Checks if a given string is a number (long)
    This does NOT handle decimals.
    YOU DO NOT NEED TO CHANGE THIS METHOD
    THIS IS FREE FOR YOU TO USE AS NEEDED
    @param numberToCheck String to check
    @return true if the String is a number, false otherwise
    '''
    
    def isNumeric(numberToCheck):
        try:
            if numberToCheck.isdigit():
                return True
            else:
                return False
        except ValueError:
            return False
