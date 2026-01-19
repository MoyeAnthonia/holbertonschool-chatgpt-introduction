#!/usr/bin/env python3
class Checkbook:
    def __init__(self):
        """Initialize the checkbook with a balance of 0.0."""
        self.balance = 0.0

    def deposit(self, amount):
        """
        Function Description:
            Adds the specified amount to the account balance.

        Parameters:
            amount (float): The amount to deposit. Must be non-negative.

        Returns:
            None
        """
        self.balance += amount
        print(f"Deposited ${amount:.2f}")
        print(f"Current Balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        """
        Function Description:
            Subtracts the specified amount from the account balance if funds are sufficient.

        Parameters:
            amount (float): The amount to withdraw. Must be non-negative and ≤ balance.

        Returns:
            None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}")
            print(f"Current Balance: ${self.balance:.2f}")

    def get_balance(self):
        """
        Function Description:
            Displays the current account balance.

        Parameters:
            None

        Returns:
            None
        """
        print(f"Current Balance: ${self.balance:.2f}")


def get_valid_amount(action):
    """
    Prompt the user for a valid numeric, non-negative amount.
    Allows returning to the main menu by entering 'b'.
    Loops until valid input is provided or user chooses to go back.

    Parameters:
        action (str): 'deposit' or 'withdraw', used in the prompt.

    Returns:
        float | None: The valid amount entered, or None if the user chooses to go back.
    """
    while True:
        user_input = input(f"Enter the amount to {action} (or 'b' to go back): $").strip().lower()
        if user_input == 'b':
            return None  # Go back to main menu
        try:
            amount = float(user_input)
            if amount < 0:
                print("Amount cannot be negative. Try again.")
                continue
            return amount
        except ValueError:
            print("Invalid input. Please enter a numeric value or 'b' to go back.")


def main():
    """Main loop to interact with the checkbook."""
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()

        if action == 'exit':
            print("Exiting the checkbook program. Goodbye!")
            break
        elif action == 'deposit':
            amount = get_valid_amount('deposit')
            if amount is None:
                continue  # User chose to go back
            cb.deposit(amount)
        elif action == 'withdraw':
            amount = get_valid_amount('withdraw')
            if amount is None:
                continue  # User chose to go back
            cb.withdraw(amount)
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
