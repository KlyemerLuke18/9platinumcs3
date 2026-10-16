#Klyemer Luke S. Colico #name
#empty space
class BankAccount: #creation of bank account class
    def __init__(self, account_number: int, balance: float):  #defining variables
        self.__account_number = account_number #defining account number
        self.balance = balance #defining balance
    def set_account_number(self, account_number: int): #defining the setter of account number and making it integer
        self.__account_number = account_number #returns the value for setting the account number
    def set_balance(self, balance: float): #defining the setter of balance and making it include decimals
        if balance < 0:   #if function when balance is less than 0
            print("The balance must not be a negative number.")  #it prints out "The balance must not be a negative number."
        else: #the exception where balance is equal or greater than 0
            self.__balance = balance #returns the value of balance to itself
    @property #the @property that lets you turn a method into a attribute so you can access it using a dot notation
    def account_number(self) -> int: #defining account number by itself to integer with the at property
        return self.__account_number #returns the value for account number with the at property
    @property #the @property again that lets you turn a method into a attribute so you can access it using a dot notation
    def balance(self) -> float: #defining balance by itself to include decimals with the property
        return self.__balance #returns the value for balance with the at property
    def balance(self, balance: float): #defines balance with self and itself with float
        self.set_balance(balance) #returns the value by setting with itself
if __name__ == "__main__": #the if function where it checks if the file is being run as the main program or if it is used as a module
    a1 = BankAccount(12345, 1000) #setting the values for the account number and balance
    print("Account 1") #prints "Account 1"
    print(f"Account Number: {a1.account_number}") #prints out "Account Number:" and the account number itself
    print(f"Balance: {a1.balance}") #prints out "Balance:" and the balance itself
    a1.set_balance(-100) #setting the balance to -100 and prints out ""The balance must not be a negative number."
    print("\nUpdate balance to -100") #prints "Update balance to -100"
    print(f"Account Number: {a1.account_number}") #prints out "Account Number:" and the account number itself again with no changes
    print(f"Balance: {a1.balance}") #prints out "Balance:" and the balance itself again with no changes
