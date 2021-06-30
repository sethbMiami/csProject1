# this is the main program for Codecadmy CS Project - Mortgage calculator.

# this is the principal amount of the house
# this is the down payment amount towards the principal amount
r = 4.5   # annual interest rate 4.5%
n = 360   # number of monthly payments for a 30 year mortgage
apt = 2500
api = 1500

def calculate_mortgage_m(p, dp):    # function calculates monthly mortgage payment
    np = p - dp
    i = (r/100)/12
    m = np * (i*(1+i)**n)/((1+i)**n - 1)
    monthly_payment = m + (apt / 12) + (api / 12)
    return round(monthly_payment, 2)

def yes_or_no(question):
    while "the answer is invalid":
        reply = input(question)
        if reply[0] == 'y':
            return True
        if reply[0] == 'n':
            print("Thank you for visiting. Goodbye.")
            quit()

print("Welcome to the CS project Mortgage Calculator!")
print("This program will calculate your monthly mortgage payment based off of the house principal amount and your initial downpayment")
print("*note - This monthly payment is based off of a 30 year fixed mortgage and includes the annual interest rate of 4.5%, with an annual property tax of $2500 and annual property insurance of $1550")

reply_true = yes_or_no("Do you wish to proceed?")

if reply_true:
    print("Lets get started!")
    
num = int(input("What is the price of the home?   Enter amount: "))
num2 = int(input("How much will your downpayment be?   Enter amount: "))

print("Thank you!")
print()
monthly_payment_true = calculate_mortgage_m(num, num2)

print("Your payment will be {} per month".format(monthly_payment_true))
