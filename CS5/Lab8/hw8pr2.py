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



#String 2
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
  
 