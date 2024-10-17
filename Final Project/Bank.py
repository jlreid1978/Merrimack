from Account import Account
from BankUtility import BankUtility
import numpy as np

# Bank class creates the account instance and holds it in an array
# This class also interacts directly with the array
class Bank:
    # set variables for account numbers, pin numbers, max accounts, and hold the account array
    def __init__(self):
        self.acct_min = 10000000
        self.acct_max = 99999999
        self.pin_min = 1
        self.pin_max = 9999
        self.max_accounts = 100
        self.accounts = np.full(self.max_accounts, None)
        self.utility = BankUtility()
        

    # method to add an element until the array is full
    def _add_to_array(self, arr, element):
        # Check if there's space
        if None in arr:
            arr[np.where(arr == None)[0][0]] = element
            return True
        else:
            print("\n\033[31mNo more accounts available\033[0m\n")
            return False


    # method to add account
    def addAccountToBank(self):
        first, last = self.utility.promptUserForString()
        # generates a random PIN based on the PIN min and max variables
        pin = self.utility.generateRandomInteger(self.pin_min, self.pin_max)
        pin = str(pin).zfill(4)

        # generates a random account number based on the account min and max variables
        while True:
            new_account = self.utility.generateRandomInteger(self.acct_min, self.acct_max)
            if new_account not in self.accounts:
                break
        
        # prompts for the SSN, then inserts dashes before storing it
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
        # Sets all variables to the Account instance
        account = Account(new_account)
        account.setFirst(first)
        account.setLast(last)
        account.set_ssn(ssn)
        account.setPIN(pin)
        valid_acct = self._add_to_array(self.accounts, account)

        if valid_acct:
            return account, account.getPIN()
        return "\n\033[31mProblem creating account\033[0m\n"            


    # method to remove account
    def removeAccountFromBank(self, account):
        if account in self.accounts:
            index = np.where(self.accounts == account)[0][0]
            self.accounts[index] = None
            return True
        return False
    

    # method to find account in the accounts array
    def findAccount(self, user_account):
        for account in  self.accounts:
            if account is not None and account.getAccount() == user_account:
                return account
        return None


    # bonus method to add monthly interest to all accounts
    def addMonthlyInterest(self, percent):
        percent = float(percent) / 100
        for account in self.accounts:
            if account is not None:
                try:
                    acct_bal = account.getBal()
                    deposit = round(acct_bal * percent)
                    new_bal = account.deposit(deposit)
                    dep = self.utility.cashFromCents(deposit)
                    new_bal = self.utility.cashFromCents(new_bal)
                    print(f"\n\033[32mDeposited interest: ${dep} into account: {account}")
                    print(f"New balance: ${new_bal}\033[0m\n")
                except ValueError:
                    return False
        return True
    