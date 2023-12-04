import random

class Board:
    """A data type representing a Connect-4 board
       with an arbitrary number of rows and columns.
    """

    def __init__(self, width, height):
        """Construct objects of type Board, with the given width and height."""
        self.width = width
        self.height = height
        self.data = [[' ']*width for row in range(height)]

        # We do not need to return anything from a constructor!

    def __repr__(self):
        """This method returns a string representation
           for an object of type Board.
        """
        s = ''   
        count = 0                        # The string to return
        for row in range(0, self.height):
            s += '|'
            for col in range(0, self.width):
                s += self.data[row][col] + '|'
            s += '\n'    # 
            count +=1

        s += (2*self.width + 1) * '-' + "\n"   # Bottom of the board

       # print number under the line
       
        s +='\n'  # a new line
        for i in range(self.width):
            s += ' ' 
            if i > 9:
                s = s + str(i%10)
            else:
                 s+= str(i) 
        for col in range(self.height):
            print('')

        return s       # The board is complete; return it
    
    def addMove(self, col, ox):
        """Argument col: an int for the col's index in which the checker will be added
           Argument ox: an one character string representing the checker to add to the board
           ox should be either 'X' or 'O'
        """
        # find the row and col position(index of row and col), and replace [row][col] with ox
        # index of col = col
        row = self.height - 1     # index of row
        
        while row >=0:
            if self.data[row][col] == " ":
                self.data[row][col] = ox
                break
            else:
                row = row - 1   # not an empty space, move up (index -1)
    
    def clear(self):
        """Clear the board
        """
        self.data = ''
       
# This is the end of the Board class
# Below are some boards that will be re-created each time the file is run:

    def setBoard(self, moveString):
        """Accepts a string of columns and places
           alternating checkers in those columns,
           starting with 'X'.

           For example, call b.setBoard('012345')
           to see 'X's and 'O's alternate on the
           bottom row, or b.setBoard('000000') to
           see them alternate in the left column.

           moveString must be a string of one-digit integers.
        """
        nextChecker = 'X'   # start by playing 'X'
        for colChar in moveString:
            col = int(colChar)
            if 0 <= col <= self.width:
                self.addMove(col, nextChecker)
            if nextChecker == 'X':
                nextChecker = 'O'
            else:
                nextChecker = 'X'

    def allowsMove(self, c):
        """Argument c: an int for col number
           return True if the calling object (of type Board) does allow a move into column c
           returns False if column c is not a legal column number for the calling object
           returns False if column c is full
        """

        # c is not in range of col, return false
        if c not in range(self.width):
            return False
        
        # col is full, return False
        else:
            for row in range(self.height):
                if self.data[row][c] != " ":     # not empty, check the above position
                    row -=1
                else:   # empty, return True
                    return True
        return False
             
    def isFull(self):
        """return True if the calling object (of type Board) is completely full of checkers.
        """

        # nested loop to check each index
        for col in range(self.width):
            for row in range(self.height):
                if self.data[col][row] == " ":  # empty, return false
                    return False

        return True
    
    def delMove(self, c):
        """Argument c: an int for col number
           Remove a check from the board
        """
        for i in range(self.height):
            if self.data[i][c] != " ":
                self.data[i][c] = " "
                break
            # empty, change the row number

    def winsFor(self, ox):
        """Argument ox: a one character string for either "O" or "X"
           return True if there are four checkers of type ox in a row on the board. 
           return False otherwise. 
        """
        H = self.height
        W = self.width
        D = self.data
        for row in range(H):
            for col in range(W):
                if inarow_Neast(ox, row, col, D, 4) == True:
                    print('111111111111111111111111')
                    return True
                elif inarow_Nsouth(ox,row, col, D, 4):
                    print("2222222222222222222222222")  
                    return True
                elif inarow_Nnortheast(ox, row, col, D, 4):
                    print('333333333333333333333333333333')
                    return True
                elif inarow_Nsoutheast(ox,row, col, D, 4):
                     print('44444444444444444444444444444444444')
                     return True
        return False

    def colsToWin(self, ox):
        """Argument ox: a string character, either "O" or "X"
            return the list of columns (in numeric value) where ox can move 
            in the next turn in order to win and finish the game
        """
        H = self.height   # row
        W = self.width    # col
        
        list_win = []
        for col in range(W):             
            if self.allowsMove(col) == True:    # check all empties places
                self.addMove(col,ox)            # add a checker: addMove(ox)
                if self.winsFor(ox) == True:    # if have four ox --- > put the col number in a list
                    list_win += [col]
                self.delMove(col)               # delete

        return list_win                         # return the list
    
    def aiMove(self, ox):
        """Argument ox: a string, either "O" or "X"
           return an int for column number. If there is a col number to win, return the col number.
           If there is no way to win and a way to black the opponent, return the col number to block the opponent
           other, return the player's choice
        """
        row_num = self.height    # total row number
        col_num = self.width    # total col number
        D = self.data

        if ox == 'X':
            opponent  = 'O'
        else:
            opponent = 'X'

        list_win = self.colsToWin(ox)    # list of int for col number for ox to wins
        list_block = self.colsToWin(opponent)  # list of int for col number for ox to block

        if len(list_win) > 0:    # has col number to win
            return random.choice(list_win)
        
        elif len(list_block) > 0:     # can block
            return random.choice(list_block)
        else:
            col_list = []
            # the opponent has two markers in a row, and both sides are empty  
            """ if inarow_Neast(ox, row, col, D, 4) and self.allowsMove(col - 1) and self.allowsMove(col - 1):    
                self.addMove(col+1, opponent)"""
            
            for col in range(self.width): 
                for row in range(self.height):
                    # | |x|x| |
                    if inarow_Neast(ox, row, col, D, 2) and self.allowsMove(col - 1) and self.allowsMove(col + 1): 
                        # | x| |x|x| | | --->| x|O|x|x| | |
                        if (col - 2) in range(self.width) and D[row][col - 2] == ox:
                            print(col - 1, 'hihihihihihihiihihihhihi')
                            return (col - 1)
                        
                        # | | |x|x| |O| --->| x| |x|x|O|X|
                        elif (col - 2) in range(self.width) and (col+3) in range(self.width) and D[row][col+3] == ox:
                            print(col + 3)
                            return (col + 3)
                        
                        # | |x|x| |, must have a 'O'
                        else:
                            LC = [col-1, col + 1]
                            return random.choice(LC)
                        
                    elif self.data[row][col] == ox and self.allowsMove(col) == True:    # has a ox, try to make a vertical line
                         col_list += [col]
                         print(col_list)

                    elif len(col_list) == 0 :     
                        for col in range(self.width):
                            if self.allowsMove(col) == True:
                                col_list += [col]
            return random.choice(col_list)

    def hostGame(self):
        """hosts a full game of Connect Four
        """

        print('Hi, welcome to this boring game')
        print()
        
        print("Please decide if you want be 'X' or 'O.'\n Typo is NOT accepted at Harvey Mudd College since eah student is expected take Introduction to academic writing.")
        
        player = input("X or O: " )
        player = player.upper()
        print()

        condition = True

        game_start = True

        while condition == True:
            if player == 'X':
                ai = "O"
                condition = False
                # print("Opponent: ", ai)
            elif player == 'O':
                ai = "X"
                condition = False
            else:
                print('Your input is unavaible. Please re-choose!')
                print("If you want to end the game, please type end.")
                user_input = input('Input or end: ' )

                if user_input.upper() == 'END':
                    condition = False
                    game_start = False
                    print()
                    print("The game is ended. Thank you for visiting")

                elif user_input.upper() in ['X', 'O']:
                    if user_input == "X":
                        ai = 'O'
                    else:
                        ai = 'X'
                    condition = False

            print('User: ', player)
            print("Opponent: ", ai)
            print()


        while game_start == True:
            user_column = -1    # intentionally not valid!

            while self.allowsMove(user_column) == False:     # intentionally not valid, the first time...
                # user_string = input("Choose a column: ")
                user_string = input("Please choose a column: ")
                try:
                    user_column = int(user_string)
                except ValueError:       # in case an integer wasn't typed...
                    user_column = -1
                
            self.addMove(user_column, player)      # a new board

            print(self)         # print the board
                
            if self.winsFor(player) == True:
                print('Congratulaitons!', player, "wins the game")
                break 
            else:
                self.aiMove(ai)
                col_pos = self.aiMove(ai)
    
                self.addMove(col_pos, ai)
                print(self) 

                if self.winsFor(ai) == True:
                    print("Woops! The program wins the game")
                    break 


