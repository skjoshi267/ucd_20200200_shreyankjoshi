#Get all errors from Errors class
from errors import Errors
#Get all configurations from Configuration Class
from config import Configuration
#Import Stock Data and Operations
from stock_database import stock_data

#Select the mode of application : 1. Command Line 2. GUI
def user_menu():
    operation_menu_txt = Configuration.tabulate_output("OPMENU")
    try:
        op_mode = int(input(operation_menu_txt+"\nSelect: "))
        print("\n"+Errors.INVALID_CHOICE) if (op_mode != 1 and op_mode != 2) else run_app(op_mode)  
    except ValueError:
        print("\n"+Errors.ONLY_NUMBERS)

#Run the application based on user choice
def run_app(app_mode):
    command_line() if app_mode == 2 else start_gui()

def command_line():
    display_options()

def start_gui():
    print("GUI is under construction. Exiting now.")

#Display all the operations for command line
def display_options():
    option = 0
    disp_menu_txt = Configuration.tabulate_output("DISPOPTMENU")
    while (option != 4):
        try:
            option = int(input("\n"+disp_menu_txt+"\nSelect: "))
            perform_operation(option)
        except ValueError:
            print("\n"+Errors.ONLY_NUMBERS)

#Perform CLI Operations
def perform_operation(op):
    if op not in range(1,5):
        print("\n"+Errors.INVALID_CHOICE)    
    elif op == 1:
        stock_data.stock_main()
    elif op == 2:
        print("Generate Report")
    elif op == 3:
        print("Get T&C")
    else:
        pass
     


