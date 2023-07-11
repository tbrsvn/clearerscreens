from os import system, name

def clearerscreens(): 
    if name == 'nt': 
        x = system('cls') 
    else: 
        x = system('clear')