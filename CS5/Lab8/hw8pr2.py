# For this hw problem, solve any ten of the PythonBat problems on the three pages noted above.

# Be sure to name the functions the same as specified by PythonBat
# Copy your working and tested functions into a file named hw8pr2.py
# No docstrings needed!


'''
Given a string and a non-negative int n, return a larger string that is n copies of the original string.

string_times('Hi', 2) → 'HiHi'
string_times('Hi', 3) → 'HiHiHi'
string_times('Hi', 1) → 'Hi'
'''

def string_times(str, n):
  string = n*str
  return string


"""
Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;


front_times('Chocolate', 2) → 'ChoCho'
front_times('Chocolate', 3) → 'ChoChoCho'
front_times('Abc', 3) → 'AbcAbcAbc'

"""
def front_times(str, n):
    return n*str[0:3]


def string_bits(str):
  result = " "
  for i in range(len(str)):
  
    if i % 2 == 0:
      result = result + str[i]
  return result

"""
Given a string, return the count of the number of times that a substring length 2 
appears in the string and also as the last 2 chars of the string, 
so "hixxxhi" yields 1 (we won't count the end substring).

last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2

"""
def last2(str):
  
  count  = 0
  if len(str)< 2:
    return 0
  for i in range(len(str)-2):
   
    if str[i:i+2] == str[-2:]:
      count +=1
  return count

"""

Given an array of ints, return the number of 9's in the array.


array_count9([1, 2, 9]) → 1
array_count9([1, 9, 9]) → 2
array_count9([1, 9, 9, 3, 9]) → 3

"""
def array_count9(nums):
  count = 0
  for i in range(len(nums)):
    if nums[i] == 9:
      count +=1
  return count

"""

Given an array of ints, return True if one of the first 4 elements in the array is a 9. 
The array length may be less than 4.


array_front9([1, 2, 9, 3, 4]) → True
array_front9([1, 2, 3, 4, 9]) → False
array_front9([1, 2, 3, 4, 5]) → False
"""
def array_front9(nums):
  if len(nums) == 0:  # empty array
    return False
  elif len(nums) < 4:  # length < 4
    if 9 in nums:
      return True
    else:
      return False
  else:               # length >= 4
    if 9 in nums[0:4]:
      return True
    else:
      return False
    
"""
def array_front9(nums):
  # First figure the end for the loop
  end = len(nums)
  if end > 4:
    end = 4
  
  for i in range(end):  # loop over index [0, 1, 2, 3]
    if nums[i] == 9:
      return True
  return False
  
"""

"""
Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.


array123([1, 1, 2, 3, 1]) → True
array123([1, 1, 2, 4, 1]) → False
array123([1, 1, 2, 1, 2, 3]) → True
"""

def array123(nums):
  
  if len(nums) <3:  # length <3
    return False
  else:
    for i in range(len(nums)-2): # length >= 3
      if nums[i:i+3] == [1,2,3]:
        return True
  return False

"""
Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. 
So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.


string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0
"""
def string_match(a, b):
  # Figure which string is shorter.
  shorter = min(len(a), len(b))
  count = 0
  
  # Loop i over every substring starting spot.
  # Use length-1 here, so can use char str[i+1] in the loop
  for i in range(shorter-1):
    a_sub = a[i:i+2]
    b_sub = b[i:i+2]
    if a_sub == b_sub:
      count = count + 1

  return count

"""
def string_match(a, b):
  # nested loop a[0:2] == b[n:n+2]
  # a[1:3] == b[n:n+2]
  count = 0
  
  for i in range(len(a)-1):
    for n in range(len(b)-1):
      print("a[i:i+2]:", a[i:i+2])
      print("b[n:n+2]:", b[n:n+2])
      if a[i:i+2] == b[n:n+2]:
        count +=1
        
  return count
  """

#----------String 2-------------
"""
def double_char(str):
  result = " "
  for i in range(len(str)):
    result = result + 2*str[i]
  return result

def double_char(str):
  result = ""
  for i in range(len(str)):
    result += str[i] + str[i]
  return result

"""

"""
Given a non-empty string like "Code" return a string like "CCoCodCode".


string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
"""
def string_splosion(str):
  char = "" #NOTE: return a string, so use char = ""/ return a list, use LC = []/return a num, count = 0
  for i in range(len(str)):
    char = char + str[0:i+1]
    print(char)
    # str[0:1] --> str[0:i+1] i = 0
    # str[0:2] --> str[:i+1] i== 1 (first two char)
    # str[0:3] --> str[:i+1] i== 2 (first three char)
  return char


def double_char(str):
  
  result = ""
  for char in str:
    result = result + 2*char
  return result

"""

Return the number of times that the string "hi" appears anywhere in the given string.

count_hi('abc hi ho') → 1
count_hi('ABChi hi') → 2
count_hi('hihi') → 2

"""
def count_hi(str):
  count = 0
  for i in range(len(str)):
    if str[i:i+2] == "hi":
      count = count + 1
  return count

