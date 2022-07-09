# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import pandas as pd
import numpy as np
import numpy_financial as npf
from datetime import date

class MortgageCalculator:
    """
       Defines the main class for mortgage calculation
    """
    def __init__(self, interest, years, mortgage):
        self.interest = interest
        self.years = years
        self.mortgage = mortgage
        
        self.monthly_payment = round(-1 * npf.pmt(interest/1200, years*12, mortgage), 2)
        self.total_repayment = round(self.monthly_payment * self.years * 12)

    def definition(self):
        """
        Describes the mortgage
        """
        return f"A {self.years}-year mortgage for a total amount borrowed of ${self.mortgage} at an interest rate of {self.interest}%\nhas a monthly payment amount of ${self.monthly_payment}.\nThe total amount repaid on this mortgage by the end of the term will be ${self.total_repayment}.\n"


"""
    Defines some example mortgages to display to the user
"""
MortgageA = MortgageCalculator(4.0, 20, 250000)
MortgageB = MortgageCalculator(4.0, 30, 250000)
MortgageC = MortgageCalculator(4.5, 30, 250000)

def choose_example():
    """
       Allows user to select an example mortgage and view details
    """
    while True:
        print("You have chosen to view example mortgages.")
        print("Please select from the following options:")
        print("Type 'a' to view details of a 20-year mortgage for a total amount borrowed of $250,000 with an interest rate of 4.0%")
        print("Type 'b' to view details of a 30-year mortgage for a total amount borrowed of $250,000 with an interest rate of 4.0%")
        print("Type 'c' to view details of a 30-year mortgage for a total amount borrowed of $250,000 with an interest rate of 4.5%")
        print("Type 'd' to view details of all of the above mortgages at once.")
        print("Type 'x' to return to the main menu.")
        print("Type 'z' to exit the mortgage calculator.")
        
        choice = input("Enter your selection here:\n")

        if choice == "a":
            print(MortgageA.definition())
        elif choice == "b":
            print(MortgageB.definition())
        elif choice == "c":
            print(MortgageC.definition())
        elif choice == "d":
            print(MortgageA.definition())
            print(MortgageB.definition())
            print(MortgageC.definition())
        elif choice == "x":
            welcome_user()
            break
        elif choice == "z":
            print("Thank you for using the mortgage calculator and goodbye.")
            break
        else:
            print("Invalid input, please try again.\n")

def enter_details():
    """
       Menu to allow user to input their own parameters and view mortgage costs
    """
    while True:
        print("Please enter the details for your mortgage.")
        print("Enter the interest rate first, then the number of years")
        print("the mortgage will run for, then the total amount borrowed.")
        print("Use a comma to separate the values.\n")
        print("For example, for a 4.25% interest rate on a 30-year mortgage")
        print("borrowing a total of $250,000, enter the following:\n")
        print("4.25, 30, 250000")

        try:
            user_interest, user_years, user_amount = input("Enter the values here:\n").split(",")
            num_interest = float(user_interest)
            num_years = float(user_years)
            num_amount = float(user_amount)
            if (num_years > 0 and num_amount > 0):
                print(f"values are {num_interest}, {num_years}, {num_amount}\n")
            else:
                print("The number of years and the amount borrowed must be a positive amount, please try again.\n")
        except ValueError:
            print("The values you have entered are not in the correct format, please try again.\n")
        else:
            break

def own_details():
    """
       Menu to allow user to input their own parameters and view mortgage costs
    """
    while True:
        print("You have chosen to input details and view the resulting mortgage costs.")
        print("Please select from the following options:")
        print("Type 'a' to continue to input your details.")
        print("Type 'x' to return to the main menu.")
        print("Type 'z' to exit the mortgage calculator.")
        
        choice = input("Enter your selection here:\n")

        if choice == "a":
            enter_details()
            break
        elif choice == "x":
            welcome_user()
            break
        elif choice == "z":
            print("Thank you for using the mortgage calculator and goodbye.")
            break
        else:
            print("Invalid input, please try again.\n")


def welcome_user():
    """
       Introductory screen for the user
    """
    while True:
        print("Welcome to the mortgage calculator!")
        print("Please select from the following options:")
        print("Type 'a' to view examples of different mortgages.")
        print("Type 'b' to input your own details.")
        print("Type 'z' to exit the mortgage calculator.")

        choice = input("Enter your selection here:\n")

        if choice == "a":
            choose_example()
            break
        elif choice == "b":
            own_details()
            break
        elif choice == "z":
            print("Thank you for using the mortgage calculator and goodbye.")
            break
        else:
            print("Invalid input, please try again.\n")

welcome_user()


