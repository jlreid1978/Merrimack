from Account import Account
from Bank import Bank
from BankUtility import BankUtility
from CoinCollector import CoinCollector

class BankManager:
    def __init__(self):
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
            user_pin = input("Please enter your PIN number. ")
            valid_pin = account.isValidPIN(user_pin)
            if valid_pin:
                pass
            else:
                print("\n\033[31mInvalid PIN number\033[0m\n")
        else:
            print("\n\033[31mNo account found\033[0m\n")

        return account, valid_pin
    

    # module to process user selection
    def _branchOpen(self, bank, utility, option):

        if option == 1:
            print(self.menu[option])
            new_account, pin = bank.addAccountToBank(utility)
            print(f"\n\033[32mYour new account number is {new_account}.")
            print(f"Your new pin number is {pin}.\033[0m\n")

        elif option == 2:
            account, valid_pin = self.promptForAccountNumberAndPIN(bank)
            
            if account and valid_pin:
                account_info = account.toString()
                print(account_info)

        elif option == 3:
            account, valid_pin = self.promptForAccountNumberAndPIN(bank)
            
            if account and valid_pin:
                ### add replace PIN code ###  

            
            




        else:
            print(self.menu[option])
    

    # 1 manditory method main method to run the program
    def main(self):
        utility = BankUtility()
        bank = Bank()

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
                        self._branchOpen(bank, utility, option)
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

