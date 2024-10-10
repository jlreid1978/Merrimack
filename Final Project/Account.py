class Account:
    
    def __init__(self, bank, user_account):
        self.acct_info = bank.findAccount(user_account)
    # add your attributes here
    # add methods as getters and setters for attributes

    def deposit(amount):
        # implement deposit here
        return 0

    def withdraw(amount):
        # implement withdraw here
        return 0 # be sure to change this

    def isValidPIN(pin):
        if Account.acct_info[0] == pin:
            return True

        return False # be sure to change this

    # all objects have a toString method - this indicates you are providing
    # your own version

    def __repr__(self):
      return "" # change this as needed
