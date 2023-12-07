from milestone import *

# this is the interface of the game
condition = True

while condition == True:
    b = Board()
    b.hostGame()
    print(b)
    
    print('Do you want to continue playing the game?')
    print('If you want to continue the game, please enter yes')
    print('If you want to exit the game, please enter no')
    
    user_input = input('input: ')

    if user_input.lower() == 'yes':
        condition == True
    elif  user_input.lower() == 'no':
        print('Thank you for visiting the game')
        condition == False
