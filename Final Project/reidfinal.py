import Account
import Bank
from BankManager import BankManager
from BankUtility import BankUtility
import CoinCollector
from getpass import getpass


def menu():
    selection = [
        "=====================================================",
        "1. Open an account",
        "2. Get account informatio and balance",
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
    
    return selection


def branchOpen(manager, selection, option):
    banker = BankUtility()

    if option == 1:
        print(selection[option])
        new_account = manager.createAccount(banker)
        try:
            pin_one = int(getpass("Please enter a four digit pin number. "))
            pin_two = int(getpass("Please re-enter your pin number. "))

            if len(str(pin_one)) != 4 or pin_one != pin_two:
                raise ValueError
            
            else:
                print("Account Created")

        except ValueError:
            print("\n\033[31mInvalid pin format, or pin did not match, please try again.\033[0m\n")
        print(new_account)
    else:
        print(selection[option])


def main():
    manager = BankManager()
    selection = menu()
    while True:
        print("What do you want to do? ")
        for s in selection:
            print(s)

        try:
            option = int(input())
            if option in range(1, (len(selection) - 1)):
                if option == 11:
                    print("\n\033[32mGoodbye\033[0m\n")
                    break
                else:
                    branchOpen(manager, selection, option)
            else:
                raise ValueError
        except ValueError:
            print("\n\033[31mPlease enter a valid selection.\033[0m\n")



if __name__ == "__main__":
    main()