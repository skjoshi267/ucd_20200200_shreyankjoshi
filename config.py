from colorama import init
import tabulate as tb

class Configuration:
    DATABASE_PATH = "stock_database/jl_stock.csv"

    #Set the backend file path
    def set_file_path(file_path):
        Configuration.DATABASE_PATH = file_path

    #Initialize color scheme
    def initialize_color_scheme():
        init()

    #Format the Menu Output based on Menu Type
    def tabulate_output(menu,data=None):
        #Operation Menu GUI v/s CLI
        align="left"
        if menu.upper() == "OPMENU":
            header = ["Kindly choose an option to use the app"]
            table_text = [["1. Graphical User Interface"],["2. Command Line Interface"]]
        #Display Menu for Stock Actions
        elif menu.upper() == "DISPOPTMENU":
            header = ["Kindly Select an Action"]
            table_text = [["1. Search & Analyse Stock"], \
                        ["2. Generate Report"],["3. Terms & Conditions"],["4. Exit"]]
        elif menu.upper() == "MAINMENU":
            header = ["Welcome to Justice League!"]
            table_text = [["Stock Analysis App"]]
            align = "center"
        elif menu.upper() == "SEARCHMENU":
            header = ["Kindly Select a Search Option"]
            table_text = [["1. Search by Tickr"],["2. Search by Name"],["3. Exit"]]
        elif menu.upper() == "DATAFRAME":
            header = "keys"
            table_text = data
        elif menu.upper() == "ANMENU":
            header = ["Welcome to JL Stock Analytics"]
            table_text = [["1. Descriptive Analytics"],["2. Predictive Analyitcs"],["3. Exit"]]
        elif menu.upper() == "DESCSMENU":
            header = ["Kindly Select type of Descriptive Statistics"]
            table_text = [["1. Summary"],["2. Raw Time Series"],["3. Linear Trends"],["4. Movinge Average(n)"],["5. Weighted Moving Average"],["6. MACD"]]
        return tb.tabulate(table_text,header,"psql",stralign=align)