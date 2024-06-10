class FinanceTracker:
    def __init__(self) -> None:
        self.balance = 0
    
    def add_income(self, amount):
        self.balance += amount  
        print(f"Coming {amount} rubles. Now u have {self.balance} rubles")
        
    def add_expense(self, amount):
        self.balance -= amount
        if self.balance < 0:
            print("Error! Your waste is more money than you have")
            self.balance = 0
        else:
            print(f"You expense {amount} rubles. Now u have {self.balance} rubles")
        
    def show_balance(self):
        print(f"Your balance: {self.balance}")
        
def main():
    tracker = FinanceTracker()
    while True:
        print("=" * 15)
        print("1. Add money")
        print("2. Waste money")
        print("3. Show your money")
        print("4. Quit")
        print("=" * 15)
        
        choice = input("Enter a number: ") #need python 3.10 or later for cases :(
        
        if choice == '1':
            amount = float(input("Added money: "))
            if amount <= 0:
                print("You dont get any money, or you entered a num < 0! Try again")
            else:
                tracker.add_income(amount)
        elif choice == '2':
            amount = float(input("wasted money: "))
            tracker.add_expense(amount)
        elif choice == '3':
            tracker.show_balance()
        elif choice == '4':
            print("Bye!")
            break
        else: 
            print("Wrong number, try again")

if __name__ == "__main__":
    main()
    

    
    
