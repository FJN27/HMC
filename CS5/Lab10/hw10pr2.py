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
        s = ''                          # The string to return
        for row in range(0, self.height):
            s += '|'
            for col in range(0, self.width):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2*self.width + 1) * '-' + "\n"   # Bottom of the board

       # print number under the line
       
        s +='\n'  # a new line
        for i in range(self.width):
            s += ' ' 
            if i > 9:
                s = s + str(i%10)
            else:
                 s += str(i)

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

        # Check to see if ox wins, starting from any checker:
        for row in range(0, H):
            for col in range(0, W-3):
                if D[row][col] == ox and D[row][col+1] == ox and \
                    D[row][col+2] == ox and D[row][col+3] == ox:
                        return True
        # check for vertical wins
        for row in range(0, H-3):
            for col in range(0, W):
                if D[row][col] == ox and D[row+1][col] == ox and \
                D[row+2][col] == ox and D[row+3][col] == ox:
                    return True
        # check for south-east diagonal wins
        for row in range(0, H-3):
            for col in range(0, W-3):
                if D[row][col] == ox and D[row+1][col+1] == ox and \
                D[row+2][col+2] == ox and D[row+3][col+3] == ox:
                    return True
        
        # check for north-west diagonal wins
        for row in range(0, H-3):
            for col in range(0, W-3):
                if D[row+3][col] == ox and D[row+2][col+1] == ox and \
                D[row+1][col+2] == ox and  D[row][col+3] == ox:
                    return True
    

        # but, if it looks at EACH row and col and never finds a win...
        return False     # only gets here if it never returned True, above
    
        
    def hostGame(self):
        """hosts a full game of Connect Four
        """

        player = 'X'
        
        while True:
            user_column = -1    # intentionally not valid!
            while self.allowsMove(user_column) == False:
                # intentionally not valid, the first time...
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
            if player == 'X':
                player = 'O'
            else:
                player = 'X'


bigb = Board(15,5)
b = Board(7,6)
