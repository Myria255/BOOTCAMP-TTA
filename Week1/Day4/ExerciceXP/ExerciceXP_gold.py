#EXERCISE 1
 #PART 1
class BankAccount:
    def __init__(self, owner, balance=0, username=None, password=None):
        self.owner = owner
        self.balance = balance
        self.username= username
        self.password= password
        self.authenticated = False

    def deposit(self, amount):
        try:
            amount = float(amount)
            if amount <= 0:
                print("Deposit amount must be positive.")
        except ValueError:
            print("Invalid deposit amount.")
        else:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
     
    def withdraw(self, amount):
        try:
            amount = float(amount)
            if amount <= 0:
                print("Withdrawal amount must be positive.")
                return
        except ValueError:
            print("Invalid withdrawal amount.")
        else:
            if amount > self.balance:
                print("Insufficient funds.")
            else:
                self.balance -= amount
            print(f"Withdrawal of {amount} successful. New balance: {self.balance}")
    def authenticate(self, username, password):
        if self.username is None or self.password is None:
            print("No authentication credentials set for this account.")
            return False
        if username == self.username and password == self.password:
            self.authenticated = True
            print("Authentication successful.")
            return True
        else:
            print("Authentication failed. Incorrect username or password.")
            return False
    #withdrawal with authentication
    def withdraw_with_authentication(self, amount, username, password):
        if self.authenticate(username, password):
            self.withdraw(amount)
        else:
            print("Withdrawal failed due to authentication error.")
    #deposit with authentication and minimum balance check
    def deposit_with_authentication(self, amount, username, password):
        if self.authenticate(username, password):
            self.deposit(amount)
        else:
            print("Deposit failed due to authentication error.")

#Part 2

class MinimumBalanceAccount(BankAccount):
    def __init__(self, owner, balance=0, minimum_balance=100):
        super().__init__(owner, balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        try:
            amount = float(amount)
            if amount <= 0:
                print("Withdrawal amount must be positive.")
                return
        except ValueError:
            print("Invalid withdrawal amount.")
        else:
            if self.balance - amount < self.minimum_balance:
                print(f"Cannot withdraw ${amount}. Minimum balance of ${self.minimum_balance} must be maintained.")
            else:
                self.balance -= amount
                print(f"Withdrawal of ${amount} successful. New balance: ${self.balance}")
                
#Part 4

class ATM:
    def __init__(self,account_list,try_limit=3):
        self.account_list = [account_list] if isinstance(account_list, BankAccount) else account_list
        self.try_limit = try_limit
        try:
            try_limit = int(try_limit)
            if try_limit <= 0:
                print("Try limit must be a positive integer. Defaulting to 3.")
                self.try_limit = 3
            else:
                self.try_limit = try_limit
        except ValueError:
            print("Invalid try limit. Defaulting to 3.")
            self.try_limit = 3
        current_try = 0
        while current_try < self.try_limit:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            for account in self.account_list:
                if account.authenticate(username, password):
                    self.current_account = account
                    print("Access granted.")
                    return
            current_try += 1
        print("Too many failed attempts. Access denied.")
    def show_main_menu(self, bank_account): 
        self.current_account = bank_account
        while True:
            print("\nMain Menu:")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                print(f"Your current balance is: ${self.current_account.balance}")
            elif choice == '2':
                amount = input("Enter the amount to deposit: ")
                self.current_account.deposit_with_authentication(amount, self.current_account.username, self.current_account.password)
            elif choice == '3':
                amount = input("Enter the amount to withdraw: ")
                self.current_account.withdraw_with_authentication(amount, self.current_account.username, self.current_account.password)
            elif choice == '4':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        def log_in(username, password):
            for account in self.account_list:
                if account.authenticate(username, password):
                    return account
            return None
    
#Test cases
account1 = BankAccount("Alice", 500, "alice123", "password1")
account2 = MinimumBalanceAccount("Bob", 1000, 200)
atm = ATM([account1, account2])
atm.show_main_menu(account1)
atm.show_main_menu(account2)
