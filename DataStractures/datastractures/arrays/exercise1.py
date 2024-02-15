from util import timeit
expense = [2200, 2350, 2600, 2130, 2190]

january = expense[0]
february = expense[1]
march = expense[2]
april = expense[3]
may = expense[4]

print("Enter the month, all in lowercase!")
month1 = input("Enter the first month: ")
month2 = input("Enter the second month: ")

@timeit
def expense_difference(month1_val, month2_val):
    diff = month2_val - month1_val
    print("Expense difference between", month1, "and", month2, "is:", diff)


if month1 == "january":
    month1_val = january
elif month1 == "february":
    month1_val = february
elif month1 == "march":
    month1_val = march
elif month1 == "april":
    month1_val = april
elif month1 == "may":
    month1_val = may

if month2 == "january":
    month2_val = january
elif month2 == "february":
    month2_val = february
elif month2 == "march":
    month2_val = march
elif month2 == "april":
    month2_val = april
elif month2 == "may":
    month2_val = may

expense_difference(month1_val, month2_val)
