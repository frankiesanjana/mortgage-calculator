"""
Import external libraries for the program
Connect APIs and allow access via credentials file
"""
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
import numpy_financial as npf
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('mortgage_database')
stored_data = SHEET.worksheet('database')


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
        return f"{Fore.LIGHTCYAN_EX}{Style.BRIGHT}A {self.years}-year mortgage for a total amount borrowed of ${self.mortgage} at an interest rate of {self.interest}%\nhas a monthly payment amount of ${self.monthly_payment}.\n\nThe total amount repaid on this mortgage by the end of the term will be ${self.total_repayment}.\n"


# Defines some example mortgages to display to the user
MortgageA = MortgageCalculator(4.0, 20, 250000)
MortgageB = MortgageCalculator(4.0, 30, 250000)
MortgageC = MortgageCalculator(4.5, 30, 250000)


def choose_example():
    """
       Allows user to select an example mortgage and view details
    """
    print(f"\n{Fore.LIGHTGREEN_EX}{Style.BRIGHT}Hi, {username}!\n")
    while True:
        print(f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}You have chosen to view example mortgages.\n")
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
            print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}\nThank you for using the mortgage calculator and goodbye, {username}.")
            break
        else:
            print(Fore.LIGHTYELLOW_EX + "\nInvalid input, please try again.\n")


def save_details():
    """
       Menu to allow user to save the details they have entered,
       submit alternative details or choose another option
    """
    while True:
        print(Fore.LIGHTRED_EX + Style.BRIGHT + "Would you like to save these details?\n")
        print("Type 's' to save these details for future use.")
        print("Type 'a' to input some alternative details.")
        print("Type 'x' to return to the main menu.")
        print("Type 'z' to exit the mortgage calculator.")

        save = input("Enter your selection here:\n")

        if save == "s":
            list_details = [username, UserMortgage.interest, UserMortgage.years, UserMortgage.mortgage, UserMortgage.monthly_payment, UserMortgage.total_repayment]
            print("Saving your details...\n")
            database = SHEET.worksheet('database')
            database.append_row(list_details)
            print("Great! Your details have been saved to the database.\n")
            print("\nTaking you to the main menu...")
            welcome_user()
            break
        elif save == "a":
            enter_details()
            break
        elif save == "x":
            welcome_user()
            break
        elif save == "z":
            print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}\nThank you for using the mortgage calculator and goodbye, {username}.")
            break
        else:
            print(Fore.LIGHTYELLOW_EX + "Invalid input, please try again.\n")


def enter_details():
    """
       Section where the user enters their details
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
                print(f"\nThe details you have entered are an interest rate of {num_interest}%\n for {num_years} years, for an amount of ${num_amount}\n")
                global UserMortgage
                UserMortgage = MortgageCalculator(num_interest, num_years, num_amount)
                print(UserMortgage.definition())
                save_details()
                break
            else:
                print(Fore.LIGHTYELLOW_EX + "The number of years and the amount borrowed must be a positive amount, please try again.\n")
        except ValueError:
            print(Fore.LIGHTYELLOW_EX + "The values you have entered are not in the correct format, please try again.\n")
        else:
            break


def own_details():
    """
       Menu to allow user to input their own parameters and view mortgage costs
    """
    print(f"\n{Fore.LIGHTGREEN_EX}{Style.BRIGHT}Hi, {username}!\n")
    while True:
        print(f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}You have chosen to input details and view the resulting mortgage costs.\n")
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
            print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}\nThank you for using the mortgage calculator and goodbye, {username}.")
            break
        else:
            print(Fore.LIGHTYELLOW_EX + "Invalid input, please try again.\n")


def welcome_user():
    """
       Main menu of the mortgage calculator
    """
    while True:
        print(f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}\nWelcome to the main menu, {username}!\n")
        print("Please select from the following options:\n")
        print("Type 'a' to view examples of different mortgages.")
        print("Type 'b' to input your own details and view results.")
        print("Type 'c' to view your saved details and results.")
        print("Type 'z' to exit the mortgage calculator.\n")

        choice = input("Enter your selection here:\n")

        if choice == "a":
            choose_example()
            break
        elif choice == "b":
            own_details()
            break
        elif choice == "c":
            retrieve_saved_details()
            break
        elif choice == "z":
            print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}\nThank you for using the mortgage calculator and goodbye, {username}.")
            break
        else:
            print(Fore.LIGHTYELLOW_EX + "Invalid input, please try again.\n")


def retrieve_saved_details():
    """
       Allows user to view details they have stored in the database
    """
    if stored_data.find(username, in_column=1):
        print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "\nThe details you currently have saved are:\n")
        df = pd.DataFrame(stored_data.get_all_records())
        user_record = df.loc[df['username'] == username].to_string(index=False)
        print(user_record)
        while True:
            print("\nWhat would you like to do next?")
            print("Type 'a' to input further details.")
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
                print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}\nThank you for using the mortgage calculator and goodbye, {username}.")
                break
            else:
                print(Fore.LIGHTYELLOW_EX + "Invalid input, please try again.\n")
    else:
        print(Fore.LIGHTYELLOW_EX + "\nYou do not currently have any details stored.")
        print(Fore.LIGHTYELLOW_EX + "Returning to the main menu...")
        welcome_user()


def returning_user():
    """
       Welcome screen for returning users
    """
    print("Welcome back! Please enter your username.")
    print("Alternatively, type 'n' to create a new username")
    while True:
        global username
        username = input("Enter your username here:\n")

        if username == 'n':
            new_username()
            break
        elif stored_data.find(username, in_column=1):
            print("\nTaking you to the main menu...")
            welcome_user()
            break
        else:
            print(Fore.LIGHTYELLOW_EX + "\nUsername not found, please try again.")


def new_username():
    """
       Welcome screen for new users
       where they can set a username
    """
    while True:
        print("To get started, please enter your username.")
        print("Usernames must be between 2 and 15 characters,")
        print("and should contain only letters from a to z.\n")

        global username
        username = input("Enter your username here:\n")

        if stored_data.find(username, in_column=1):
            print(Fore.LIGHTYELLOW_EX + "\nSorry, that username has already been taken.")
            print(Fore.LIGHTYELLOW_EX + "Please choose an alternative username.\n")
        elif username.isalpha() and len(username) > 1 and len(username) < 16:
            welcome_user()
            break
        else:
            print(Fore.LIGHTYELLOW_EX + "\nThe username you have entered is not valid, please try again.\n")


def intro_page():
    """
       Introductory screen for the user
    """
    print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "Welcome to the mortgage calculator!\n")
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + """\
                           ====
                           !!!!
      ==========================
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  ||      _____          _____    ||
  ||      | | |          | | |    ||
  ||      |-|-|          |-|-|    ||
  ||      #####          #####    ||
  ||                              ||
  ||      _____   ____   _____    ||
  ||      | | |   @@@@   | | |    ||
  ||      |-|-|   @@@@   |-|-|    ||
  ||      #####   @@*@   #####    ||
  ||              @@@@            ||
******************____****************
**************************************\n""")
    print("This program allows you to enter your financial details")
    print("and see the costs associated with your mortgage.\n")
    while True:
        print("To get started, please enter 1 if you have saved details in the mortgage calculator.")
        print("Enter 2 if you have not previously saved your information in the mortgage calculator.\n")

        type = input("Please enter your choice here:\n")

        if type == "1":
            returning_user()
            break
        elif type == "2":
            new_username()
            break
        else:
            print(Fore.LIGHTYELLOW_EX + "Invalid input, please try again.\n")


intro_page()
