# this is the main program for Codecadmy CS Project - Mortgage calculator.

p = 0 # this is the principal amount of the house
dp = 0 # this is the down payment amount towards the principal amount
r = 4.5 # annual interest rate 4.5%
n = 360 # number of monthly payments for a 30 year mortgage
apt = 2500
api = 1500

def calculate_mortgage_m(principal, downpayment):    # function calculates monthly mortgage payment
    np = p - dp
    i = (r/100)/12 
    # M = P [ i(1 + i)^n ] / [ (1 + i)^n – 1] mortgage payment formula
    m = np * (i(1+i)**n)/((1+i)**n - 1)
    monthly_payment = m + (apt / 12) + (api / 12)
    return monthly_payment

def yes_or_no(question):
    while "the answer is invalid":
        reply = str(input(question+' (y/n): ')).lower().strip()
        if reply[0] == 'y':
            return True
        if reply[0] == 'n':
            print("Thank you for visiting. Goodbye.")
            quit()

print("Welcome to the CS project Mortgage Calculator!")
print("This program will calculate your monthly mortgage payment based off of the house principal amount and your initial downpayment")
print("*note - This monthly payment is based off of a 30 year fixed mortgage and includes the annual interest rate of 4.5%, with an annual property tax of $2500 and annual property insurance of $1550")

reply = yes_or_no("Do you wish to proceed?")

if reply == True:
    print("Lets get started!")
    
# p = input("What is the price of the home?   Enter amount: ")
try:
  num = int(input("What is the price of the home?   Enter amount: "))
  print("num:", num)
except ValueError:
    print("Please input a number")  




try:
  num2 = int(input("How much will your downpayment be?   Enter amount: "))
  print("num:", num2)
except ValueError:
    print("Please input a number")



print("Thank you!")
print()

monthly_payment = calculate_mortgage_m(num, num2)

print("Your payment will be {} per month".format(monthly_payment))
