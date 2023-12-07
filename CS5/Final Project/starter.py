import random 
import time

class Board:
    """A data type representing a Connect-4 board
       with an arbitrary number of rows and columns.
    """
    def __init__(self, width, height):
        """Construct objects of type Board, with the given width and height.
        """
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
    
    def resetBoard(self):
        """clear the board
        """
        self.data = ' '

    def emptyBoard(self):
        """return True if the board is empty
            return False if the board is not empty
        """
        for row in range(self.height):
            for col in range(self.width):
                if self.data[row][col] != " ":
                    return False
        return True
    
    def fullBoard(self):
        """return True if the board is full
           return False if the board is not full
        """
        for row in range(self.height):
            for col in range(self.width):
                if self.allowsMove(col, row) == True:
                    return False
        return True

    def allowsMove(self, col, row):
        """Argument col: a int for col number
           Argument rwo: a int for row number
           check if an ox can be added
        """   
        if col in range(self.width) and row in range(self.height):
            if self.data[row][col] == ' ':
                return True
        return False
          
    def addMove(self, col, row, ox):
        """Argument col: an int for the col's index in which the checker will be added
           Argument ox: an one character string representing the checker to add to the board
           ox should be either 'X' or 'O'
        """
        col_num = self.width 
        row_num = self.height 
        
        if col in range(col_num) and row in range(row_num) and self.data[row][col] == " ":
            self.data[row][col] = ox
        
    def delMove(self, col, row):
        """delete the check at [col, row]
        """
        self.data[row][col] = " "

    def winsFor(self, ox):
        """
        """
        H = self.height
        W = self.width
        D = self.data

        for row in range(H):
            for col in range(W):
                if inarow_Neast(ox, row, col, D, 3) == True:
                    print('111111111111111111111111')
                    return True
                elif inarow_Nsouth(ox,row, col, D, 3) == True:
                    print("2222222222222222222222222")  
                    return True
                elif inarow_Nnortheast(ox, row, col, D, 3) == True:
                    print('333333333333333333333333333333')
                    return True
                elif inarow_Nsoutheast(ox,row, col, D, 3) == True:
                     print('44444444444444444444444444444444444')
                     return True
        return False
    
    def posToWin(self, ox):
        """Argument ox: a string, either "O" or "X"
           return an int for column and row number. If there is a col number to win, return the col number.
           If there is no way to win and a way to black the opponent, return the col number to block the opponent
           other, return the player's choice
        """
        row_num = self.height
        col_num = self.height

        pos_win = []
        for row in range(row_num):
            for col in range(col_num):
                if self.allowsMove(col, row) == True:
                    self.addMove(col, row, ox)
                    if self.winsFor(ox) == True:
                        pos_win += [[col, row]]
                    self.delMove(col, row)

        return pos_win
       
    def aiMove(self, ox):
        """Posititon for ai movement
        """
        allow_move_list = []
        count = 0
        
        if ox == 'X':
            ai = 'O'
        else:
            ai = 'X'
        
        for row in range(self.height):
            for col in range(self.width):
                if self.data[row][col] == ox:
                    count +=1

        list_win = self.posToWin(ai)   # list of pos for ai to win
        # print("list_win: ",  list_win)

        list_block = self.posToWin(ox)   # list of pos for ai to block
        print("list_block: ",  list_block)

        if len(list_win) > 0:
            print('win win win win win win win win win win')
            return random.choice(list_win)
        
        elif len(list_block) > 0:
            print('blokc blokc blokc blokc blokc blokc blokc blokc blokc blokc')
            return random.choice(list_block)
        
        elif self.emptyBoard() == True:
            row_pos = int(self.width//2 + 1)
            col_pos = int(self.height//2 + 1)
            return [row_pos, col_pos]
        
        elif count == 1:  # only one ox on board, take an edge position
                print('edgeedgeedgeedgeedgeedgeedgeedgeedgevvvedgeedgeedgeedgev')
                edge_pos = [[0, 0], [0, self.height-1], [self.width - 1, self.height -1], [self.width - 1, 0]]
                for char in (edge_pos):
                    if self.allowsMove(char[0], char[1]) == True:
                        allow_move_list +=[[char[0],char[1]]]
                return random.choice(allow_move_list)
        
        else:
            print('randomrandomrandomrandomrandomrandomrandomrandomrandom')
            for row in range(self.height):
                for col in range(self.width):
                    if self.allowsMove(col, row) == True:
                        allow_move_list += [[col, row]]
            print('randomrandomrandomrandomrandomrandomrandomrandomrandom')
            return random.choice(allow_move_list)

        
    def hostGame(self):
        """host a game
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
                player = input('Input or end: ' )

                if player.upper() == 'END':
                    condition = False
                    game_start = False
                    print()
                    print("The game is ended. Thank you for visiting")

                elif player.upper() in ['X', 'O']:
                    if player == "X":
                        ai = 'O'
                    else:
                        ai = 'X'
                    condition = False

            print('***********************')
            print('player is:', player)
            print('The opponent is:', ai)
            print('***********************')
            print()

        print("The rule of the game is....")
        # num = input('Please type num, the number of', player, 'in a row to win the game')
        print()


        if game_start == True:
            print('Do you wannt to go first?')
            print('If yes, please enter 1')
            print('If not, please eneter 2')
            go_first = input('Input: ')

            if go_first == '2':
                # pos = self.aiMove(player)
                self.addMove(1, 1, ai)
                print(self)
            
        while game_start == True:

            user_column = -1    # intentionally not valid!
            user_row = -1    # intentionally not valid!

            while self.allowsMove(user_column, user_row) == False:     # intentionally not valid, the first time...
                # user_string = input("Choose a column: ")
                user_string = input("Please choose a column: ")
                user_string_row = input("Please choose a row: ")
                try:
                    user_column = int(user_string)
                    user_row = int(user_string_row)

                except ValueError:       # in case an integer wasn't typed...
                    user_column = -1
                    user_string_row = -1

            self.addMove(user_column, user_row, player)      # a new board
            
            print()
            print(self)         # print the board
            
            if self.fullBoard == True:    # draw
                print('Draw')
            
            elif self.winsFor(player) == True:   # player wins
                print('Congratulaitons!', player, "wins the game")
                game_start = False

            elif self.winsFor(player):
                    print("Woops! The program wins the game")
                    game_start = False 
            else:    
                position = self.aiMove(player)
                print(position)
               
                self.addMove(position[0], position[1], ai)
                time.sleep(0.5)
                print(self) 
                
                

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
       
    if c_start > col_num:
        return False # out of bounds in cols
        
    for i in range(N):                  
        if A[r_start][c_start+i] != ch: # check for mismatches
            return False               
    return True                        

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
