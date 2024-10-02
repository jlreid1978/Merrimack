class BankManager:
    def __init__(self):
        self.__knox = {}
        
        # This is where you will implement your method and start
        # the program from. The BankManager class should create an instance
    # of a Bank object when the program runs and use that instance to
    # manage the Accounts in the bank
    
    @staticmethod
    def promptForAccountNumberAndPIN(bank):
        # implement promptForAccountNumberAndPIN here
        # takes one parameter, a Bank object that represents the bank.
        # The method should prompt the user to enter an account number
        # and then try to find a matching account with that account number
        # in the bank.
        return
    

    def createAccount(self, manager):
        min = 100000000
        max = 999999999
        while True:
            new_account = manager.generateRandomInteger(min, max)
            if new_account not in self.__knox:
                return new_account

