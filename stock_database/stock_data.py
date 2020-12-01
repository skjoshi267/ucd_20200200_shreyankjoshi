import pandas as pd
from config import Configuration
from errors import Errors,Warnings
import yfinance as yf
import urllib
from datetime import datetime
from stock_database import data_analysis

def prep_stock_data(stock_data):
    try:
        #Remove unwanted columns
        stock_data = stock_data.drop(columns = ["Unnamed: 8"],axis = 1)
        #Specify Missing Values for Industry
        stock_data.industry = stock_data.industry.fillna("No Industry")
    except:
        print("\n"+Errors.TRANSFORMATION_ERROR)
        return stock_data, False
    else:
        return stock_data, True

def search_stock_api(stock_tickr,period):
    try:
        #Use Yahoo Finance to get Stock Data for a time period
        stock_tickr = stock_tickr.replace(" ","")
        stock_data = yf.Ticker(stock_tickr)
        print("\n","-"*30,stock_data.info["shortName"],"-"*30,"\n")
        
        start = None
        end = None
        if period[0] != "" and period[1] != "":
            start = period[0]
            end = period[1]
            period_arg = None
        else:
            period_arg = "max"

        stock_prices = stock_data.history(period=period_arg,start=start,end=end)
    except OverflowError as invalid_period:
        print("\n"+Errors.CAUGHT_EX.replace("&0",invalid_period))
        return ""
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
        
        #Apply Data Transformations
        stock_csv_df, trans_error = prep_stock_data(stock_csv_df)
        
        #Search for Stock Data based on Tickr Symbol/Name
        search_choice = 0
        stock_result = ""
        while search_choice != 3:
            try:
                search_choice = int(input("\nKindly select an option:\n1. Search by Tickr \n2. Search by Name \
                \n3. Exit\nSelect: "))      
                if search_choice == 1:
                    #Search Stock by Ticker
                    stock_tickr = input("\nEnter Stock Tickr Symbol: ")
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

            except ValueError:
                print("\n"+Errors.ONLY_NUMBERS)
    except FileNotFoundError:
        print("\n"+Errors.FILE_NOT_FOUND.replace("&1",Configuration.DATABASE_PATH))
    #except:
        #print("\n"+Errors.UNEXPECTED_ERROR)
