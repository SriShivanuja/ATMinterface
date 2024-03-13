class Account:
    def __init__(self, user_id, pin, balance=0):
        self.user_id = user_id
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited ${amount}")
        print("AMOUNT DEPOSITED")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
            print("COLLECT YOUR MONEY")
        else:
            print("Insufficient funds!")

    def transfer(self, recipient, amount):
        if amount <= self.balance:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f"Transferred ${amount} to {recipient.user_id}")
            print("AMOUNT TRANSFERED SUCCESSFULLY")
        else:
            print("Insufficient funds!")

    def get_transaction_history(self):
        return self.transaction_history


class ATM:
    def __init__(self):
        self.users = {
            "user123": Account("user123", "1234", 1000),
            "user456": Account("user456", "5678", 500),
        }
        self.current_user = None

    def authenticate_user(self, user_id, pin):
        if user_id in self.users and self.users[user_id].pin == pin:
            self.current_user = self.users[user_id]
            return True
        else:
            print("Invalid user ID or PIN. Please try again.")
            return False

    def display_menu(self):
        print("\nATM Menu:")
        print("1. Transactions History")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Transfer")
        print("5. Quit")

    def run(self):
        print("Welcome to the ATM!")
        user_id = input("Enter your user ID: ")
        pin = input("Enter your PIN: ")

        if self.authenticate_user(user_id, pin):
            while True:
                self.display_menu()
                choice = input("Enter your choice (1-5): ")

                if choice == "1":
                    print("Transaction History:")
                    for transaction in self.current_user.get_transaction_history():
                        print(transaction)
                elif choice == "2":
                    amount = float(input("Enter the amount to withdraw: "))
                    self.current_user.withdraw(amount)
                    
                elif choice == "3":
                    amount = float(input("Enter the amount to deposit: "))
                    self.current_user.deposit(amount)
                    
                    
                elif choice == "4":
                    recipient_id = input("Enter the recipient's user ID: ")
                    recipient = self.users.get(recipient_id)
                    if recipient:
                        amount = float(input("Enter the amount to transfer: "))
                        self.current_user.transfer(recipient, amount)
                        
                    else:
                        print("Recipient not found.")
                elif choice == "5":
                    print("Thank you for using the ATM. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")


#instance of the ATM class 
atm = ATM()
atm.run()
