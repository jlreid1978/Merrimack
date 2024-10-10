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

    @staticmethod
    def promptForAccountNumberAndPIN(bank):
        user_acct = input("Please enter your account number. ")
        user_pin = input("Please enter your PIN number. ")

        return user_acct, user_pin 
    

    def _branchOpen(self, option):
        utility = BankUtility()
        bank = Bank()

        if option == 1:
            print(self.menu[option])
            new_account, pin = bank.createAccount(utility)
            print(f"\n\033[32mYour new account number is {new_account}.")
            print(f"Your new pin number is {pin}.\033[0m\n")

        elif option == 2:
            
            user_account, user_pin = self.promptForAccountNumberAndPIN(bank)

            # Do something with account and pin
            print(f"User account {user_account} pin {user_pin}")

            account = Account(bank, user_account)
            if account:
                print(f"account = {account}")

            else:
                print("No account found.")

        else:
            print(self.menu[option])
    

    # main module to run the program
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

