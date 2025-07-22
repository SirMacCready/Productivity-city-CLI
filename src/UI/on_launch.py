import os
import sys

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        sys.stdout.write('\033c')
        sys.stdout.flush()
    
def display_menu():
    print("|1.See my raw score\n")
    print("|2.Check on my village\n")
    print("|3.Exit\n") 
    
    choice = input("|your answer ->")

    return choice