"""
Return True if the string "cat" and "dog" appear the same number of times in the given string.

cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True

"""
def cat_dog(str):
  count_dog = 0
  count_cat = 0
  for i in range(len(str)):
    if str[i:i+3] == "dog":
      count_dog +=1
    if str[i:i+3] == "cat":
      count_cat +=1 
  if count_cat == count_dog:
    return True
  else:
    return False

"""
Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.

end_other('Hiabc', 'abc') → True
end_other('AbC', 'HiaBc') → True
end_other('abc', 'abXabc') → True

"""

def end_other(a, b):
  if len(a) > len(b):
    b = b.lower()
    l = -1*len(b)
    a = a[l:]
    if a.lower()== b:
      return True
    else:
      return False
  elif len(a) < len(b):
    a = a.lower()
    l = -1*len(a)
    b = b[l:]
    if b.lower()== a:
      return True
    else:
      return False
  else:
    if a.lower() == b.lower():
      return True
    else:
      return False
    
"""
def end_other(a, b):
  a = a.lower()
  b = b.lower()
  return (b.endswith(a) or a.endswith(b))

"""

"""
Return True if the given string contains an appearance of "xyz"
where the xyz is not directly preceeded by a period (.).
So "xxyz" counts but "x.xyz" does not.

xyz_there('abcxyz') → True
xyz_there('abc.xyz') → False
xyz_there('xyz.abc') → True

"""

def xyz_there(str):
    return str.count('.xyz') != str.count('xyz')

"""
Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.

count_code('aaacodebbb') → 1
count_code('codexxcode') → 2
count_code('cozexxcope') → 2

"""
def count_code(str):
  count = 0
  for i in range(len(str)-3):     # subtracted three. String out of range otherwise
    if str[i:i+2] == "co" and str[i+3] =="e":
      count +=1
  return count


#-------------List 2 ------------
"""

Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.

count_evens([2, 1, 2, 3, 4]) → 3
count_evens([2, 2, 0]) → 3
count_evens([1, 3, 5]) → 0"""

def count_evens(nums):
  # even number--> n%2=0
  count = 0
  for char in nums:
    if char%2 == 0:
      count +=1
  return count


"""
Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.

big_diff([10, 3, 5, 6]) → 7
big_diff([7, 2, 10, 9]) → 8
big_diff([2, 10, 7, 2]) → 8

"""

def big_diff(nums):
  return max(nums) - min(nums)
  
"""
Return the "centered" average of an array of ints, which we'll say is the mean average of the values, 
except ignoring the largest and smallest values in the array. 
If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. 
Use int division to produce the final average. You may assume that the array is length 3 or more.


centered_average([1, 2, 3, 4, 100]) → 3
centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
centered_average([-10, -4, -2, -4, -2, 0]) → -3
"""

def centered_average(nums):
  
  sum_remove = sum(nums) - max(nums) - min(nums)
  avg_value  = sum_remove/(len(nums)-2)  # the avg value
  
  return avg_value

"""

Return the sum of the numbers in the array, returning 0 for an empty array. 
Except the number 13 is very unlucky, so it does not count and 
numbers that come immediately after a 13 also do not count.


sum13([1, 2, 2, 1]) → 6
sum13([1, 1]) → 2
sum13([1, 2, 2, 1, 13]) → 6

"""
def sum13(nums):
  if len(nums) == 0:
    return 0
  else: 
    for i in range(len(nums)):
      if nums[i] == 13:
        nums[i] = 0
        if i+1 < len(nums): 
          nums[i+1] = 0
       
    return sum(nums)
"""
def sum13(nums):
    sum = 0 
    condition = True
    
    for num in nums:
      if num == 13:
        condition = False
        continue
      
      if condition == False:
        condition = True
        continue
      
      if condition == True:
        sum = sum + num
        
    return sum
    
"""


"""
Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.


sum67([1, 2, 2]) → 5
sum67([1, 2, 2, 6, 99, 99, 7]) → 5
sum67([1, 1, 6, 7, 2]) → 4
"""

def sum67(nums):
  
  sum = 0
  condition = True
  
  for num in nums:
    if num == 6:
      condition = False
      continue     # the continue can be deleted

    if num == 7 and condition == False:
      condition = True
      continue       # continue is needed because the num 7 is NOT added to sum
      
    if condition == True:
      sum = sum + num   # the num is added only if the boolean variable condition = True
      
  return sum


"""
Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.


has22([1, 2, 2]) → True
has22([1, 2, 1, 2]) → False
has22([2, 1, 2]) → False
"""

def has22(nums):
  if len(nums) < 2:
    return False
  else:
    for i in range(len(nums)-1):
      if nums[i:i+2] == [2, 2]:
        return True
  return False
