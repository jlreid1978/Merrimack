class BankManager:
        
        
    # This is where you will implement your method and start
    # the program from. The BankManager class should create an instance
    # of a Bank object when the program runs and use that instance to
    # manage the Accounts in the bank
    
    @staticmethod
    def promptForAccountNumberAndPIN(bank):
        user_acct = input("Please enter your account number. ")
        user_pin = input("Please enter your PIN number. ")

        return user_acct, user_pin
    


                

