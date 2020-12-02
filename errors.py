from colorama import Fore,Style
#Error Messages
class Errors:
    #Error - Standard
    CAUGHT_EX = Fore.RED+"&0"+Style.RESET_ALL
    #Error - When expected input is number but string is entered.
    ONLY_NUMBERS = Fore.RED+"Valid Choices are only Numbers. Please Try Again!"+Style.RESET_ALL
    #Error - When choice selected is out of domain
    INVALID_CHOICE = Fore.RED+"Please Select a Valid Choice!"+Style.RESET_ALL
    #Error - No Such File or Directory Found
    FILE_NOT_FOUND = Fore.RED+"Unable to Locate &1. Kindly Check Configuration"+Style.RESET_ALL
    #Error - Unexpected Error
    UNEXPECTED_ERROR = Fore.RED+"Unexpected Error. Kindly contact Developer"+Style.RESET_ALL
    #Error - Type Error
    TYPE_MISMATCH = Fore.RED+"Unable to Convert Tickr Symbol"+Style.RESET_ALL
    #Error - No Data Found. Return Suggestions
    NOT_FOUND = Fore.RED+"No Search Results were found for &1 \
    \nKindly search with the Tickr Symbol"+Style.RESET_ALL
    #Error - Invalid Dates Entered
    INVALID_PERIOD = Fore.RED+"Invalid Period Entered"+Style.RESET_ALL
    
#Warning Messages
class Warnings:
    #Warning - Unable to transform data. Please proceed with caution
    TRANSFORMATION_ERROR = Fore.RED+"Errors Occured during Data Transformation, Using API"+Style.RESET_ALL
    #Warning - Multiple Results Found
    MULTIPLE = Fore.YELLOW+"Multiple Search Results were found for &1\nKindly search with the Tickr Symbol"+Style.RESET_ALL
    #Warning - No Data Was Found
    DATA_NOT_FOUND = Fore.YELLOW+"Company is Delisted or Incorrect Information Given"+Style.RESET_ALL
    #Warning - Standard
    CAUGHT_EX = Fore.YELLOW+"&0"+Style.RESET_ALL