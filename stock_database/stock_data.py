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

#Global Variable
stock_symbol = ""

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
        #Get Historical Data
        stock_prices = stock_data.history(period=period[0],start=period[1],end=period[2])
        #Perform Data Transformation
        if len(stock_prices) > 0:
            stock_prices = prep_stock_data(stock_prices)
    except Exception as unknown:
        print("\n"+Errors.CAUGHT_EX.replace("&0",str(unknown)))
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

def set_date(period_range,from_date=True):
    try:
        #Get Start Date
        input_date = input("\nEnter Start Date (YYYY-MM-DD): ")
        input_date = datetime.strptime(input_date,"%Y-%m-%d").date()

    except ValueError as date_value:
        print("\n"+Errors.CAUGHT_EX.replace("&0",str(date_value)))
        period = set_period(True)
        period_range = [period,None,None]
    else:
        if from_date:
            period_range[0] = ""
            period_range[1] = input_date
        else:
            period_range[0] = ""
            period_range[2] = input_date
    finally:
        return period_range

def set_period(error = False):
    acceptable_period_range = ["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"]
    if error:
        print("\n"+Warnings.CAUGHT_EX.replace("&0","Selecting Invalid Period will get data for Max"))
    period_range_txt = Configuration.tabulate_output("PERIODR") 
    period_range = input(period_range_txt+"\nSelect: ")
    period_range = period_range.lower()
    if period_range not in acceptable_period_range:
        print("\n"+Warnings.CAUGHT_EX.replace("&0","Invalid input. Period set to Max"))
        return "max"
    else:
        return period_range

def search_stock_data(stock_data,stock_tickr,stock_name):
    #Set Start Date
    period = set_date(["","",""])

    if period[1]:
        #Set End Date
        period = set_date(period,False)

    #Search based on tickr symbol
    if stock_tickr:
        stock_r_data = search_stock_api(stock_tickr,period) 
    else:
        #Get Tickr Symbol from Selected Name
        stock_symbol = search_stock_name(stock_data,stock_name)
        stock_r_data = search_stock_api(stock_symbol,period)
     
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
                if search_choice not in range(1,4):
                    #Invalid Choice
                    print("\n"+Errors.INVALID_CHOICE)
                    continue
                elif search_choice == 1:
                    #Search Stock by Ticker
                    stock_tickr = input("\nEnter Stock Tickr Symbol: ")
                    stock_tickr = stock_tickr.upper()
                    stock_symbol = stock_tickr
                    stock_result = search_stock_data(stock_csv_df,stock_tickr,False)
                elif search_choice == 2:
                    #Search Stock by Name
                    stock_name = input("\nEnter Stock Name: ")
                    stock_result = search_stock_data(stock_csv_df,False,stock_name)                 
                else:
                    #Exit Menu
                    break
                
                if isinstance(stock_result,pd.DataFrame) and len(stock_result)>0:
                    data_analysis.analysis_main(stock_result,stock_symbol)
                else:    
                    print("\n"+Warnings.DATA_NOT_FOUND)
                    continue
            except ValueError:
                print("\n"+Errors.ONLY_NUMBERS)
            except Exception as unknown:
                print("\n"+Errors.CAUGHT_EX.replace("&0",str(unknown)))
            finally:
                return None
    except FileNotFoundError:
        print("\n"+Errors.FILE_NOT_FOUND.replace("&1",Configuration.DATABASE_PATH))
    except Exception as unknown:
        print("\n"+Errors.CAUGHT_EX.replace("&0",str(unknown))) 
   
    
