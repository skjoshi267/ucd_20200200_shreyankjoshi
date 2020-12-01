#Get all errors from Errors class
from errors import Errors

#Import Stock Data from .CSV file
from stock_database import stock_data

#Import Tabulate
import tabulate as tb

#Format the Menu Output based on Menu Type
def tabulate_output(menu):
    #Operation Menu GUI v/s CLI
    if menu.upper() == "OPMENU":
        header = ["Kindly choose an option to use the app"]
        table_text = [["1. Graphical User Interface"],["2. Command Line Interface"]]
    elif menu.upper() == "DISPOPTMENU":
        header = ["Welcome to Stock Operations!"]
        table_text = [["Kindly select the operation"],["1. Search & Analyse Stock"], \
                      ["2. Generate Report"],["3. Terms & Conditions"],["4. Exit"]]
    return tb.tabulate(table_text,header,"psql")

#Select the mode of application : 1. Command Line 2. GUI
def user_menu():
    operation_menu_txt = tabulate_output("OPMENU")
    try:
        op_mode = int(input(operation_menu_txt+"\nSelect: "))
        print("\n"+Errors.INVALID_CHOICE) if (op_mode != 1 and op_mode != 2) else run_app(op_mode)  
    except ValueError:
        print("\n"+Errors.ONLY_NUMBERS)

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
    disp_menu_txt = tabulate_output("DISPOPTMENU")
    while (option != 4):
        try:
            option = int(input(disp_menu_txt+"\nSelect: "))
            perform_operation(option)
        except ValueError:
            print("\n"+Errors.ONLY_NUMBERS)

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
        print("\n"+Errors.INVALID_CHOICE)

     


