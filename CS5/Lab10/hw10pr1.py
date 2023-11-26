#
# hw10pr1.py 
#
# Name:
#

# First, the class definition
#
# ++ ALSO ++  below, we define several useful objects of type Date
#  +++ keep those and/or add your own! +++


class Date:
    """A user-defined data structure that
       stores and manipulates dates.
    """

    # The constructor is always named __init__ !
    def __init__(self, month, day, year):
        """Construct a Date with the given month, day, and year."""
        self.month = month
        self.day = day
        self.year = year


    # The "printing" function is always named __repr__ !
    def __repr__(self):
        """This method returns a string representation for the
           object of type Date that calls it (named self).

           ** Note that this function _can_ be called explicitly, but
              it more often is used implicitly via the print statement
              or simply by expressing self's value.
        """
        d = self.day
        m = self.month
        y = self.year
        string = f"{m:02d}/{d:02d}/{y:04d}"
        # The "d" after the integer stands for "_d_ecimal integer..."
        return string

        #
        # Note that we could have also written:
        #
        # return f"{self.month:02d}/{self.day:02d}/{self.year:04d}"
    
    # Here is an example of a "method" of the Date class:
    def isLeapYear(self):
        """Returns True if the calling object is
           in a leap year; False otherwise."""
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False

    def copy(self):
        """Returns a new object with the same month, day, year
           as the calling object (self).
        """
        
        dnew = Date(self.month, self.day, self.year)

        return dnew
    
    def equals(self, d2):
        """Decides whether self and d2 represent the same calendar date,
           regardless of whether they are in the same place in memory.
        """
        if self.year == d2.year and self.month == d2.month and self.day == d2.day:
            return True
        else:
            return False
    
    def __eq__(self, d2):
        """Overrides the == operator so that it declares two of the same dates
           in history as ==.  This way , we don't need to use the awkward
           d.equals(d2) syntax...
        """

        if self.year == d2.year and self.month == d2.month and self.day == d2.day:
            return True
        else:
            return False
        
    def isBefore(self, d2):
        """True if the calling object is a calendar date before the argument named d2
           If self and d2 represent the same day, this method should return False
           If self is after d2, return False.
           """
        # before d2, return True
        if self.year < d2.year:
            return True
        elif self.month < d2.month and self.year == d2.year:  # same year (before, value of month is smaller)
            return True
        elif self.day < d2.day and self.month == d2.month and self.year == d2.year:      # same year and month (before, day of month is smaller)
            return True

        return False
    
    def isAfter(self, d2):
        """Argument d2: 
           return True if the calling object is after the argument d2
           return False if d2 and the object represent the same date
           return Flase if the calling object is before the calling object
        """

        # return True if is after
        if self.year > d2.year:   
            return True
        elif self.month > d2.month and self.year == d2.year :  # same year (after, value of month is lager)
            return True
        elif self.day > d2.day and self.year == d2.year and self.month == d2.month:      # same year and month (after, value of day is lager)
            return True
        
        return False
    
    def tomorrow(self):
        """Changing the calling object so that it represents one calendar 
           day after the date it originally represented
        """
        fdays = self.isLeapYear() + 28 # the Boolean variable True has a int value of 1
                                       # the Boolean variable True has a int value of 0
                                       # leap year, 29 days in Feburary

        DIM = [0, 31, fdays, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
       
        
        if self.day == DIM[self.month] and self.month == 12:
            self.year += 1
            self.month = 1
            self.day = 1
            
        elif self.day == DIM[self.month]:
            self.month += 1
            self.day = 1
        else:
            self.day += 1

   
        
       
    def yesterday(self):
        """Changing the calling object so that it represents one calendar 
           day before the date it originally represented
        """
        fdays = self.isLeapYear() + 28

        DIM = [0, 31, fdays, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


        if self.month == 1 and self.day == 1: # one year forward
             self.year -=1
             self.month = 12
             self.day = 31

        elif self.day == 1:
            self.month -= 1
            self.day = DIM[self.month]
        else:
            self.day -= 1

    def addNDays(self, N):
        """ change the calling object so that it represents N calendar days 
            after the date it originally represented.
        """

        # call the function for N time
        for i in range(N):
           self.tomorrow()

    def subNDays(self, N):
        """Return the difference between two dates
        """
        for i in range(N):
            self.yesterday

    def diff(self, d2):

        selfcopy = self.copy()
        d2copy = d2.copy()
        count = 0

        # same date 
        if selfcopy.equals(d2copy):
            return count
        
        # selfcopy is before d2copy
        elif selfcopy.isBefore(d2copy):
            while selfcopy.isBefore(d2copy) == True:
                selfcopy.tomorrow()
                count +=1
                # print('d2', d2)
                print('selfcopy.isBefore(d2copy)', selfcopy.isBefore(d2copy))
            return -count 
        
        elif selfcopy.isAfter(d2copy):
            while selfcopy.isAfter(d2copy) == True:
                selfcopy.yesterday()
                count +=1
                # print(selfcopy)
            return count 
        

    def dow(self):
        """ returns one of the following strings: "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", or "Sunday".
        """
        today = Date(11, 9, 2023) # Tuesday

        difference = self.diff(today)  # difference in days

        week = ["Tuesday", "Friday", "Saturaday", "Sunday", "Monday", "Tuesday", "Wednesday"]
       
        return week[difference%7]


# Be sure to add code for the Date class ABOVE--indented inside the class
# definition
#

#
# Lots of dates to work with...
#
# The nice thing about putting them here is that they get redefined with
#   each run of the software (needed for testing!)
#

d = Date(11, 9, 2023)     # Today? Yesterday?
d2 = Date(5, 11, 2024)    # Start of summer break
ny = Date(1, 1, 2024)     # New year
nd = Date(1, 1, 2030)     # New decade
nc = Date(1, 1, 2100)     # New century
graduation = Date(5, 16, 2027)    # Alter to suit!
nextsemester = Date(1, 16, 2024)  # Start of classes next semester
wd = Date(11, 12, 2013)   # A popular wedding day
wd2 = Date(11, 12, 2013)  # A copy of wd, to check == and .equals()
wd10 = Date(10, 10, 2010)  # 10/10/10
sm1 = Date(10, 28, 1929)  # One stock market crash
sm2 = Date(10, 19, 1987)  # Another crash: October Mondays are risky!