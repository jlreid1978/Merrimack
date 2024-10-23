from BankUtility import BankUtility

# Account class, which holds all the account info for each instance
class Account:
    def __init__(self, account):
        self._account = str(account)
        self._first = ""
        self._last = ""
        self._ssn = ""
        self._pin = ""
        self._bal = 0
        self.utility = BankUtility()


    # getters and setters for all variables
    def getAccount(self):
        return self._account


    def getFirst(self):
        return self._first
    

    def getLast(self):
        return self._last
    

    def get_ssn(self):
        return self._ssn
    

    def getPIN(self):
        return self._pin
    

    def getBal(self):
        return self._bal
    

    def setFirst(self, first_name):
        self._first = first_name

    
    def setLast(self, last_name):
        self._last = last_name


    def set_ssn(self, user_ssn):
        self._ssn = user_ssn

    
    def setPIN(self, user_pin):
        self._pin = user_pin


    # method for making a deposit
    def deposit(self, amount):
        self._bal = self._bal + amount
        return self._bal


    # method for making a withdrawl
    def withdraw(self, amount):
        self._bal = self._bal - amount
        return self._bal


    # method to validate PIN
    def isValidPIN(self, pin):
        if pin == self._pin:
            return True

        return False
    

    # method to obtain account info
    def toString(self):
        cash = self.utility.cashFromCents(self._bal)
        acct = [
            "\n========================================\n",
            f"Account Number: {self._account}\n",
            f"Owner First Name: {self._first}\n",
            f"Owner Last Name: {self._last}\n"
            f"Owner SSN: {self._ssn}\n",
            f"PIN: {self._pin}\n",
            f"Balance: ${cash}\n"
            "========================================\n"
            ]
        
        acct_info = "".join(acct)

        return acct_info


    def __repr__(self):
      return self._account
