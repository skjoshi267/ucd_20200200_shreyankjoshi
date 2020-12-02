#Import user menu
from user_menu import menu
#Import Configuration
from config import Configuration

#Start the application
if __name__ == "__main__":
    Configuration.initialize_color_scheme()
    #print("\n"+"-"*40+"\nWelcome to Justice League - Stock App\n"+"-"*40)
    main_menu_txt = Configuration.tabulate_output("MAINMENU")
    print(main_menu_txt+"\n")
    menu.user_menu()

#References
#https://pypi.org/project/colorama/
#https://pypi.org/project/tabulate/
