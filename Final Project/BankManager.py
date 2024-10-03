from getpass import getpass

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
        min = 10000000
        max = 99999999
        while True:
            new_account = manager.generateRandomInteger(min, max)
            if new_account not in self.__knox:

                first = input("Please enter your first name. ")
                last = input("Please enter your last name. ")
                pin = manager.generateRandomInteger(1, 9999)
                pin = str(pin).zfill(4)
                
                while True:
                    try: 
                        ssn = input("Please enter your social security number (without dashes). ")
                        if len(ssn) == 9 and ssn.isdigit():
                            ssn = f"{ssn[:3]}-{ssn[3:5]}-{ssn[5:]}"
                            break
                        else:
                            raise ValueError
                    
                    except ValueError:
                        print(f"\n\033[31mInvalid social security number\033[0m\n")
                
                print("Account Created")
                self.__knox[new_account] = [{"pin": pin}, {"bal": 0}, {"first": first}, {"last": last}, {"ssn": ssn}]

                # DEBUG
                print(self.__knox)
                return new_account, pin




                

