#Import Pandas
import pandas as pd
#Import Configuration
from config import Configuration
#Import Errors & Warnings
from errors import Errors,Warnings
#Import YFINANCE module
import yfinance as yf
#Import URLLIB for handling HTTP Request
import urllib
#Import Datetime
from datetime import datetime
#Import Data Analysis Functions
from stock_database import data_analysis

#Clean data before analysis
def prep_stock_data(stock_data):
    try:
        #Remove unwanted columns
        stock_data = stock_data.drop(columns = ["Dividends","Stock Splits"],axis = 1)
        #Fill 0 for null values
        stock_data = stock_data.fillna(0)
    except:
        print("\n"+Warnings.TRANSFORMATION_ERROR)
    finally:
        return stock_data

#Search stock data by yfinance API if Tickr Symbol provided
def search_stock_api(stock_tickr,period):
    try:
        #Replace blank spaces in Symbol
        stock_tickr = stock_tickr.replace(" ","")
        stock_data = yf.Ticker(stock_tickr)
        start = None
        end = None
        #Set period for collecting data
        if period[0] != "" and period[1] != "":
            start = period[0]
            end = period[1]
            period_arg = ""
        else:
            period_arg = "max"
<<<<<<< Updated upstream

        stock_prices = stock_data.history(period=period_arg,start=start,end=end)
    except OverflowError as invalid_period:
        print("\n"+Errors.CAUGHT_EX.replace("&0",invalid_period))
        return ""
=======
        #Get Historical Data
        stock_prices = stock_data.history(period=period_arg,start=start,end=end)
        #Perform Data Transformation
        stock_prices = prep_stock_data(stock_prices)
>>>>>>> Stashed changes
    except KeyError:
        return ""
    except urllib.error.HTTPError:
        return ""
    else:
        return stock_prices

def search_stock_name(stock_data,stock_name):
    try:
        #Search for the stock inside the .CSV file
        stock_data = stock_data[stock_data["Name"].str.lower().str.contains(stock_name.lower())]
        if len(stock_data) == 1:
            print("\n",stock_data[["Symbol","Name","IPOyear","Summary Quote"]])
            return stock_data["Symbol"].to_string()[-4:]
        else:
            #Determine if no results/more than one result was found
            #Ask user to search with Tickr based
            if (len(stock_data) < 1):
                print("\n"+Errors.NOT_FOUND.replace("&1",stock_name)) 
            else:
                print("\n"+Warnings.MULTIPLE+"\n"+stock_data[["Symbol","Name","IPOyear","Summary Quote"]])
            return ""
    except TypeError:
        print(Errors.TYPE_MISMATCH)
        return ""
    except:
        print(Errors.UNEXPECTED_ERROR)
        return ""

<<<<<<< Updated upstream
def get_and_validate_period():
    try:
        valid_start_date = datetime.strptime(input("\nEnter Start Date for Analysis (YYYY-MM-DD): "),"%Y-%m-%d").date()
        valid_end_date = datetime.strptime(input("\nEnter End Date for Analysis (YYYY-MM-DD): "),"%Y-%m-%d").date()

        if valid_end_date > datetime.today().date():
            raise ValueError("End Date cannot be greater than Today")
        elif valid_end_date <= valid_start_date:
            raise ValueError("Starte Date cannot be greater than End Date")
        else:
            period = [valid_start_date,valid_end_date]
    except ValueError as date_value:
        print("\n"+Errors.CAUGHT_EX.replace("&0",str(date_value)))
        period = []
    finally:
        return period
=======
def validate_period(period):
    try:
        #Convert date string to datetime
        date_val = datetime.strptime(period,"%Y-%m-%d").date()
    except ValueError as date_value:
        print("\n"+Errors.CAUGHT_EX.replace("&0",str(date_value))+ \
        "\n"+Warnings.CAUGHT_EX.replace("&0","Proceeeding with Max Time Range"))
        date_val = ""
    finally:
        return date_val
>>>>>>> Stashed changes

def search_stock_data(stock_data,stock_tickr,stock_name):
    #Validate and Get Time Period
    period = get_and_validate_period()
    if not len(period):
        return "DE"

    #Search based on tickr symbol
    if stock_tickr:
        stock_r_data = search_stock_api(stock_tickr,period) 
    else:
        #Get Tickr Symbol from Selected Name
        stock_tickr = search_stock_name(stock_data,stock_name)
        stock_r_data = search_stock_api(stock_tickr,period)
     
    return stock_r_data      

def stock_main():
    try:
        #Read the contents of the file
        stock_csv_df = pd.read_csv(Configuration.DATABASE_PATH)
        
        #Search for Stock Data based on Tickr Symbol/Name
        search_choice = 0
        stock_result = ""
        search_text = Configuration.tabulate_output("SEARCHMENU")
        while search_choice != 3:
            try:
                search_choice = int(input("\n"+search_text+"\nSelect: "))      
                if search_choice == 1:
                    #Search Stock by Ticker
                    stock_tickr = input("\nEnter Stock Tickr Symbol: ")
                    stock_tickr = stock_tickr.upper()
                    stock_result = search_stock_data(stock_csv_df,stock_tickr,False)
                    
                elif search_choice == 2:
                    #Search Stock by Name
                    stock_name = input("\nEnter Stock Name: ")
                    stock_result = search_stock_data(stock_csv_df,False,stock_name)                    
                elif search_choice == 3:
                    #Exit Menu
                    break
                else:
                    #Invalid Choice
                    print("\n"+Errors.INVALID_CHOICE)
                    continue
                
                if isinstance(stock_result, pd.DataFrame):
                    print(stock_result)
                    data_analysis.analysis_main(stock_result)
                elif stock_result == "DE":
                    continue
                else:    
                    print("\n"+Warnings.DATA_NOT_FOUND)
                    continue
<<<<<<< Updated upstream
=======
                else:
                    #print(Configuration.tabulate_output("DATAFRAME",stock_result))
                    data_analysis.analysis_main(stock_result)
>>>>>>> Stashed changes

            except ValueError:
                print("\n"+Errors.ONLY_NUMBERS)
    except FileNotFoundError:
        print("\n"+Errors.FILE_NOT_FOUND.replace("&1",Configuration.DATABASE_PATH))
    #except:
        #print("\n"+Errors.UNEXPECTED_ERROR)
