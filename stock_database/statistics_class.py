from config import Configuration
from errors import Errors,Warnings

class Statistics:
    __stock_data = ""

    def __init__(self,stock_prices):
        self.__stock_data = stock_prices
    
    def get_stock_data(self):
        return self.__stock_data

    def desc_stats(self):
        desc_stats_menu_txt = Configuration.tabulate_output("DESCSMENU")
        try:
            stats_choice = int(input("\n"+desc_stats_menu_txt+"\nSelect: "))
            if stats_choice not in range(1,8):
                print("\n"+Errors.INVALID_CHOICE)
            elif stats_choice == 1:
                print("\n")
                print(Configuration.tabulate_output("DATAFRAME",self.__stock_data.describe()))
            else:
                pass
        except ValueError:
            print("\n"+Errors.ONLY_NUMBERS)
        finally:
            return None

    def pred_stats(self):
        pass

     