#!/usr/bin/python3

class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print(f"✅ Deposited ${amount:.2f}")
        print(f"💰 Current Balance: ${self.balance:.2f}\n")

    def withdraw(self, amount):
        if amount > self.balance:
            print("⚠️  Insufficient funds to complete the withdrawal.\n")
        else:
            self.balance -= amount
            print(f"✅ Withdrew ${amount:.2f}")
            print(f"💰 Current Balance: ${self.balance:.2f}\n")

    def get_balance(self):
        print(f"💰 Current Balance: ${self.balance:.2f}\n")


def get_amount(action_type):
    """
    Prompt the user for an amount.
    User can enter 'b' to go back to the main menu.
    Loops until valid input is entered.
    Returns:
        float | None: The amount entered, or None if user goes back.
    """
    while True:
        user_input = input(f"Enter the amount to {action_type} (or 'b' to go back): $").strip().lower()
        if user_input == 'b':
            return None
        try:
            amount = float(user_input)
            if amount < 0:
                print("⚠️  Amount must be positive.")
                continue
            return amount
        except ValueError:
            print("⚠️  Invalid amount. Please enter a number or 'b' to go back.")


def main():
    cb = Checkbook()
    try:
        while True:
            action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()

            if action == 'exit':
                print("👋 Exiting the checkbook program. Goodbye!")
                break

            elif action == 'deposit':
                amount = get_amount("deposit")
                if amount is None:
                    continue  # go back to main menu
                cb.deposit(amount)

            elif action == 'withdraw':
                amount = get_amount("withdraw")
                if amount is None:
                    continue  # go back to main menu
                cb.withdraw(amount)

            elif action == 'balance':
                cb.get_balance()

            else:
                print("⚠️  Invalid command. Please try again.\n")

    except KeyboardInterrupt:
        print("\n\n⛔ Program interrupted by user. Goodbye!")


if __name__ == "__main__":
    main()
