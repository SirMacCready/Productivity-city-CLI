import json
from UI.scoring_interface import display_score
from UI.village_Interface import display_village
from UI.on_launch import clear_terminal,display_menu


checking = True

while checking :
    clear_terminal()
    choice = display_menu()
    if choice is "1" :
        display_score()
        
    elif choice is "2" : 
        display_village()
        
    else :
        checking = False
        clear_terminal()