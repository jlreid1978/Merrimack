# import BankManager
# import Account
# import Bank
# import BankUtility
# import CoinCollector


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





def main():
    selection = menu()
    while True:
        print("What do you want to do? ")
        for s in selection:
            print(s)

        try:
            option = int(input())
            if option in range(1, (len(selection) - 1)):
                break
            else:
                raise ValueError
        except ValueError:
            print("Please enter a valid selection.")



if __name__ == "__main__":
    main()