#Get all errors from Errors class
from errors import Errors

#Import Stock Data from .CSV file
from stock_database import stock_data

#Select the mode of application : 1. Command Line 2. GUI
def user_menu():
    print("Hello!, Kindly choose an option to use the app.")
    try:
        op_mode = int(input("1. Graphical User Interface \n2. Command Line Interface \n"))
        print(Errors.INVALID_CHOICE) if (op_mode != 1 and op_mode != 2) else run_app(op_mode)  
    except ValueError:
        print("-"*10+"\n"+Errors.ONLY_NUMBERS)

#Run the application based on user choice
def run_app(app_mode):
    command_line() if app_mode == 2 else start_gui()

#Display all the operations for command line
def command_line():
    display_options()

def start_gui():
    print("GUI is under construction. Exiting now.")

#Options for user to select
def display_options():
    option = 0
    while (option != 4):
        try:
            print("\nWelcome! \nKindly choose an option!\n"+"-"*25)
            option = int(input("1. Search Stock \n2. Analyse Stock \n3. Terms & Conditions \n4. To Exit \n"))
            perform_operation(option)
        except ValueError:
            print("-"*25+"\n"+Errors.ONLY_NUMBERS)

def perform_operation(op):
    if op == 1:
        stock_data.stock_main()
    elif op == 2:
        print("Perform Analytics")
    elif op == 3:
        print("Get T&C")
    elif op == 4:
        print("Goodbye!\n"+"-"*25)
    else:
        print("-"*25+"\n"+Errors.INVALID_CHOICE)

     


