print("Welcome to the tip calculator")
bill = int(input("What was the total bill?\n"))
tip = int(input("Enter percentage of tip?\n"))
total_bill = bill + tip
members = int(input("The total number of members?\n"))
to_pay = total_bill / members
pay = round(to_pay, 2)
print("Each individual should pay ", str(pay))