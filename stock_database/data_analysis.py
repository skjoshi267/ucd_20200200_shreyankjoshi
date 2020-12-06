from config import Configuration
from errors import Errors,Warnings
from stock_database.statistics_class import Statistics

def analysis_main(stock_prices,symbol):
    analytics_menu_txt = Configuration.tabulate_output("ANMENU")
    stats_analysis = Statistics(symbol,stock_prices)
    analysis_type = 0
    while analysis_type != 3:
        try:
            analysis_type = int(input("\n"+analytics_menu_txt+"\nSelect: "))
            print(analysis_type)
            if analysis_type not in range(1,4):
                print("\n"+Errors.INVALID_CHOICE)
                continue
            elif analysis_type == 1:
                stats_analysis.desc_stats()
            elif analysis_type == 3:
                break
            else:
                stats_analysis.pred_stats()
        except ValueError:
            print("\n"+Errors.ONLY_NUMBERS)
        except Exception as unknown:
            print("\n"+Errors.CAUGHT_EX.replace("&0",str(unknown)))
        finally:
            pass


    
    

    
