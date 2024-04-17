print("What is your weekly income?")
weekly_income = int(input())
print("How much do you pay for your weekly expenses?")
living_expenses = int(input())
print("Whats the price of a new computer?")
new_computer_cost = int(input())

net_income = weekly_income - living_expenses
print("Your net income for the average week is $" + str(net_income) + " .")

weeks_required = new_computer_cost / net_income
print("It will take " + str(weeks_required) + " weeks to save for a new computer.")