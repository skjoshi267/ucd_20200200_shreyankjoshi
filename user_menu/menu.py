from errors import Errors
def user_menu():
    print("Hello!, Kindly choose an option to use the app.")
    try:
        op_mode = int(input("1. Graphical User Interface \n2. Command Line Interface \n"))
        print("Only 1 and 2 are valid choices. Please Try Again") if (op_mode != 1 and op_mode != 2) else run_app(op_mode)  
    except ValueError:
        print("-"*10+"\n"+Errors.ONLY_NUMBERS)

def run_app(app_mode):
    display_options() if app_mode == 1 else True

def display_options():
    option = 0
    while (option != 99):
        print("Welcome!")
        try:
            print("Kindly choose the operation to perform")
            option = int(input("1. Get Data \n2. Perform Analysis \n3. Add Data \n99. To Exit \n"))
        except ValueError:
            print("-"*10+"\n"+Errors.ONLY_NUMBERS)
        

     


