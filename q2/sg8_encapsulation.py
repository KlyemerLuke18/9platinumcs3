#Klyemer Luke S. Colico

class BankAccount:
    def __init__(self, account_number: int, balance: float):
        self.__account_number = account_number
        self.balance = balance 

    #setter methods
    def set_account_number(self, account_number: int):
        self.__account_number = account_number

    def set_balance(self, balance: float):
        if balance < 0:
            print("The balance must not be a negative number.")
        else:
            self.__balance = balance

    #getter methods
    @property
    def account_number(self) -> int:
        return self.__account_number

    @property
    def balance(self) -> float:
        return self.__balance

    #setter for @property syntax
    def balance(self, balance: float):
        self.set_balance(balance)


if __name__ == "__main__":
    a1 = BankAccount(12345, 1000)

    # demonstrate public getters
    print("Account 1")
    print(f"Account Number: {a1.account_number}")
    print(f"Balance: {a1.balance}")

    a1.set_balance(-100)
    print("\nUpdate balance to -100")
    print(f"Account Number: {a1.account_number}")
    print(f"Balance: PHP {a1.balance}")