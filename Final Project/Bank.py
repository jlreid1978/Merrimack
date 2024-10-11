from Account import Account
import numpy as np

class Bank:
    __knox = {}

    def __init__(self):
        self.acct_min = 10000000
        self.acct_max = 99999999
        self.pin_min = 1
        self.pin_max = 9999
        self.max_accounts = 5
        self.accounts = np.full(self.max_accounts, None)
        

    # method to add an element until the array is full
    def add_to_array(self, arr, element):
        # Check if there's space
        if None in arr:
            arr[np.where(arr == None)[0][0]] = element
            return True
        else:
            print("\n\033[31mNo more accounts available\033[0m\n")
            return False


    # method to add account
    def addAccountToBank(self, utility):
        first = input("Please enter your first name. ")
        last = input("Please enter your last name. ")
        pin = utility.generateRandomInteger(self.pin_min, self.pin_max)
        pin = str(pin).zfill(4)

        while True:
            new_account = utility.generateRandomInteger(self.acct_min, self.acct_max)
            if new_account not in self.accounts:
                break
        
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
        
        account = Account(new_account)
        account.setFirst(first)
        account.setLast(last)
        account.set_ssn(ssn)
        account.setPIN(pin)

        valid_acct = self.add_to_array(self.accounts, account)

        if valid_acct:
            return account, account.getPIN()
        return "\n\033[31mProblem creating account\033[0m\n"            


    # method to remove account
    def removeAccountFromBank(self, account):
        if account in self.accounts:
            index = np.where(self.accounts == account)[0][0]
            account[index] = None
            return True
        return False
    

    def findAccount(self, user_account):
        for account in  self.accounts:
            if account is not None and account.getAccount() == user_account:
                return account
        return None


    def addMonthlyInterest(self, percent):
        # EXTRA CREDIT
        return
    