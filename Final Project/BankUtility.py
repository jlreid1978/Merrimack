import random

class BankUtility:

    def promptUserForString(self):
        first = str(input("Please enter your first name. "))
        last = str(input("Please enter your last name. "))
        return first, last
    
    
    def promptUserForPositiveNumber(prompt):
        # implement promptUserForPositiveNumber here
        return 0.0 # be sure to change this
    
    
    def generateRandomInteger(self, min, max):
        new_account = random.randint(min, max)
        return new_account
    
    
    def convertFromDollarsToCents(self, cash):
        cash = f"{cash:.2f}"
        change = str(cash).split(".")
        change = int("".join(change))
        return change
    

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
