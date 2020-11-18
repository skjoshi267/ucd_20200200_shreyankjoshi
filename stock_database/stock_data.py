import pandas as pd
from config import Configuration
from errors import Errors

def prep_stock_data(stock_data):
    try:
        #Remove unwanted columns
        stock_data = stock_data.drop(columns = ["Unnamed: 8"],axis = 1)
        #Specify Missing Values for Industry
        stock_data.industry = stock_data.industry.fillna("No Industry")
        #Remove Stocks where IPO Year is missing
        stock_data = stock_data.drop(stock_data[stock_data["IPOyear"].isnull()].index)
        stock_data.reset_index(drop = True)
    except:
        print("-"*25+"\n"+Errors.TRANSFORMATION_ERROR)
        return True
    else:
        return False

def search_stock_api(stock_data,stock_tickr):
    return None

def search_stock_data(stock_data,stock_ticker,use_api):
    stock_ticker = stock_ticker.upper()
    if use_api:
        selected_stock = search_stock_api(stock_data,stock_ticker)
    else:
        selected_stock = stock_data[stock_data["Symbol"] == stock_ticker]
        if len(selected_stock) == 0:
            selected_stock = stock_data[stock_data["Symbol"].str.startswith(stock_ticker[0]) & \
            stock_data["Symbol"].str.endswith(stock_ticker[-1])]
            if len(selected_stock) == 0:
                selected_stock = search_stock_api(stock_data,stock_ticker)
            else:
                print("\nCouldn't find the tickr symbol. Here are some similar results:\n")
    return ( selected_stock if len(selected_stock) else None )       

def stock_main():
    print("Welcome to Justice League - Stock Listing")
    try:
        #Read the contents of the file
        stock_df = pd.read_csv(Configuration.DATABASE_PATH)
        
        #Apply Data Transformations
        use_api = prep_stock_data(stock_df)

        index = 0
        choice = ""
        while choice.upper() != "E":
            if index > 0:
                choice = input("\nKindly press (E) to exit or (S) to search again\n")
                if choice.upper() == "E" or choice.upper() == "S":
                    index -= 1
                    continue
                else:
                    print("-"*25+"\n"+Errors.INVALID_CHOICE)
                    continue

            index += 1
            stock_tickr = input("\nEnter Tickr Symbol:\n")
            #Search for Stock
            stock_results = search_stock_data(stock_df,stock_tickr,use_api)
            if len(stock_results):
                print(stock_results)
            else:
                print("-"*25+"\n"+Errors.NOT_FOUND.replace("&1",stock_tickr))
            
            
 
    except FileNotFoundError:
        print("-"*25+"\n"+Errors.FILE_NOT_FOUND.replace("&1",Configuration.DATABASE_PATH))
    except:
        print("-"*25+"\n"+Errors.UNEXPECTED_ERROR)
