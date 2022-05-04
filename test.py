def main():
  income = 0.0
  fixed = 0.0
  additional = "y"
  expense = 0.0
  totalExpense = 0.0
  totals = 0.0
  income = getIncome()
  fixed = fixedCosts()
  additional = moreExpenses()
  while additional == "y":
      index = addExpenses()
      totalExpense += index
      additional = moreExpenses()
  totals = fixed + totalExpense
  print("Additional expenses: $", "%.2f"%index)
  spending(income, totals)

def getIncome():
  while True:
    try:
      income = float(input("Hello, Ashley. What was your income for this month?: "))
    if income < 0:
      print("Invalid entry, please try again.")
    else:
      return income
   except:
     print("Invalid entry, please try again.")

def fixedCosts():
  fixed = [700.00, 45.00, 60.00]
  print("Your rent: $", "%.2f"%fixed[0])
  print("Your phone bill: $", "%.2f"%fixed[1])
  print("Your car insurance: $", "%.2f"%fixed[2])
  fixed = sum(fixed)
  print("Your fixed monthly costs are: $", "%.2f"%fixed)
  return fixed

def moreExpenses():
  additional = ""
  additional = input("Would you like to enter another expense? (y/n): ")
  additional = additional.lower()
  while additional != "y" and additional != "n":
    print("Invalid entry, please try again.")
    additional = input("Would you like to enter another expense? (y/n): ")
    additional = additional.lower()
  return additional

def addExpenses():
  index = []
  expense = 0.0
  while True:
    try:
      expense = float(input("Enter an additional expense: "))
      index.append(expense)
     if expense < 0:
       print("Invalid entry, please try again.")
     else:
       return index
    except:
      print("Invalid entry, please try again.")

def spending(income, totals):
  finalTotal = income - totals
  if finalTotal > 0:
    print("You saved $", "%.2f"%finalTotal, "this month!")
  elif finalTotal < 0:
    print("You overspent by $", "%.2f"%finalTotal, "this month!")
  else:
    print("You broke even this month!")