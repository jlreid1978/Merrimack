from Account import Account
from Bank import Bank
from BankManager import BankManager
from BankUtility import BankUtility
from CoinCollector import CoinCollector


def menu():
    selection = [
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
    
    return selection


def branchOpen(manager, selection, option):
    banker = BankUtility()

    if option == 1:
        print(selection[option])
        new_account, pin = manager.createAccount(banker)
        print(f"\n\033[32mYour new account number is {new_account}.")
        print(f"Your new pin number is {pin}.\033[0m\n")
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
            print("\n\033[31mInvalid choice\033[0m\n")


if __name__ == "__main__":
    main()