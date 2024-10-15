from Bank import Bank
from BankUtility import BankUtility
from CoinCollector import CoinCollector
from getpass import getpass
from math import floor

class BankManager:
    def __init__(self):
        self.utility = BankUtility()
        self.bank = Bank()
        self.coin_collector = CoinCollector()
        self.menu = [
            "=====================================================",
            "1. Open an account",
            "2. Get account information and balance",
            "3. Change PIN",
            "4. Deposit money in account",
            "5. Transfer money between accounts",
            "6. Withdraw money from account",
            "7. ATM Withdrawl",
            "8. Deposit change",
            "9. Close an account",
            "10. Add monthly interest to all accounts",
            "11. End Program",
            "====================================================="
            ]
        


    # 2 manditory method for validating account and pin
    @staticmethod
    def promptForAccountNumberAndPIN(bank):
        account = None
        valid_pin = None

        user_acct = input("Please enter your account number. ")
        account = bank.findAccount(user_acct)
        if account:
            user_pin = getpass("Please enter your PIN number. ")
            valid_pin = account.isValidPIN(user_pin)
            if valid_pin:
                pass
            else:
                print("\n\033[31mInvalid PIN number\033[0m\n")
        else:
            print("\n\033[31mNo account found\033[0m\n")

        return account, valid_pin
    

    def _change_pin(self, account):
        while True:
            try:
                new_pin1 = int(getpass("Please enter your new 4 digit PIN "))
                new_pin2 = int(getpass("please re-enter your new 4 digit PIN "))
                if len(str(new_pin1)) == 4 and (new_pin1 == new_pin2):
                    account.setPIN(str(new_pin1))
                    print("\n\033[32mNew PIN set\033[0m\n")
                    break
                else:
                    raise ValueError
            except ValueError:
                print("\n\033[31mInvalid PIN number\033[0m\n")


    def _atm_calculation(self, atm_transaction):
        twenty = floor(atm_transaction / 20)
        atm_transaction = atm_transaction - (twenty * 20)
        ten = floor(atm_transaction / 10)
        atm_transaction = atm_transaction - (ten * 10)
        five = floor(atm_transaction / 5)
        atm_transaction = atm_transaction - (five *5)

        if atm_transaction == 0:

            print(f"Number of 20-dollar bills: {twenty}")
            print(f"Number of 10-dollar bills: {ten}")
            print(f"Number of 5-dollar bills: {five}")
            return True
        else:
            return False


    def _transaction(self, type):
        while True:
            try:
                if type == "ATM Withdrawl":
                    transaction = int(input(f"Please enter the amount to withdrawl in multiples of $5: "))
                    if transaction % 5 == 0:
                        atm_valid = self._atm_calculation(transaction)
                        if atm_valid:
                            transaction = float(str(transaction) + ".00")
                        else:
                            raise ValueError
                        
                    else:
                        raise ValueError

                else:
                    transaction = float(input(f"Please enter the amount to {type} in dollars and cents (e.g. 3.50): "))

                if len(str(transaction).split(".")[1]) != 2:
                    transaction = f"{transaction:.2f}"

                confirm = input(f"Please confirm the {type} of ${transaction}. ")
                if confirm.lower() == "yes" or confirm.lower() == "y":
                    transaction = self.utility.convertFromDollarsToCents(float(transaction))
                    print(f"\n\033[32mYour {type} was successful\033[0m\n")
                    return transaction
            except ValueError:
                print("\n\033[31mInvalid value\033[0m\n")


    def _transfer(self):
        try:
            sec_acct = int(input("\nPlease enter account number to transfer to: "))
            second_acct = self.bank.findAccount(sec_acct)
            
            if second_acct:
                transaction = float(input("Please enter the amount to transfer in dollars and cents (e.g. 3.50): "))

                if len(str(transaction).split(".")[1]) != 2:
                    transaction = f"{transaction:.2f}"

                confirm = input(f"Please confirm the transfer of ${transaction}. ")
                if confirm.lower() == "yes" or confirm.lower() == "y":
                    transaction = self.utility.convertFromDollarsToCents(float(transaction))
                    transfer_complete = True
                else:
                    raise ValueError
            else:
                print("\n\033[31mInvalid account\033[0m\n")
                raise ValueError
        
        except ValueError:
            transfer_complete = transaction = False

        return transfer_complete, second_acct, transaction


    # module to process user selection
    def _branchOpen(self, option):
        if option == 1:
            print(self.menu[option])
            new_account, pin = self.bank.addAccountToBank()
            print(f"\n\033[32mYour new account number is {new_account}")
            print(f"Your new pin number is {pin}\033[0m\n")

        elif option in range(2, 10):
            account, valid_pin = self.promptForAccountNumberAndPIN(self.bank)
            
            if account and valid_pin:

                if option == 2:
                    account_info = account.toString()
                    print(account_info)

                elif option == 3:
                    self._change_pin(account)

                elif option == 4:
                    deposit = self._transaction("deposit")
                    if deposit:
                        bal = account.deposit(deposit)
                        bal = self.utility.cashFromCents(bal)
                        print(f"\n\033[32mYour new balance is ${bal}\033[0m\n")
                    else:
                        print("\n\033[31mAn error has occurred, please try again\033[0m\n")

                elif option == 5:
                    transfer_complete, second_acct, transaction = self._transfer()
                    if transfer_complete:
                        acct_bal = account.getBal()
                        bal = self.utility.cashFromCents(acct_bal)
                        if transaction < bal:
                            try:
                                bal = account.withdraw(withdrawl)
                                sec_acct_bal = second_acct.getBal()
                                sec_acct_bal = account.deposit(deposit)
                                sec_bal = self.utility.cashFromCents(sec_acct_bal)
                                print("Transfer complete")
                                print(f"New balance in account: {account} is ${bal}")
                                print(f"New balance in account: {second_acct} is ${sec_bal}")
                            except ValueError:
                                print("\n\033[31mAn error occurred during transfer\033[0m\n")

                        else:
                            print("\n\033[31mInsufficient Funds\033[0m\n")
                
                elif option == 6:
                    withdrawl = self._transaction("withdrawl")
                    acct_bal = account.getBal()
                    if withdrawl < acct_bal:
                        bal = account.withdraw(withdrawl)
                        bal = self.utility.cashFromCents(bal)
                        print(f"\n\033[32mYour new balance is ${bal}\033[0m\n")
                    else:
                        print("\n\033[31mInsufficient Funds\033[0m\n")

                elif option == 7:
                    withdrawl = self._transaction("ATM Withdrawl")
                    acct_bal = account.getBal()
                    if withdrawl < acct_bal:
                        bal = account.withdraw(withdrawl)
                        bal = self.utility.cashFromCents(bal)
                        print(f"\n\033[32mYour new balance is ${bal}\033[0m\n")
                    else:
                        print("\n\033[31mInsufficient Funds\033[0m\n")

                elif option == 8:
                    coins = input("Please deposit coins. ").upper()
                    deposit = self.coin_collector.parseChange(coins)
                    if deposit:
                        change = self.utility.cashFromCents(deposit)
                        bal = account.deposit(deposit)
                        bal = self.utility.cashFromCents(bal)
                        print(f"\n\033[32m${change} in coins deposited into account")
                        print(f"Your new balance is ${bal}\033[0m\n")
                    else:
                        print("\n\033[31mAn error has occurred, please try again\033[0m\n")

                elif option == 9:
                    closure_Verify = self.bank.removeAccountFromBank(account)
                    if closure_Verify:
                        print(f"\n\033[32mAccount {account} has been closed\033[0m\n")
                    else:
                        print("\n\033[31mAn error has occurred closing the account\033[0m\n")

        elif option == 10:
            print("Add monthly interest to all accounts")
                      
        else:
            print(self.menu[option])
    

    # 1 manditory method main method to run the program
    def main(self):
        # create the menu
        while True:
            print("What do you want to do? ")
            for selection in self.menu:
                print(selection)

            try:
                # ask which option the user wants to choose
                option = int(input())
                if option in range(1, (len(self.menu) - 1)):
                    if option == 11:
                        print("\n\033[32mGoodbye\033[0m\n")
                        break
                    else:
                        # runs the requested selection
                        self._branchOpen(option)
                else:
                    raise ValueError
            except ValueError:
                print("\n\033[31mInvalid choice\033[0m\n")


# Program can be started from BankManager.py or reidfinal.py
def run():
    manager = BankManager()
    manager.main()


if __name__ == "__main__":
    run()

