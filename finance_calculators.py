
import math

print("Welcome to the Financial Calculator, where we help you calculate your monthly repayment amount!")

#Asking the user which type of financial calculator they need
while True:
    print("\nWhat would you like to calculate?")
    print("investment - to calculate the amount of interest you'll earn on your investment")
    print("bond - to calculate the amount you'll have to pay on a home loan")

    choice = input("\nEnter either 'investment' or 'bond' from the menu above to proceed: ").lower()
    
#Calculating how much the user will have in their investment
    if choice == "investment":
        amount = float(input("\nEnter the amount of money that you are depositing: "))
        rate = float(input("\nEnter the interest rate: " )) / 100 
        years = int(input("\nEnter the number of years you plan on investing: "))
        interest = input("\nDo you want 'simple' or 'compound' interest? ").lower()

        if interest == "simple":
            total = amount * (1 + rate * years)
        elif interest == "compound":
            total == amount * math.pow((1 + rate), years)

        print(f"\nAfter {years} years at {rate*100:.2f}%, you will have R{total:.2f}.")

#Calculating the user's monthly bond repayment amount 
    elif choice == "bond":
        house_value = float(input("\nEnter the present value of the house: "))
        rate = float(input("\nEnter the interest rate: "))
        months = int(input("\nEnter the number of months you plan to take to repay the bond: "))

        repayment = (rate * house_value) / (1 - math.pow((1 + rate), -months))

        print(f"\nYou will have to repay R{repayment:.2f} per month over {months} months.")

    else: 
        print("\nInvalid choice. Please try again.") 