from config import Configuration
from errors import Errors,Warnings
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn
import yfinance as yf
from datetime import datetime
from sklearn.linear_model import LinearRegression
import statsmodels.formula.api as smf
import pandas as pd

class Statistics:
    __stock_data_tickr = ""
    __stock_data = ""

    def __init__(self,symbol,stock_prices):
        self.__stock_data_tickr = symbol
        self.__stock_data = stock_prices
    
    def get_stock_data(self):
        return self.__stock_data

    def desc_stats(self):
        desc_stats_menu_txt = Configuration.tabulate_output("DESCSMENU")
        try:
            stats_choice = int(input("\n"+desc_stats_menu_txt+"\nSelect: "))
            if stats_choice in range(1,8) and stats_choice > 1:
                plt.close("all")
                fig = plt.figure()
                ax = plt.subplot()
                if stats_choice == 2:
                    self.raw_times_series()
                    x_label = "Time (Month-Day)"
                    y_label = "Closing Price"
                    title = "Time Series Analysis"
                elif stats_choice == 4:
                    sample_size = int(input("\nEnter the sample size for Moving Average: "))
                    self.moving_average(sample_size)
                    x_label = "Time (Month-Day)"
                    y_label = "Closing Price"
                    title = "Moving Average (n) vs 20 vs 50"
                elif stats_choice == 5:
                    weight_size = int(input("\nEnter the sample size for Moving Average: "))
                    self.weighted_mov_avg(weight_size)
                    x_label = "Time (Month-Day)"
                    y_label = "Closing Price"
                    title = "Weighted Average(10)"
                elif stats_choice == 6:
                    self.macd_avg()
                    x_label = "Time (Month-Day)"
                    y_label = "Closing Price"
                    title = "MACD"
                else:
                    pass
                date_form = mdates.DateFormatter("%m-%y")
                ax.xaxis.set_major_formatter(date_form)
                ax.set_xlabel(x_label)
                ax.set_ylabel(y_label)
                ax.set_title(title)
                plt.legend()
                plt.show()
            elif stats_choice == 1:
                print("\n")
                print(Configuration.tabulate_output("DATAFRAME",self.__stock_data.describe()))
            else:
                print("\n"+Errors.INVALID_CHOICE)
        except ValueError:
            print("\n"+Errors.ONLY_NUMBERS)
        except Exception as unknown:
            print("\n"+Errors.CAUGHT_EX.replace("&0",str(unknown)))
        finally:
            return None

    def raw_times_series(self):
        plt.plot(self.__stock_data.index,self.__stock_data.loc[:,"Close"],color = "orange",linewidth=1.5,label="Raw Time Series")

    def linear_trends(self):
        plt.plot(self.__stock_data.index,self.__stock_data.loc[:,"Close"],"o",color = "orange",linewidth=1.5,label="Linear Trend")

    def moving_average(self,n=10):
        self.raw_times_series()
        self.__stock_data_ma = self.__stock_data["Close"].rolling(window = n,min_periods = 1).mean()
        self.__stock_data_ma20 = self.__stock_data["Close"].rolling(window = 20,min_periods = 1).mean()
        self.__stock_data_ma50 = self.__stock_data["Close"].rolling(window = 50,min_periods = 1).mean()
        msa_n_label = "MSA-"+str(n)
        plt.plot(self.__stock_data_ma,color = "blue",linewidth = 1.0,label = msa_n_label)
        plt.plot(self.__stock_data_ma20,color = "red",linewidth = 1.0,label = "MSA-20")
        plt.plot(self.__stock_data_ma50,color = "green",linewidth = 1.0,label = "MSA-50")

    def calc_weighted_avg(self,stock_data):
        weights = np.arange(1,len(stock_data)+1)
        return np.dot(stock_data,weights).sum()/weights.sum()

    def weighted_mov_avg(self,n=10):
        self.raw_times_series()
        self.__stock_data_ma10 = self.__stock_data["Close"].rolling(window = 10,min_periods = 1).mean()
        self.__stock_data_wa = self.__stock_data["Close"].rolling(window = n,min_periods = 1).apply(lambda value : self.calc_weighted_avg(value),raw = True)
        plt.plot(self.__stock_data_ma10,color = "purple",linewidth = 1.0,label = "MSA-10")
        wma_n_label = "WMA-"+str(n)
        plt.plot(self.__stock_data_wa,color = "green",linewidth = 1.0,label = wma_n_label)

    def macd_avg(self):
        self.raw_times_series()
        self.__stock_data_ewm12 = self.__stock_data["Close"].ewm(span = 12,adjust = False).mean()
        self.__stock_data_ewm26 = self.__stock_data["Close"].ewm(span = 26,adjust = False).mean()
        self.__stock_data_macd = self.__stock_data_ewm26 - self.__stock_data_ewm12 
        plt.plot(self.__stock_data_macd,color = "green",linewidth = 1.0,label = "MACD")

    def predict_stock_price(self,stock_model_data,prediction_date):
        stock_model_data["Days"] = (stock_model_data.index - pd.to_datetime('1970-01-01')).days
        lr_model = smf.ols("Close ~ Days",data=stock_model_data)
        lr_model = lr_model.fit()
        base_date = datetime.strptime("1970-01-01","%Y-%m-%d").date()

        predicted_days = (prediction_date - base_date).days
        trend_line = lr_model.predict()
        predicted_value = lr_model.predict({"Days":predicted_days})
        print("\nPredicted Value is",predicted_value)
        plt.plot(stock_model_data["Days"],stock_model_data["Close"],"o",color="orange")
        plt.plot(stock_model_data["Days"],trend_line,"r",color="blue")
        plt.show()

    def pred_stats(self):
        exit_command = ""
        while exit_command != "E":
            try:
                exit_command = input("\nPress 'E' to exit or 'Enter' to continue ")
                if exit_command.upper() == "E":
                    break

                model_start = input("\nEnter Modelling Start Date: ")
                model_start = datetime.strptime(model_start,"%Y-%m-%d").date()

                model_end = input("\nEnter Modelling End Date: ")
                model_end = datetime.strptime(model_end,"%Y-%m-%d").date()

                if model_end <= model_start:
                    print("\n"+Errors.CAUGHT_EX.replace("&0","Model End Date cannot be smaller or equal to Model Start Date"))
                    continue

                predict_date = input("\nEnter Date for Prediction: ")
                predict_date = datetime.strptime(predict_date,"%Y-%m-%d").date()


                stock_data_pred = yf.Ticker(self.__stock_data_tickr)
                stock_data_pred_data = stock_data_pred.history(period="",start=model_start,end=model_end)
                self.predict_stock_price(stock_data_pred_data,predict_date)

            except ValueError as date_value:
                print("\n"+Errors.CAUGHT_EX.replace("&0",str(date_value)))
                continue
            except Exception as unknown:
                print("\n"+Errors.CAUGHT_EX.replace("&0",str(unknown)))
                continue