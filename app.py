from os import system
# LEGEND
# 0 - free - f
# 1 - reserved - r
# 2- bought - b
seats = [ 0, 0, 1, 2, 0, 0, 0, 0 ]
# index   0, 1  2, ...........,7
option = -1

def clear_Console():
    system("cls")

while option !=0:
    # iterative count algorithm
    # HW1: let's say free_seats = len()
    free_seats = len(seats)
    for pi in range ( len(seats) ):
        if seats[pi] == 1 or seats[pi] == 2:
            free_seats -= 1
    # #############################
    
    # ########### PLOT ############
    print()
    for pi in range( len(seats) ):
        print("", pi+1, "", end = " ")
    print()
    
    for pi in range( len(seats) ):
        if seats[pi] == 1:
            print("|r|", end = " ")
        elif seats[pi] == 2:
            print("|b|", end=" ")
        elif seats[pi] == 0:
            print("|f|", end=" ")
    print("\nFree seats: ", free_seats)
    print("\n")
            
    # #############################
    
    # ########### MENU ############
    print("MENU")
    print("1. Book")
    print("2. Buy")
    print("3. Cancel")
    print("0. Exit")
    print("_"*30)
    # #############################

    try:
        option = int(input(">>> "))
        if option < 0 or option > 3:
            clear_Console()
            print("Value Error, only numbers from 1 to 3, or 0 for exit")
    except:
        clear_Console()
        print("Value Error, only numbers from 1 to 3, or 0 for exit")
    
    # HW2: add check condition:
    # - boundaries
    # - check if the place is free
    
    if option == 1:
        try:
            place = int(input("Which place? "))
        
            if seats[place-1] == 0:
                seats[place-1] = 1
                clear_Console()
            else:
                clear_Console()
                print("Sorry, this seats is reserved or bought")
        except:
            clear_Console()
            print("Value Error, only numbers from 1 to 8")
    # HW3: add buy, cancel + check ONLY IF BOOKED!
    if option == 2:
        try:
            place = int(input("Which place? "))

            if seats[place-1] == 0:
                seats[place-1] = 2
                clear_Console()
            else:
                clear_Console()
                print("Sorry, this seats is reserved or bought")
        except:
            clear_Console()
            print("Value Error, only numbers from 1 to 8")
            
    if option == 3:
        try:
            place = int(input("Which place? "))

            if seats[place-1] == 1:
                seats[place-1] = 0
                clear_Console()
            else:
                clear_Console()
                print("Sorry, this seats is reserved or bought")
        except:
            clear_Console()
            print("Value Error, only numbers from 1 to 8")
            
    if option == 0:
        exit()