class Category:
    def __init__(self, category_name):
        """Initialize a Category instance with a name and an empty ledger."""
        self.category_name = category_name  # Store the category name
        self.ledger = []  # Initialize an empty ledger list for transactions

    def deposit(self, amount, description=''):
        """Deposit an amount into the category, with an optional description."""
        # Append a dictionary with the deposit amount and description to the ledger
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        """Withdraw an amount from the category if sufficient balance exists."""
        # Check if there's enough balance to withdraw the requested amount
        if self.get_balance() >= amount:
            # Append a negative amount (withdrawal) to the ledger
            self.ledger.append({'amount': -amount, 'description': description})
            return True  # Withdrawal was successful
        return False  # Insufficient funds, withdrawal failed

    def get_balance(self):
        """Calculate and return the current balance of the category."""
        # Sum all amounts in the ledger to determine the total balance
        total = sum(item['amount'] for item in self.ledger)
        return total

    def transfer(self, amount, category):
        """Transfer an amount to another category, updating both ledgers."""
        # Check if sufficient funds are available for the transfer
        if self.check_funds(amount):
            # Withdraw from the current category and deposit into the target category
            self.withdraw(amount, description=f'Transfer to {category.category_name}')
            category.deposit(amount, description=f'Transfer from {self.category_name}')
            return True  # Transfer was successful
        return False  # Transfer failed due to insufficient funds

    def check_funds(self, amount):
        """Check if the category has sufficient funds for the specified amount."""
        return amount <= self.get_balance()  # Return True if enough funds exist

    def __str__(self):
        """Return a string representation of the category and its ledger."""
        # Format the category name to be centered with asterisks
        output = f"{self.category_name:*^30}\n"  
        for item in self.ledger:
            # Truncate the description to a maximum of 23 characters
            description = item['description'][:23]  
            # Format the amount to 2 decimal places
            amount = f"{item['amount']:.2f}"  
            # Append formatted item description and amount to the output
            output += f"{description:<23}{amount:>7}\n"  
        # Append the total balance at the end
        output += f"Total: {self.get_balance():.2f}"  
        return output

def create_spend_chart(categories):
    """Create a chart showing the percentage of spending by category."""
    total_spent_list = []  # List to store total spent per category
    total_spent = 0  # Total spent across all categories

    # Step 1: Calculate total spent for each category
    for category in categories:
        spent = sum(-item['amount'] for item in category.ledger if item['amount'] < 0)  # Sum negative amounts (withdrawals)
        total_spent_list.append(spent)  # Append the total spent for the category
        total_spent += spent  # Accumulate total spent across all categories

    # Step 2: Calculate the percentage of total spent for each category
    percentage_list = [(int((spent / total_spent) * 100) if total_spent > 0 else 0) for spent in total_spent_list]

    # Step 3: Create the spend chart
    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):  # Iterate from 100 to 0 in steps of 10
        chart += f"{i:>3}| "  # Right-align the percentage
        for percentage in percentage_list:
            # Append 'o' if this category's percentage is greater than or equal to the current level
            chart += "o  " if percentage >= i else "   "
        chart += "\n"  # Newline after each percentage level

    # Step 4: Create the horizontal separator line
    chart += "    " + "-" + "-" * (3 * len(categories)) + "\n"  # Separator line extending two spaces

    # Step 5: Create the category names at the bottom
    max_length = max(len(category.category_name) for category in categories)  # Find the longest category name
    for i in range(max_length):
        chart += "     "  # Indentation for category names
        for category in categories:
            # Append the character from the category name, with padding if necessary
            if i < len(category.category_name):
                chart += category.category_name[i] + "  "  # Append character and space
            else:
                chart += "   "  # Padding for shorter category names
        chart += "\n"  # Newline after each row of names

    return chart[:-1] # Remove any trailing whitespace, including the last newline

# Example usage:
food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
auto = Category("Auto")
food.transfer(50, clothing)
food.transfer(100, auto)
clothing.withdraw(30.50, 't-shirt')
auto.withdraw(70.30, "engine")

print(food)
# create_spend_chart([food, clothing, auto])
print(
    (create_spend_chart([food, clothing, auto])))

