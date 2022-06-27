# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import pandas as pd
import numpy as np
from datetime import date

class MortgageCalculator:
    """
       Defines the main class for mortgage calculation
    """
    def __init__(self, interest, years, mortgage):
        self.interest = interest
        self.years = years
        self.mortgage = mortgage

    def definition(self):
        """
        Describes the mortgage
        """
        return f"A {self.years}-year mortgage for a total amount borrowed of ${self.mortgage} at an interest rate of {self.interest}%"

MortgageA = MortgageCalculator(4.0, 20, 250000)
print(MortgageA.definition())

MortgageB = MortgageCalculator(4.0, 30, 250000)
print(MortgageB.definition())

MortgageC = MortgageCalculator(4.5, 30, 250000)
print(MortgageC.definition())
