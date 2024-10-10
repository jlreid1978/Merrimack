class Bank:
    __knox = {}

    def __init__(self):
        self.acct_min = 10000000
        self.acct_max = 99999999
        self.pin_min = 1
        self.pin_max = 9999


    def createAccount(self, utility):

        while True:
            new_account = utility.generateRandomInteger(self.acct_min, self.acct_max)
            if new_account not in self.__knox:
                pin = self.addAccountToBank(utility, new_account)
                return new_account, pin

    def addAccountToBank(self, utility, account):
        first = input("Please enter your first name. ")
        last = input("Please enter your last name. ")
        pin = utility.generateRandomInteger(self.pin_min, self.pin_max)
        pin = str(pin).zfill(4)
        
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
        Bank.__knox[account] = [{"pin": pin}, {"bal": 0}, {"first": first}, {"last": last}, {"ssn": ssn}]


        # DEBUG
        print(Bank.__knox)
        return pin
            

    def removeAccountFromBank(account):
        # be sure to change this as needed
        return False
    

    def findAccount(self, account):
        if account in Bank.__knox:
            acct_info = Bank.__get_acct
            return acct_info
        
        else:
            return None


    def addMonthlyInterest(percent):
        # EXTRA CREDIT
        return
    


    def __get_acct(account_num):
    
        acct_pin = Bank.__knox[account_num][0]["pin"]
        acct_first = Bank.__knox[account_num][0]["first"]
        acct_last = Bank.__knox[account_num][0]["last"]
        acct_ssn = Bank.__knox[account_num][0]["ssn"]
        acct_bal = Bank.__knox[account_num][0]["bal"]

        return [acct_pin, acct_first, acct_last, acct_ssn, acct_bal]


