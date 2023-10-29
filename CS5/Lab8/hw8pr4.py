#
# hw8pr4.py
#

#
# Example user-interaction looping program
#  (a variant of the one we reviewed in class)
#

def menu():
    """Prints the menu of options that the user can choose."""
    print()
    print("(0) Enter a new list")
    print("(1) Continue (and re-print)!")
    print("(2) Find the average price")
    print("(3) Find the standard deviation")
    print("(4) Find the minimum and its day")
    print("(5) Find the maximum and its day")
    print("(6) Your TT investment plan")
    print("(9) Break! (quit)")
    print()


def avg_price(L):
    """Argument: a list of int
       Return a int/float: average value
    """
    sum = 0
    length = len(L)
    for i in range(len(L)):
        sum = L[i] + sum 
    return sum/length

import math

def standard_deviation(L):
    """Argument L: a list of number
       Return an int/float: standard deviation of the list
    """

    L_avg = avg_price(L) # average value of the list
    deno = 0
    if len(L) == 0: # empty list: SD = 0
        return 0
    else:
        for i in range(len(L)):
            deno += (L[i] - L_avg)**2   
            SD = math.sqrt(deno/len(L))    
    return SD     
            

def min(L):
    """Argument L: a list of int
    Return an int/float: min(L) and index of min(L)
    """
    
    if len(L) == 0: # empty list
        return 0
    
    elif len(L) == 1:
       return L[0]
    
    else:   # non-empty list
        min = L[0]
        index = 0
        for i in range(len(L)):
            if min > L[i]:
                min = L[i]
                index +=1
    return min, index
   
   # return min(L), L.index(min(L)) no built-in function allowed


def max_index(L):
    """Argument L: a list of int
       Return an int/float: max(L) and index of max(L)
    """
    
    if len(L) == 0: # empty list
        return 0
    
    elif len(L) == 1:
       return L[0]
    
    else:   # non-empty list
        max = L[0]
        index = 0
        for i in range(len(L)):
            if L[i] > max:
                max = L[i]
                index +=1
    return max, index
   
   # return max(L), L.index(max(L)) no built-in function allowed


def max_noindex(L):
    """Argument L: a list of int
       Return an int/float: max(L) and index of max(L)
    """
    
    if len(L) == 0: # empty list
        return 0
    
    elif len(L) == 1:
       return L[0]
    
    else:   # non-empty list
        max = L[0]
        for i in range(len(L)):
            if L[i] > max:
                max = L[i]
                
    return max

def max_profit(L):
    """Argument L: a list of int/float
       Return a list
    """
    diff = []
    if len(L) == 0:
        return " "
    else:
        for i in range(len(L)):  # i = sell 
            # LoL = [[L[i] - L[n], i, n] for n in range(i, len(L))]
            for n in range(i, len(L)):   # n = buy
                diff += [[L[i]-L[n], L[i], L[n], i, n,]]  # a list of profits
    diff = max_noindex(diff)

    return diff
 


def main():
    """The main user-interaction loop.
    """
    secret_value = 4.2

    L = [30, 10, 20] # list of price
    
    while True:      
        print("\n\nThe list is", L)
        menu()
        choice = input("Choose an option: ")
 
        try:
            choice = int(choice)   # Make into an int!
        except:
            print("I didn't understand your input! Continuing...")
            continue


        if choice == 9:    # We want to quit
            break          # Leaves the while loop altogether

        elif choice == 1:  # We want to continue (and print) ...
            print(L)

        elif choice == 0:  # We want to enter a new list
            newL = input("Input a new list: ")   

            try: 
                newL = eval(newL) # eval runs Python's interpreter! 
                if type(newL) != type([]): 
                    print("That didn't seem like a list. Not changing L.")
                else: 
                    L = newL  # Here, things were OK, so let's set our list, L
            except:
                print("I didn't understand your input. Not changing L.")

        elif choice == 2:   #fing the average price
            avg = avg_price(L)
            print("The average price is:", avg)

        elif choice == 3:  # Unannounced menu option!
            SD = standard_deviation(L)
            print("The standard deviation of L is:", SD)

        elif choice == 4: 
            LC = min(L)
            print("The minimum price is:" ,LC[0])
            print("The index is:", LC[1])

        elif choice == 5:  
            LC = max_index(L)
            print("The maximum price is:" ,LC[0])
            print("The index is:", LC[1])

        elif choice == 6:

            LC = max_profit(L)
            profit = LC[0]
            sell_price = L[1] # he sell day must be greater than or equal to the buy day.
            buy_price = L[2]
            sell_day = LC[3]
            buy_day = LC[4]

            print(LC)
            print("The maximum profit is:", profit)
            print("The sell price is:", sell_price)
            print("The buy price is:", buy_price)
            print("The sell day is:", sell_day)
            print("The buy day is:", buy_day)

        else:
            print(choice, " That's not on the menu!")
    print()
    print("See you(Actually, never see you again!!!)!")

