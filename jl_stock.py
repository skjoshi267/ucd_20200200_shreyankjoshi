#Import user menu
from user_menu import menu
#Import Configuration
from config import Configuration
#Import Errors
from errors import Errors,Warnings

#Start the application
if __name__ == "__main__":
    try:
        #View the Main Display
        Configuration.initialize_color_scheme()
        main_menu_txt = Configuration.tabulate_output("MAINMENU")
        print(main_menu_txt+"\n")
        #Initiate User Options
        menu.user_menu()
    #Catch Module Errors
    except ModuleNotFoundError as module:
        print("\n"+Errors.CAUGHT_EX.replace("&0",str(module)))
    #Catch Unexpected Errors
    except Exception as unknown:
        print("\n"+Errors.CAUGHT_EX.replace("&0",str(unknown)))
    finally:
        print("\nGood-Bye. Thank you for using JL_Stock App!")

#References
#https://pypi.org/project/colorama/
#https://pypi.org/project/tabulate/
#https://www.earthdatascience.org/courses/use-data-open-source-python/use-time-series-data-in-python/date-time-types-in-pandas-python/customize-dates-matplotlib-plots-python/
#https://towardsdatascience.com/making-a-trade-call-using-simple-moving-average-sma-crossover-strategy-python-implementation-29963326da7a
#https://towardsdatascience.com/trading-toolbox-02-wma-ema-62c22205e2a9


