def main():
    user = get_name()
    expense_list = collect_expenses_v1()
    while True:
        show_or_quit = input("Type \"show\" if you would you like to view your current expense record, or \"quit\" if you would like to quit: ").strip().lower()
        if show_or_quit == "show": 
            print_all_expenses(user, expense_list)
            break
        elif show_or_quit == "quit":
            print("Thank you for using our Expense Tracker.")
            break
        else: 
            print("Please type either \"show\" or \"quit\".")
        

def get_name(): 
    name = input("Welcome, what's your name? ").strip().title()
    return name
 
def get_expense():
    expense_name = input("Name your expense: ").strip().title()
    return expense_name


def get_amount():
    while True:
        try: 
            expense_amount = float(input("State the amount of your expense: "))
        except ValueError:
            print("The amount has to be a number. ")
        else:
            if expense_amount <= 0:
                print("Please, enter a number greater than 0.  \n")
            else: 
                return expense_amount  

def get_category():
    while True: 
        expense_category = input("What would you categorize your expense as? ").strip().title()
        if is_valid_category(expense_category):
            return expense_category
        else: 
            print("Invalid category. Please choose either Food, Rent, Transport or Entertainment.") 

def is_valid_category(expense_category): 
    if expense_category == "Food":
        return True
    elif expense_category == "Transport":
        return True
    elif expense_category == "Rent":
        return True 
    elif expense_category == "Entertainment":
        return True
    else:
        return False

def classify_expense(expense_amount, expense_category):
    if expense_amount >= 100: 
        if expense_category == "Rent":
            return "Fixed expense"
        else:
            return "High expense"
    elif expense_category == "Food" or expense_category == "Transport":
        return "Necessary expense"
    else: 
        return "Regular expense"       


def create_expense():
    expense_dict = {
    }    
    expense = get_expense()
    amount = get_amount()
    category = get_category()
    category_class = classify_expense(amount, category)
    expense_dict["expense_name"] = expense
    expense_dict["amount"] = amount
    expense_dict["category"] = category
    expense_dict["classification"] = category_class
    return expense_dict
    
def collect_expenses_v1():
    expense_list = []
    while True:
        choice = input("If you would like to create a new expense record type \"yes\", type \"no\" to end. ").strip().lower()
        if choice == "yes":
            expense_list.append(create_expense())
        elif choice == "no":
            return expense_list 
        else:
            print("Please type either \"yes\" or \"no\". ")

def calculate_total(expense_list):
    total = 0
    for expense in expense_list:
        total += expense["amount"]
    return total 

def print_all_expenses(user_name, expense_list):
    print(f"{user_name}, here are your Expense Records: ")
    n = 0
    for expense in expense_list:
        n += 1
        print(f"{n}. {expense['expense_name']}")
        print(f"   Amount: ${expense['amount']:.2f}") 
        print(f"   Category: {expense['category']}")
        print(f"   Classification: {expense['classification']}")
        print()
    print(f"Total spent: ${calculate_total(expense_list):.2f}")
    print()
    print_category_summary(expense_list)

def calculate_category_totals(expense_list):
    category_amounts = {}
    for expense in expense_list:
        report_category = expense["category"]
        report_amount = expense["amount"]
        if report_category not in category_amounts: 
            category_amounts[report_category] = 0 
        category_amounts[report_category] += report_amount
    return category_amounts

def print_category_summary(expense_list):
    category_totals = calculate_category_totals(expense_list)
    print("Total spent by category: ")
    for category, total in category_totals.items():
        print(f"{category}: ${total:.2f}")
        

main()
