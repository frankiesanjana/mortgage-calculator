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

        

MortgageA = MortgageCalculator(4.0, 20, 250000)
print(MortgageA.definition())

MortgageB = MortgageCalculator(4.0, 30, 250000)
print(MortgageB.definition())

MortgageC = MortgageCalculator(4.5, 30, 250000)
print(MortgageC.definition())
