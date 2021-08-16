

#User needs to create and stick to a monthly budget. Based on their
#input, the program will show the user if they have overspend.

budget = float(input("Enter the amount budgeted for the month: "))
expense = float(input(" Enter an expense (or enter 0 to quit): "))
totalExpense = expense

while expense != 0:
    expense = float(input("Enter an expense (or enter 0 to quit): "))
    totalExpense += expense
print("Budgeted: ${:,.2f}".format(budget))
print("Spent: ${:,.2f}".format(totalExpense))

if totalExpense > budget:
    totalOver = totalExpense - budget
    print("You are ${:,.2f} over budget. PLAN BETTER NEXT TIME!".format(totalOver))
elif totalExpense < budget:
    total = budget - totalExpense 
    print("You are ${:,.2f} under budget. WELL DONE!".format(total))
elif totalExpense == budget:
    print("Spending matches your budget. GOOD PLANNING!")
