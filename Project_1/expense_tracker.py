# This script is an Expense Tracker that allows users to add, list, calculate total, and filter expenses by category.

# Function to add an expense to the list
def add_expense(expenses, amount, category):
    # Appends a new expense as a dictionary containing the amount and category
    expenses.append({'amount': amount, 'category': category})

# Function to print all the expenses
def print_expenses(expenses):
    # Loops through each expense in the list and prints the amount and category
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

# Function to calculate the total expenses
def total_expenses(expenses):
    # `map` applies a function to each element in `expenses` and `lambda` is an anonymous function used here
    # The lambda function extracts the 'amount' field from each expense
    # `sum` adds all the amounts together to return the total expense amount
    return sum(map(lambda expense: expense['amount'], expenses))

# Function to filter expenses by category
def filter_expenses_by_category(expenses, category):
    # `filter` applies the lambda function to each expense and keeps only the ones that match the category
    # The lambda function returns True for expenses that match the given category
    return filter(lambda expense: expense['category'] == category, expenses)

# Main program that controls the expense tracker interface
def main():
    expenses = []  # Initialize an empty list to store expenses

    # Infinite loop to keep the program running until the user chooses to exit
    while True:
        # Display the menu options
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
       
        # Get the user's choice of operation
        choice = input('Enter your choice: ')

        # Option 1: Add an expense
        if choice == '1':
            # Ask for amount and category of the expense
            amount = float(input('Enter amount: '))  # Convert the input to a float number
            category = input('Enter category: ')  # Get the category of the expense
            
            # Add the expense to the list by calling add_expense function
            add_expense(expenses, amount, category)

        # Option 2: List all expenses
        elif choice == '2':
            print('\nAll Expenses:')
            # Print the entire list of expenses using the print_expenses function
            print_expenses(expenses)
    
        # Option 3: Show total expenses
        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))  # Calls total_expenses to get and print the sum of all expenses
    
        # Option 4: Filter expenses by category
        elif choice == '4':
            # Ask for the category to filter expenses by
            category = input('Enter category to filter: ')
            
            print(f'\nExpenses for {category}:')
            # Use filter_expenses_by_category to get only expenses matching the given category
            expenses_from_category = filter_expenses_by_category(expenses, category)
            
            # Print the filtered expenses
            print_expenses(expenses_from_category)
    
        # Option 5: Exit the program
        elif choice == '5':
            print('Exiting the program.')  # Exit message
            break  # Break the loop to end the program

main()  # Start the program

"""
Breakdown of key concepts:

lambda: This is a way to create small, anonymous functions inline. For example, lambda expense: expense['amount'] means "for a given expense, return its 'amount'."
map:

map: takes a function (like a lambda) and applies it to every element in a list. In this case, it applies the lambda function to extract the 'amount' from each expense.
Example: If expenses contains [{'amount': 50}, {'amount': 30}], map(lambda expense: expense['amount'], expenses) would return [50, 30].
filter:

filter: is used to select only those elements from a list that satisfy a certain condition. In this script, it selects expenses where the 'category' matches the user's input.
Example: If expenses contains [{'category': 'food'}, {'category': 'travel'}], filter(lambda expense: expense['category'] == 'food', expenses) would return just the expenses with the category 'food'.
sum:

sum: is a built-in function that adds up all the values in a list. Here, it adds the amounts of the expenses to calculate the total cost.
Program Flow:

The user can add expenses (option 1), list all expenses (option 2), see the total of all expenses (option 3), filter expenses by category (option 4), or exit the program (option 5).
Each function is clearly separated based on its task, and it uses Python's functional programming tools like map and filter to make the code more concise and readable.
"""