def inarow_Neast(ch, r_start, c_start, A, N):
    """Argument ch: a string for character
       r_start: an int for row position
       c_start: a int for col position
       Argument A: an 2D array list
       Argument N: an int for the number of ch in a col
    """
    row_upper_bound = len(A)      # number of rows is len(A)
    col_num = len(A[0]) - N  # number of cols is len(A[0]) 

    if r_start >= row_upper_bound:
        return False # out of bounds in rows
        # other out-of-bounds checks...
    if c_start > col_num:
        return False # out of bounds in cols
        # are all of the data elements correct?
    for i in range(N):                  # loop index i as needed
        if A[r_start][c_start+i] != ch: # check for mismatches
            return False                # mismatch found--return False
    return True                         # loop found no mismatches--return True


def inarow_Nsouth(ch, r_start, c_start, A, N):
    """Argument ch: a string for character
       r_start: an int for row position
       c_start: a int for col position
       Argument A: an 2D array list
       Argument N: an int for the number of ch in a row
    """
    
    row_upper_bound = len(A) - N
    col_upper_bound = len(A[0]) 
    
    if r_start  > row_upper_bound or c_start > col_upper_bound:
        return False
    
    for i in range(N):                  
        if A[r_start+i][c_start] != ch: 
            return False               
    return True


def inarow_Nnortheast(ch, r_start, c_start, A, N):
    """Argument ch: a string for character
       r_start: an int for row position
       c_start: a int for col position
       Argument A: an 2D array list
       Argument N: an int for the number of ch in the southeast dir
       return True if N elements are consecutively arranged in southeast dir
       return False otherwise
    """

    row_upper_bound = len(A)      # number of rows is len(A)
    col_upper_bound = len(A[0]) - N

    if r_start >= row_upper_bound:
        return False # out of bounds in rows
   
    if c_start > col_upper_bound:
        return False # out of bounds in cols
   
    for i in range(N):                 
        if A[r_start-i][c_start+i] != ch:   # elements are diffferent
            return False                  
    return True                           

def inarow_Nsoutheast(ch, r_start, c_start, A, N):
    """Argument ch: a string for character
       r_start: an int for row position
       c_start: a int for col position
       Argument A: an 2D array list
       Argument N: an int for the number of ch in the southeast dir
       return True if N elements are consecutively arranged in southeast dir
       return False otherwise
    """
    col_upper_bound = len(A[0]) - N
    row_upper_bound = len(A) - N

    if c_start > col_upper_bound or r_start > row_upper_bound:
        return False
    
    for i in range(N):
        if ch != A[r_start + i][c_start + i]:
            return False

    return True

bigb = Board(15,5)
b = Board(7,6)
