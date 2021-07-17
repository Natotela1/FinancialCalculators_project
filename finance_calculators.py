# A programme that allows access to two financial calculators
# An investment calculator n A home loan repayment calculator
import math

print("    WELCOME TO OUR FINANCIAL CALCULATOR APP")
print("    You can now use this app to calculate... \nANY 'INVESTMENTS' or 'BOND' repayments, YOU QUALIFY FOR.\n")
print("\n!!!!!!!!!!!!!!!!!!!!!!!!!FIND OUT NOW!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
print("Choose either 'investment' or 'bond' to proceed:")
print("Investment    - to calculate the amount of interest you'll earn on interest.\n"
      "Bond          - to calculate the amount you'll have to pay on a home loan.")


# Using if else an elif statements to determine which financial calculator to use
# Enter which you would like to calculate either investment or bond
invest_or_bond = input("\nEnter which you'd like to calculate?['investment' or 'bond']\n")
invest_or_bond = invest_or_bond.lower()
if (invest_or_bond == "bond") :
    invest_or_bond = "bond"
    print("\n                !!!Let's calculate a Bond for you!!!")

elif invest_or_bond == "investment":
    invest_or_bond = "invest"
    print("\n                !!!Let's calculate an Investment for you!!!")
else:
    print("Please rerun the programme and enter either 'investment' or 'bond'.Which you would like to calculate?")
    print("                             'Investment' or 'Bond'!!!\n")


# if investment selected ask user to enter the following using if elif else statements
# Calculate the worth of the investment compounded or simply interested
if invest_or_bond == "invest":
    print("________________________________________________________________________________")
    investment_amount = float(input("Enter the amount of money that you would like to invest.[in Rands]\n"))
    interest_rate = float(input("Enter how much interest rate in percentage you would you like to earn?"
                                "[enter rate without '%' sign]\n"))
    number_of_years = float(input("Enter the number of years you would like to invest for.\n"))
    interest = input("Enter which interest you want “simple” or “compound” interest rate\n")
    if (interest == "simple") or (interest == "Simple") or (interest == "SIMPLE"):
        r = interest_rate / 100
        p = investment_amount
        t = number_of_years
        A = p * (1 + r * t)
        print("_____________________________SIMPLE RATE INVESTMENT________________________________")
        print(f"IF\nInvestment Amount     = R{investment_amount}\nInterest Rate         = {interest_rate}%"
              f"\nNumber of Years     = {number_of_years}years")
        print(f"THEN\nYour investment will be worth R{A} after {int(t)}years using simple interest"
              f" at a rate of {interest_rate}%.")
        print("________________________________________________________________________________")
    elif (interest == "compound") or (interest == "Compound") or (interest == "COMPOUND"):
        r = interest_rate / 100
        p = investment_amount
        t = number_of_years
        A = float(math.floor(p * math.pow((1 + r), t)))
        print("_____________________________COMPOUND RATE INVESTMENT_____________________________")
        print(f"IF\nInvestment Amount     = R{investment_amount}\nInterest Rate         = {interest_rate}%"
              f"\nNumber of Years       = {number_of_years}years")
        print(f"THEN\nYour investment will be worth R{A} after {int(t)}years using compund interest"
              f" at a rate of {interest_rate}%.!!!")
        print("________________________________________________________________________________")

    else:
        print("Please rerun the programme and enter either 'simple' or 'compound'"
              "for the interest you'd like your investment to gain")


# If bond selected ask user to enter the following
# Calculate the monthly bond repayment on house
if invest_or_bond == "bond":
    print("________________________________________________________________________________")
    present_value_of_house = float(input("Enter how much the present value of the house"
                                         " you want a bond for is?.[in Rands]\n"))
    annual_rate = float(input("Enter how much the annual interest rate in percentage is for the house?"
                              "[enter rate without '%' sign]\n"))
    number_of_months = float(input("Enter the number of months you would like to repay the bond over.\n"))
    P = present_value_of_house
    i = (annual_rate / 100) / 12
    n = number_of_months
    bond_repayment = (i * P) / (1 - (1 + i)**(-n))
    bond_repayment = (format(bond_repayment, '.2f'))
    print("_________________________MONTHLY BOND REPAYMENT ________________________________")
    print(f"IF\nValue of House   = R{present_value_of_house}\nAnnual Rate      = {annual_rate}%"
          f"\nNumber of Months = {int(number_of_months)}months\nTHEN")
    print(f"You'll be paying an amount of R{bond_repayment} monthly bond repayments!!!")
    print("________________________________________________________________________________")