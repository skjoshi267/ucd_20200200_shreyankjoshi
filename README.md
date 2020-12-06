# ucd_20200200_shreyankjoshi
 Programming to Analytics - Project (UCD20200200)

# Introduction:
Justice Stock App is designed to highlight a plethora of descriptive summary measures and predictive modelling via linear regression framework. While the initial prototype has limited capabilities in terms of modelling, user interaction and predictive algorithms, it certainly can be refined further to gain meaningful insights about the volatility in stock market. The following sections in the report shall cover the steps for user manual. 

# Pre-Requisites:
JL Stock App uses a diverse set of modules based on Python 3.8. The detailed versioning for all those modules can be found in requirements.txt. For proper functioning of the app, it is suggested to use the listed versions for each module. Moreover, the app uses excel resources and text files stored within the relevant folders. A virtual environment has also been added to the directory which can be used to run the app without having to perform any additional installation. The app tries to fetch recent data from the internet hence, having an internet connection up and running is mandatory. Functionality to read the data contents offline are limited to generating a minor report based on past data from the underlying excel file. 

# Assumptions:
JL Stock App leverages advanced concepts of statistical analysis and it is assumed the user is familiar to get the best out of it using relevant data. Furthermore, the GUI is developed is limited capacity and can only used for summary statistics as the moment. The other features are for demo purposes and yield no significant results. User shall follow the instructions given on the screen for fruitful running of the app.

# Run the App:
In general sense, running the app is simple provided the requirements as mentioned in the requirements.txt are fulfilled. Open Anaconda Prompt or Command Line on your terminal. Navigate to the project directory until the file jl_stock.py is located. Run the command, ‘python jl_stock.py’. The main screen loads up welcoming the user. For the time, login or registration facility has not been added given the absence of database.

# Main Screen:
On running the app successfully, the user is greeted with the mode of operation for the app.  The user can opt to run the app in GUI or Command Line. As stated previously the Command Line mode of operation is baked with major features in comparison to GUI. 

# Display Menu:
If the user selects CLI then he/she is requested to enter an operation to perform. Search and Analyze stock shall permit user to search for a particular stock based on Tickr symbol or Name. Ideally a user has knowledge of Tickr symbols for different corporations. However, a search function has been enabled for the user to find an organization. The search feature is presented in a limited functionality and works for complete name without options for wildcard characters and fuzzy search. 
Search and Analyze Stock:
Post selecting the search and analyze menu in the app, the user can search stock prices via Tickr Symbols, Name or exit the app. The user can also select a start date and end date to fetch stock prices for a relevant period. Validation for dates is baked in and in the event of unsupported date the app will request user to select a time range. Failing 
to select correct time range shall set maximum range by default.  If the stock prices are available, they will be fetched for relevant symbol and date range. 

# Descriptive Statistics:
Post successfully fetching the stock prices, the user can choose to conduct a wide range of descriptive statistics on the dataset. Starting with count, max, min, range, quartiles, mean and variance to raw time series. Besides, time series analysis, the user can also perform analysis such as moving averages, weighted moving averages, and converging/diverging moving averages. User can select options for output range by providing inputs. Graphs are plotted for all relevant statistical measures with proper legends, axis and titles. 

# Predictive Statistics:
User can leverage predictive analytics by choosing a specific time interval for training the algorithm. Predictive analysis is incorporated using simple linear regression based on historical data. While the accuracy for the model could be average, it does give a general idea of the regression trendline. For predicting the value of a stock, select a relevant date and the predicted value will be displayed in the terminal. 

# Generate Report:
Generate report asks the user to input a Tickr symbol and generate relevant descriptive measures offline from the underlying excel file. Additionally, the report can be upscaled to generate PDF reports based on statistical analysis and predictive analysis in the future. 

# Metadata:
The metadata option for the report provides Github link where user can log issues and communicate with the developers. Furthermore, it also provides the requirements.txt in the terminal. 
 
